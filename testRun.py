from flask import Flask, render_template, flash, url_for, redirect, request

app = Flask(__name__)


@app.route("/test")
def test():
    return render_template("test.html")


if __name__ == "__main__":
    app.run(port="80")


