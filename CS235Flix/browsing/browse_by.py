from flask import Blueprint, render_template, request
from obj.movie import Director
from file_reader.file_reader import MovieFileCSVReader
file_reader = MovieFileCSVReader('Data1000Movies.csv')
file_reader.read_csv_file()

browse_blueprint = Blueprint('brose_bp', __name__)

@browse_blueprint.route('/browse_by_title')
def browse_by_title():
    movie_list = file_reader.dataset_of_movies
    movie_list.sort()
    return render_template('list_movies.html', movie_list=movie_list)

@browse_blueprint.route('/browse_by_genre')
def browse_by_genre():
    genre_list = file_reader.dataset_of_genres
    return render_template('')

@browse_blueprint.route('/browse_by_director')
def browse_by_director():
    director_pick = request.args.get('director')
    director_list = list()
    for i in file_reader.dataset_of_directors:
        director_list.append(i)
    if director_pick is None:
        return render_template('browse_by_director.html', genre_list=director_list)
    else:
        a_director = Director(director_pick)
        movie_list = list()
        for movie in file_reader.dataset_of_movies:
            if a_director == movie.director:
                movie_list.append(movie)
        return render_template('browse_by_director.html', genre_list=director_list, movie_list=movie_list)

@browse_blueprint.route('/browse_by_actor')
def browse_by_actor():
    return 'Hello, World!'