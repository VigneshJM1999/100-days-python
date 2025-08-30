from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
import random

'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)

class Base(DeclarativeBase):
    pass

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/random")
def get_random_cafe():
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()
    if all_cafes:
        random_cafe = random.choice(all_cafes)
        return jsonify(cafe=random_cafe.to_dict())
    else:
        return jsonify(error={"Not Found": "No cafes found in the database."}), 404

@app.route("/all")
def get_all_cafes():
    result = db.session.execute(db.select(Cafe).order_by(Cafe.name))
    all_cafes = result.scalars().all()
    return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])

@app.route("/search")
def search_for_cafe():
    query_location = request.args.get("loc").capitalize()
    if not query_location:
        return jsonify(error={"Bad Request": "Missing 'loc' parameter."}), 400
    result = db.session.execute(db.select(Cafe).where(Cafe.location == query_location))
    location_cafes = result.scalars().all()
    if location_cafes:
        return jsonify(cafes=[cafe.to_dict() for cafe in location_cafes])
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."}), 404

@app.route("/add", methods=['POST'])
def add_cafe():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("loc"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})

@app.route("/update-price/<int:cafe_id>", methods=['PATCH'])
def update_price(cafe_id):
    cafe_to_update = db.get_or_404(Cafe, cafe_id)
    new_price = request.args.get("new_price")
    if new_price:
        cafe_to_update.coffee_price = new_price
        db.session.commit()
        return jsonify(success=f"Successfully updated the price for cafe {cafe_id}."), 200
    else:
        return jsonify(error={"Bad Request": "Missing 'new_price' parameter."}), 400


@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    api_key = request.args.get("api-key")

    if api_key != "TopSecretAPIKey":
        return jsonify(error={"Forbidden": "Sorry, that's not allowed. Make sure you have the correct api_key."}), 403

    cafe_to_delete = db.get_or_404(Cafe, cafe_id)

    db.session.delete(cafe_to_delete)
    db.session.commit()

    return jsonify(response={"success": "Successfully deleted the cafe."}), 200


if __name__ == '__main__':
    app.run(debug=True)
