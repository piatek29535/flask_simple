from flask import Flask, render_template

app = Flask(__name__)


posts = [
    {
        "title":"Title",
        "desc":"Post 1 Post 1",
        "tag":"Post 1"
    },
    {
        "title":"Title",
        "desc":"Post 2 Post 2",
        "tag":"Post 2"
    },{
        "title":"Title",
        "desc":"Post 3 Post 3",
        "tag":"Post 3"
    },
]

@app.route('/')
@app.route("/home")
def home():
    #home pagge title 
    title = "Home"

    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    #about page title
    title = "About"

    return render_template("about.html", title=title)

if __name__ == "__main__":
    app.run(debug=True)