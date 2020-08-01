from flask import Flask, send_file

app = Flask(__name__, template_folder="templates", static_folder="static", static_url_path="")


@app.route("/")
@app.route("/index.html")
@app.route("/index")
def index():
    return send_file("templates/index.html")


@app.route("/login.html")
@app.route("/login")
def login():
    return send_file("templates/login.html")


@app.route("/register.html")
@app.route("/register")
def register():
    return send_file("templates/register.html")


@app.route("/404.html")
@app.route("/404")
def html_404():
    return send_file("templates/404.html")


@app.route("/blog.html")
@app.route("/blog")
def blog():
    return send_file("templates/blog.html")


@app.route("/blog_single.html")
@app.route("/blog_single")
def blog_single():
    return send_file("templates/blog_single.html")


@app.route("/contact.html")
@app.route("/contact")
def contact():
    return send_file("templates/contact.html")


@app.route("/men.html")
@app.route("/men")
def men():
    return send_file("templates/men.html")


@app.route("/single.html")
@app.route("/single")
def single():
    return send_file("templates/single.html")


@app.route("/wishlist.html")
@app.route("/wishlist")
def wishlist():
    return send_file("templates/wishlist.html")


if __name__ == '__main__':
    app.run(debug=True, port=8888)
