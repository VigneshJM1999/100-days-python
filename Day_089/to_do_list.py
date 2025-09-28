from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean, Date
from flask_bootstrap import Bootstrap5
from datetime import datetime, date

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///task.db'

Bootstrap5(app)

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
db.init_app(app)

class Task(db.Model):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    date: Mapped[datetime.date] = mapped_column(Date)
    task_done: Mapped[bool] = mapped_column(Boolean, default=False)
    task: Mapped[str] = mapped_column(String, nullable=False)
    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

with app.app_context():
    db.create_all()

@app.route("/")
def home():
    result = db.session.execute(db.select(Task).order_by(Task.id))
    all_tasks = result.scalars().all()
    today_date = date.today()
    return render_template("index.html", tasks=all_tasks, now=today_date)

@app.route("/add", methods=["POST"])
def add_task():
    task_description = request.form.get("task")
    date_str = request.form.get("date")
    if date_str:
        task_date = datetime.strptime(date_str, "%Y-%m-%d").date()
    else:
        task_date = date.today()

    new_task = Task(
        task=task_description,
        date=task_date,
        task_done=False
    )
    db.session.add(new_task)
    db.session.commit()
    return redirect(url_for("home"))

from flask import request, redirect, url_for, flash

@app.route("/edit/<int:task_id>", methods=["GET", "POST"])
def edit_task(task_id):
    task = Task.query.get_or_404(task_id)

    if request.method == "POST":
        task.task = request.form["task"]
        date_str = request.form.get("date")
        if date_str:
            task.date = datetime.strptime(date_str, "%Y-%m-%d").date()
        db.session.commit()
        flash("Task updated successfully!")
        return redirect(url_for("home"))

    return render_template("edit.html", task=task)

from flask import redirect, url_for, flash

@app.route("/delete/<int:task_id>", methods=["POST", "GET"])
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    flash("Task deleted successfully!")
    return redirect(url_for("home"))


@app.route("/update/<int:task_id>", methods=["POST"])
def update_status(task_id):
    task_to_update = db.get_or_404(Task, task_id)
    task_to_update.task_done = 'task_done' in request.form

    db.session.commit()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
