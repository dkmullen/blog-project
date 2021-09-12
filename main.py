from flask import Flask, render_template
import requests

app = Flask(__name__)
all_posts = []


@app.route('/')
def home():
    global  all_posts
    response = requests.get("https://api.npoint.io/e42b353ee387383898c7")
    all_posts = response.json()
    print(all_posts)
    return render_template("index.html", posts=all_posts)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contact')
def contact():
    return render_template("contact.html")


@app.route('/<int:post_id>')
def get_post(post_id):
    requested_post = None
    for post in all_posts:
        if post['id'] == post_id:
            requested_post = post
            print(requested_post)
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
