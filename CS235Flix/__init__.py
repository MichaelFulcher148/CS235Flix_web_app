from flask import Flask
import CS235Flix.memory_repository.abtractrepository as repo
from CS235Flix.memory_repository.memory_repository import MemoryRepository, populate

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    repo.repository_instance = MemoryRepository()
    populate('CS235Flix\\memory_repository\\Data1000Movies.csv', repo.repository_instance)

    with app.app_context():
        from .home import home
        app.register_blueprint(home.home_blueprint)

        from .browsing import browse_by
        app.register_blueprint(browse_by.browse_blueprint)

        from .authentication import authentication
        app.register_blueprint(authentication.authentication_blueprint)

    return app
