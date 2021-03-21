from flask import redirect, request, render_template, flash
from flask.helpers import url_for
from flask_login import login_user, current_user, logout_user

from ..utils.forms import LoginForm, RegisterForm
from ..models.models import User
from ..extensions import bcrypt, login_manager
# cykl życia aplikacji: dev -> staging(stawia się aplikację w warunkach jak najbardziej zbliżonych do produkcji) -> prod


def configure_login(app):
    @login_manager.user_loader
    def load_user(user_id):
        return User.objects(pk=user_id).first()

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if current_user.is_authenticated:
            return redirect(url_for('index'))
        form = LoginForm()
        if form.validate_on_submit():
            user = User.objects(name=form.username.data).first()
            if user and bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                next_page = request.args.get('next')
                return redirect(next_page) if next_page else redirect(url_for('index'))
            else:
                flash(
                    'Invalid username or password. Please try again or register.', category='danger')
        return render_template('login.html', form=form)

    @app.route('/register', methods=['GET', 'POST'])
    def register():
        if current_user.is_authenticated:
            return redirect(url_for('index'))

        form = RegisterForm()
        if form.validate_on_submit():
            password = bcrypt.generate_password_hash(form.data['password'])
            name, email, user_type = form.data['username'], form.data['user_email'], 'local'
            new_user = User(name=name, email=email,
                            password=password, user_type=user_type)
            new_user.save()
            flash(
                message=f'Your account {form.username.data} has been created. You may now sign in.', category='success')
            return redirect(url_for('login'))

        return render_template('register.html', form=form)

    @app.route('/logout')
    def logout():
        logout_user()
        return redirect(url_for('index'))
