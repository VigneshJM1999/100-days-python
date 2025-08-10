from flask import Flask, render_template
from post import Post
import requests

posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
all_posts = []
for post in posts:
    temp = Post(post["id"], post["title"], post["subtitle"], post["body"])
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

if __name__ == "__main__":
    app.run(debug=True)
