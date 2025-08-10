from flask import Flask

app = Flask(__name__)

def make_bold(function):
    def wrapper_function():
        return f"<b>{function()}</b>"
    return wrapper_function

def make_emphasis(function):
    def wrapper_function():
        return f"<em>{function()}</em>"
    return wrapper_function

def make_underlined(function):
    def wrapper_function():
        return f"<u>{function()}</u>"
    return wrapper_function

@app.route("/")
def hello_world():
    return ("<h1>Hello, World!</h1>"
            "<p>This is a paragraph</p>"
            "<img src='https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExaGpvZGRtMTZsNDl2NndtaWZhZmFyZXJ5M29hZ3A5cDBkZXk1amc0bSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/WUh3L3WWY1IJvpAc1z/giphy.gif' width=500px, height=500px>")

@app.route("/<path:username>/<int:number>")
def greet_user(username, number):
    return f"Hello, {username}! You are {number} years old"

@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def bye():
    return "<h1>Bye!</h1>"

if __name__ == "__main__":
    app.run(debug=True)
