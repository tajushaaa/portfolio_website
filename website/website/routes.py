from website import app, db
from flask import render_template, flash, url_for, redirect
from .forms import RegistrationForm
from .models import User


@app.route("/")
def home_page():
    return render_template("home.html")

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('home.html'))
    return render_template('register.html', title='Register', form=form)