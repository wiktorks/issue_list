# Creating Issues list 		
# Users can be assigned to the task		
# When a task is created, all users assigned are notified by email		
# All tasks should be stored in a JSON file	(albo libka do Cache)
# RabbitMQ/Celery-
# Znajdź bibliotekę do cacheowania do Issue List
# Docker
# All tasks should also be sent to the MongoDB database	once a day	
# The application checks (at startup or every 24h) whether the json file is consistent with the database, if not the file is updated
# db should be tasks archive


from flask import Flask

from extensions import mongo
from routes.routes import configure_routes

def create_app():
    app = Flask(__name__)
    app.secret_key = 'keyboard_cat'
    # app.config['MONGODB_SETTINGS'] = "mongodb://localhost:27017/issueList"
    app.config['MONGODB_SETTINGS'] = {
        'db': 'issueList'
    }
    mongo.init_app(app)
    configure_routes(app)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)