from flask import Flask, render_template
from file_reader.file_reader import MovieFileCSVReader

def create_app():
    app = Flask(__name__)
    file_reader = MovieFileCSVReader('Data1000Movies.csv')
    file_reader.read_csv_file()

    @app.route('/')
    def index():
        movie_list = file_reader.dataset_of_movies
        movie_list.sort()
        return render_template('list_movies.html', movie_list=movie_list)

    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    @app.route('/post/<int:post_id>')
    def show_post(post_id):
        # Show the post with the given id, the id is an integer
        return 'Post %d' % post_id

    @app.route('/news', methods=['GET'])
    def shows_news():
        return "Today’s news is ..."

    return app
