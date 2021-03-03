from flask import request, redirect, jsonify, request, render_template, flash
from flask.helpers import url_for
from flask_login import login_user, current_user, logout_user

from ..utils.forms import LoginForm, RegisterForm
from ..models.user import User
from ..extensions import bcrypt, login_manager

def configure_routes(app):
    @login_manager.user_loader
    def load_user(user_id):
        # print(User.objects(pk=user_id).first().name)
        return User.objects(pk=user_id).first()

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        # print(current_user.is_authenticated)
        if current_user.is_authenticated:
            print('hurra!')
            return redirect(url_for('index'))

        form = LoginForm()
        if form.validate_on_submit():
            user = User.objects(name=form.username.data).first()
            if user and bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                return redirect(url_for('index'))
            else:
                flash('Invalid username or password. Please try again or register.', 'danger')
        return render_template('login.html', form=form)

    @app.route('/register', methods=['GET', 'POST'])
    def register():
        if current_user.is_authenticated:
            return redirect(url_for('index'))

        form = RegisterForm()
        if form.validate_on_submit():
            # try:
            password = bcrypt.generate_password_hash(form.data['password'])
            name, email, user_type = form.data['username'], form.data['user_email'], 'local'
            new_user = User(name=name, email=email, password=password, user_type=user_type)
            new_user.save()
            flash(message=f'Your account {form.username.data} has been created. You may now sign in.', category='success')
            return redirect(url_for('login'))
            # except NotUniqueError:
            #     print(NotUniqueError.args.)
            #     flash(message=f'An error occured on the server side.', category='danger')

        return render_template('register.html', form=form)
    @app.route('/logout')
    def logout():
        logout_user()
        return redirect(url_for('index'))
    #     users = list(User.objects)
    #     return jsonify(users)

    # @app.route('/users')
    # def get_users():
    #     users = list(User.objects)
    #     return jsonify(users)

    # @app.route('/adduser', methods=['POST'])
    # def add_user():
    #     name, email, password, user_type = request.json.values()
    #     User(name=name, email=email, password=password,
    #          user_type=user_type).save()
    #     return redirect('/users')
