from flask import Flask, render_template
from file_reader.file_reader import MovieFileCSVReader

def create_app():
    app = Flask(__name__)
    file_reader = MovieFileCSVReader('Data1000Movies.csv')
    file_reader.read_csv_file()

    @app.route('/')
    def index():
        return render_template('home.html')

    @app.route('/browse_by_title')
    def hello():
        movie_list = file_reader.dataset_of_movies
        movie_list.sort()
        return render_template('list_movies.html', movie_list=movie_list)

    @app.route('/browse_by_genre')
    def hello():
        genre_list = file_reader.dataset_of_genres
        genre_list.sort()
        return render_template('')

    @app.route('/browse_by_director')
    def hello():
        return 'Hello, World!'

    @app.route('/browse_by_actor')
    def hello():
        return 'Hello, World!'

    return app
