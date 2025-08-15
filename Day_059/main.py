from flask import Flask, render_template
from post import Post
import requests

posts = requests.get("https://api.npoint.io/674f5423f73deab1e9a7").json()
all_posts = []
for post in posts:
    temp = Post(post["id"], post["title"], post["subtitle"], post["body"], post["image_url"])
    all_posts.append(temp)


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", all_posts=all_posts)

@app.route('/post/<int:number>')
def post(number):
    requested_blog = None
    for blog in all_posts:
        if blog.id == number:
            requested_blog = blog
    return render_template("post.html", post=requested_blog)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
