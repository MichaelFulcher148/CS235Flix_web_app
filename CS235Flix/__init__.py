from flask import Flask
from file_reader.file_reader import MovieFileCSVReader

def create_app():
    app = Flask(__name__)
    #memory repository?

    with app.app_context():
        from .home import home
        app.register_blueprint(home.home_blueprint)

        from .browsing import browse_by
        app.register_blueprint(browse_by.browse_blueprint)

    return app
