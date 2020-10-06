from flask import Blueprint, render_template, request, url_for, Markup
import CS235Flix.browsing.services as services
import CS235Flix.memory_repository.abtractrepository as repo

browse_blueprint = Blueprint('browse_bp', __name__)

def setup_arrows(blueprint_str: str, letter_pick: str, letter_list: list):
    if letter_pick == letter_list[0]:
        left = Markup('<font> << </font>')
    else:
        left = Markup(f"<a href=\"{url_for(blueprint_str)}?letter={letter_list[letter_list.index(letter_pick) - 1]}\"> << </a>")
    if letter_pick == letter_list[-1]:
        right = Markup('<font> >> </font>')
    else:
        right = Markup(f"<a href=\"{url_for(blueprint_str)}?letter={letter_list[letter_list.index(letter_pick) + 1]}\"> >> </a>")
    return left, right

@browse_blueprint.route('/browse_by_title')
def browse_by_title():
    first_letter_pick = request.args.get('letter')
    first_letters = services.get_first_letters_of_movies(repo.repository_instance)
    if first_letter_pick is None:
        first_letter_pick = first_letters[0]
    left_link, right_link = setup_arrows('browse_bp.browse_by_title', first_letter_pick, first_letters)
    return render_template('list_movies.html', l_link=left_link, r_link=right_link, initials=first_letters, movie_list=services.get_movies_by_title(first_letter_pick, repo.repository_instance))

@browse_blueprint.route('/browse_by_genre')
def browse_by_genre():
    # genre_list = file_reader.dataset_of_genres
    return render_template('')

@browse_blueprint.route('/browse_by_director')
def browse_by_director():
    director_pick = request.args.get('director')
    first_initial_pick = request.args.get('letter')
    first_initials = services.get_first_letters_of_directors(repo.repository_instance)
    if director_pick is not None:
        first_initial_pick = director_pick[0]
    elif first_initial_pick is None:
        first_initial_pick = first_initials[0]
    left_link, right_link = setup_arrows('browse_bp.browse_by_director', first_initial_pick, first_initials)
    if director_pick is None:
        return render_template('browse_by_director.html', l_link=left_link, r_link=right_link, initials=first_initials, director_list=services.get_directors(first_initial_pick, repo.repository_instance))
    else:
        return render_template('browse_by_director.html', l_link=left_link, r_link=right_link, initials=first_initials, director_list=services.get_directors(first_initial_pick, repo.repository_instance), movie_list=services.get_movies_by_director(director_pick, repo.repository_instance))

@browse_blueprint.route('/browse_by_actor')
def browse_by_actor():
    actor_pick = request.args.get('actor')
    first_initial_pick = request.args.get('letter')
    first_initials = services.get_first_letters_of_actors(repo.repository_instance)
    if actor_pick is not None:
        first_initial_pick = actor_pick[0]
    elif first_initial_pick is None:
        first_initial_pick = first_initials[0]
    left_link, right_link = setup_arrows('browse_bp.browse_by_actor', first_initial_pick, first_initials)
    if actor_pick is None:
        return render_template('browse_by_actor.html', l_link=left_link, r_link=right_link, initials=first_initials, actor_list=services.get_actors(first_initial_pick, repo.repository_instance))
    else:
        return render_template('browse_by_actor.html', l_link=left_link, r_link=right_link, initials=first_initials, actor_list=services.get_actors(first_initial_pick, repo.repository_instance), movie_list=services.get_movies_by_actor(actor_pick, repo.repository_instance))

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
