from flask import request, redirect, jsonify, request, render_template

from ..models.user import User


def configure_routes(app):
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            username = request.form['login']
            password = request.form['password']

            user_object = User.objects(name=username)[0]
            user_object = user_object if user_object else User.objects(email=username)[0]
            print(user_object)
            return ''
        else:
            return 'kek'


    @app.route('/users')
    def get_users():
        users = list(User.objects)
        return jsonify(users)

    @app.route('/adduser', methods=['POST'])
    def add_user():
        name, email, password, user_type = request.json.values()
        User(name=name, email=email, password=password,
             user_type=user_type).save()
        return redirect('/users')
