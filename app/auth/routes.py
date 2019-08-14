from flask import render_template, request, flash, redirect, url_for
from flask_login import login_user, logout_user, current_user
from app import db
from app.auth import authentication
from app.auth.models import User, login_required
from app.auth.forms import RegistrationForm, LoginForm, ChangeUserRole
from app.character.models import Character


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
@login_required()
def log_out_user():
    logout_user()
    return redirect(url_for('main.home_page'))


@authentication.route('/user')
@login_required()
def user_list():
    if current_user.role == 'SUPER':
        users = User.query.all()
        return render_template('user_list.html', users=users)
    else:
        return redirect(url_for('authentication.user_info', user_id=current_user.id))


@authentication.route('/user/<user_id>')
@login_required()
def user_info(user_id):
    if current_user.role == 'SUPER' or current_user.id == int(user_id):
        user = User.query.get(user_id)
        characters = Character.query.filter_by(owner=user_id).all()
        return render_template('user_info.html', user=user, characters=characters)
    else:
        return render_template('no_peeking.html')


@authentication.route('/user/<user_id>/change_role', methods=['GET', 'POST'])
@login_required('SUPER')
def user_change_role(user_id):
    form = ChangeUserRole()
    user = User.query.get(user_id)
    if form.validate_on_submit():
        user.role = form.user_role.data
        flash("User Role Updated")
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('authentication.user_info', user_id=int(user.id)))

    return render_template('change_user_role.html', form=form)


@authentication.route('/nopeeking')
def no_peeking():
    return render_template('no_peeking.html')


@authentication.app_errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404
