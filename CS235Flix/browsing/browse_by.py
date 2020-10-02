from flask import Blueprint, render_template, request
from obj.movie import Director
import CS235Flix.memory_repository.abtractrepository as repo

browse_blueprint = Blueprint('browse_bp', __name__)

@browse_blueprint.route('/browse_by_title')
def browse_by_title():
    return render_template('list_movies.html', movie_list=repo.repository_instance.get_movies())

@browse_blueprint.route('/browse_by_genre')
def browse_by_genre():
    genre_list = file_reader.dataset_of_genres
    return render_template('')

@browse_blueprint.route('/browse_by_director')
def browse_by_director():
    director_pick = request.args.get('director')
    if director_pick is None:
        return render_template('browse_by_director.html', genre_list=repo.repository_instance.get_directors())
    else:
        a_director = Director(director_pick)
        movie_list = list()
        for movie in repo.repository_instance.get_movies():
            if a_director == movie.director:
                movie_list.append(movie)
        return render_template('browse_by_director.html', genre_list=repo.repository_instance.get_directors(), movie_list=movie_list)

@browse_blueprint.route('/browse_by_actor')
def browse_by_actor():
    return 'Hello, World!'