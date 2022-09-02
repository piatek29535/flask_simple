from flask import Flask, render_template

app = Flask(__name__)

@app.route("/home")
def home():
    #home pagge title 
    title = "Home"

    return render_template('home.html', title=title)


@app.route("/about")
def about():
    #about page title
    title = "About"

    return render_template("about.html", title=title)

if __name__ == "__main__":
    app.run(debug=True)