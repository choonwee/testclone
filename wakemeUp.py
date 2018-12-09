from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        "author": "Andy Lee",
        "title":"Windy",
        "content":"first flask project1",
        "date_posted": "April 2nd 1998"
    },
    {
        "author": "Gary Winthrope",
        "title": "Great Guy Gary",
        "content": "first flask project2",
        "date_posted": "April 69nd 1969"
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)


@app.route("/destination")
def destination():
    return render_template("destination.html", title="Destination")


@app.route("/contactus")
def contactus():
    return render_template("contactus.html", title="Contact Us")


@app.route("/help")
def help():
    return render_template("help.html", title="Help")


if __name__ == "__main__":
    app.run(debug=True)
