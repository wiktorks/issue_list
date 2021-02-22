from flask import request, redirect, jsonify, request

from ..models.user import User


def configure_routes(app):


    @app.route('/users')
    def get_users():
        users = list(User.objects)
        return jsonify(users)

    @app.route('/adduser', methods=['POST'])
    def add_user():
        name, email, password, user_type = request.json.values()
        print("----------------------------", name, email, password, user_type)
        User(name=name, email=email, password=password,
             user_type=user_type).save()
        return redirect('/users')
