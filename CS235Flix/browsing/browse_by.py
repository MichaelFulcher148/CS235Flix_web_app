from flask import Blueprint, render_template, request
import CS235Flix.browsing.services as services
import CS235Flix.memory_repository.abtractrepository as repo

browse_blueprint = Blueprint('browse_bp', __name__)

@browse_blueprint.route('/browse_by_title')
def browse_by_title():
    return render_template('list_movies.html', movie_list=services.get_movies_by_title(repo.repository_instance))

@browse_blueprint.route('/browse_by_genre')
def browse_by_genre():
    # genre_list = file_reader.dataset_of_genres
    return render_template('')

@browse_blueprint.route('/browse_by_director')
def browse_by_director():
    director_pick = request.args.get('director')
    if director_pick is None:
        return render_template('browse_by_director.html', genre_list=services.get_directors(repo.repository_instance))
    else:
        return render_template('browse_by_director.html', genre_list=services.get_directors(repo.repository_instance), movie_list=services.get_movies_by_director(director_pick, repo.repository_instance))

@browse_blueprint.route('/browse_by_actor')
def browse_by_actor():
    return 'Hello, World!'

@browse_blueprint.route('/movie_info')
def view_movie_info():
    movie_name = request.args.get('movie_name')
    movie_date = request.args.get('date')
    if movie_name is None or movie_date is None:
        return render_template('view_movie.html')
    else:
        movie_date = int(movie_date)
        data = services.get_movie_info(movie_name, movie_date, repo.repository_instance)
        if data is None:
            return render_template('view_movie.html')
        else:
            return render_template('view_movie.html', movie_data=data)