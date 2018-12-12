from flask import Flask, render_template, flash, url_for, redirect, request
from destinationForm import DestinationForm, BusRoutes
from forms import ContactForm


app = Flask(__name__)

app.secret_key = 'development key'
app.config['SECRET_KEY'] = '4f6c484fa2d098ccb271bf1f07173423'

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/contactus", methods=["GET", "POST"])
def contactus():
    form = FeedbackForm()
    if form.validate_on_submit():
        flash(f'You are in transit, on Bus {form.busNumber.data}!', 'danger')
        return redirect("transit")
    return render_template("contactus.html", title="Contact Us", form=form)


@app.route("/login")
def login():
    pass


@app.route("/help")
def help():
    return render_template("help.html", title="Help")


@app.route("/destination", methods=['GET', 'POST'])
def destination():
    form = DestinationForm()
    if form.validate_on_submit():
        flash(f'You are in transit, on Bus {form.busNumber.data}!', 'danger')
        return redirect("transit")
    return render_template("destinationForm.html", title="Destination", form=form)


@app.route("/transit")
def transit():
    return render_template("inTransitpage.html", title="Transit")


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()

    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required.')
            return render_template('contact.html', form=form)
        else:
            return 'Form posted.'

    elif request.method == 'GET':
        return render_template('contact.html', form=form)


@app.route('/busroutes', methods=['GET', 'POST'])
def busroutes():
    form = BusRoutes()
    if form.validate_on_submit():
        flash(f'{form.comment.data}!')
    return render_template("busroutes.html", title="Bus Routes", form=form)


if __name__ == "__main__":
    app.run(debug=True)
