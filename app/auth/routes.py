from flask import render_template, request, flash, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user
from app.auth.forms import RegistrationForm, LoginForm
from app.auth import authentication
from app.auth.models import User


@authentication.route('/register', methods=['GET', 'POST'])
def register_user():
    if current_user.is_authenticated:
        flash('you are already logged in')
        return redirect(url_for('main.home_page'))
    form = RegistrationForm()
    if form.validate_on_submit():
        User.create_user(
            user=form.username.data,
            password=form.password.data
        )
        flash('Registration Successful')
        return redirect(url_for('authentication.do_the_login'))
    return render_template('registration.html', form=form)


@authentication.route('/login', methods=['GET', 'POST'])
def do_the_login():
    if current_user.is_authenticated:
        flash('you are already logged in')
        return redirect(url_for('main.home_page'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(user_name=form.username.data).first()
        if not user or not user.check_password(form.password.data):
            flash('Invalid Credentials, Please try again')
            return redirect(url_for('authentication.do_the_login'))

        login_user(user, form.stay_logged_in.data)
        return redirect(url_for('main.home_page'))

    return render_template('login.html', form=form)


@authentication.route('/logout')
@login_required
def log_out_user():
    logout_user()
    return redirect(url_for('main.home_page'))


@authentication.app_errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404
