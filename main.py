from flask import Flask, render_template, request
import requests
import smtplib

app = Flask(__name__)
all_posts = []


@app.route('/')
def home():
    global all_posts
    response = requests.get("https://api.npoint.io/e42b353ee387383898c7")
    all_posts = response.json()
    print(all_posts)
    return render_template("index.html", posts=all_posts)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/<int:post_id>')
def get_post(post_id):
    requested_post = None
    for post in all_posts:
        if post['id'] == post_id:
            requested_post = post
            print(requested_post)
    return render_template("post.html", post=requested_post)


@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == "POST":
        if request.form['name'] and request.form['email'] and request.form['phone'] and request.form['message']:
            event=f"Name: {request.form['name']}\nEmail: {request.form['email']}\nMessage: {request.form['message']}"
            send_email(event)
            return render_template("contact.html", message_sent=f"Hey now, {request.form['name']}")
    return render_template("contact.html", message_sent=False)


def send_email(event):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user="", password="")
        connection.sendmail(
            from_addr="",
            to_addrs="",
            msg=f"Subject: Contact Form Message\n\n{event}"
            )


if __name__ == "__main__":
    app.run(debug=True)
