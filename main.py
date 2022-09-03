from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '36f7ea87c77e106ad91076720397f1b9'

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

    return render_template('home.html', posts=posts)

@app.route('/register')
def register():
    title = "Register"
    form = RegistrationForm()
    return render_template('register.html', title=title, form=form)


@app.route('/login')
def login():
    title = "Login"
    form = LoginForm()
    return render_template('login.html', title=title, form=form)


@app.route("/about")
def about():
    #about page title
    title = "About"

    return render_template("about.html", title=title)

if __name__ == "__main__":
    app.run(debug=True)