from flask import Flask, render_template
from datetime import datetime

home_title = "Home Page"

posts = [
    {
        "author":"test1",
        "title":"Title test1",
        "content": "Content test1",
        "date_added": datetime.now()
    },
    {
        "author":"test2",
        "title":"Title test2",
        "content": "Content test2",
        "date_added": datetime.now()
    },
    {
        "author":"test3",
        "title":"Title test3",
        "content": "Content test3",
        "date_added": datetime.now()
    },
]

app = Flask(__name__)

@app.route("/home")
@app.route("/")
def fun():
    return render_template("home.html", posts=posts, title=home_title)

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)