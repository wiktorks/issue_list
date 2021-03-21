from flask import render_template

def configure_main(app):
    @app.route('/')
    def index():
        return render_template('index.html')