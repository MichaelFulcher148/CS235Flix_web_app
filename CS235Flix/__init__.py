from flask import Flask
from file_reader.file_reader import MovieFileCSVReader
import CS235Flix.memory_repository.abtractrepository as repo
from CS235Flix.memory_repository.memory_repository import MemoryRepository

def create_app():
    app = Flask(__name__)

    file_reader = MovieFileCSVReader('Data1000Movies.csv')
    file_reader.read_csv_file()

    repo.repository_instance = MemoryRepository()
    for movie in file_reader.dataset_of_movies:
        repo.repository_instance.add_movie(movie)
    for director in file_reader.dataset_of_directors:
        repo.repository_instance.add_director(director)
    for actor in file_reader.dataset_of_actors:
        repo.repository_instance.add_actor(actor)
    for genre in file_reader.dataset_of_genres:
        repo.repository_instance.add_genre(genre)
    repo.repository_instance.tidy_up()
    del file_reader

    with app.app_context():
        from .home import home
        app.register_blueprint(home.home_blueprint)

        from .browsing import browse_by
        app.register_blueprint(browse_by.browse_blueprint)

    return app
