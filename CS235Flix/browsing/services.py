from CS235Flix.memory_repository.abtractrepository import AbstractRepository
from obj.movie import Director, Actor, Genre, Movie

def get_movies_by_date(repo: 'AbstractRepository'):
    pass

def get_first_letters_of_actors(repo: 'AbstractRepository'):
    first_letter_list = list()
    for actor in repo.get_actors():
        if actor.actor_full_name[0] not in first_letter_list:
            first_letter_list.append(actor.actor_full_name[0])
    return first_letter_list

def get_first_letters_of_movies(repo: 'AbstractRepository'):
    first_letter_list = list()
    for movie in repo.get_movies():
        if movie.title[0] == '(':
            if movie.title[1] not in first_letter_list:
                first_letter_list.append(movie.title[1])
        else:
            if movie.title[0] not in first_letter_list:
                first_letter_list.append(movie.title[0])
    return first_letter_list

def get_first_letters_of_directors(repo: 'AbstractRepository'):
    first_initial_list = list()
    for director in repo.get_directors():
        if director.director_full_name[0] not in first_initial_list:
            first_initial_list.append(director.director_full_name[0])
    return first_initial_list

def get_movies_by_director(director_name: str, repo: 'AbstractRepository') -> list:
    a_director = Director(director_name)
    movie_list = list()
    for movie in repo.get_movies():
        if a_director == movie.director:
            movie_list.append(movie)
    return movie_list

def get_movies_by_actor(actor_name: str, repo: 'AbstractRepository'):
    a_actor = Actor(actor_name)
    movie_list = list()
    for movie in repo.get_movies():
        if a_actor in movie.actors:
            movie_list.append(movie)
    return movie_list

def get_movies_by_genre(genre_name: str, repo: 'AbstractRepository'):
    a_genre = Genre(genre_name)
    movie_list = list()
    for movie in repo.get_movies():
        if a_genre in movie.genres:
            movie_list.append(movie)
    return movie_list

def get_movies_by_title(search_letter: str, repo: 'AbstractRepository') -> list:
    movie_list = list()
    for movie in repo.get_movies():
        if movie.title[0] == '(':
            if movie.title[1] == search_letter:
                movie_list.append(movie)
        else:
            if movie.title[0] == search_letter:
                movie_list.append(movie)
    return movie_list

def get_directors(search_letter: str, repo: 'AbstractRepository') -> list:
    director_list = list()
    for director in repo.get_directors():
        if director.director_full_name[0] == search_letter:
            director_list.append(director)
    return director_list

def get_actors(search_letter: str, repo: 'AbstractRepository'):
    actor_list = list()
    for actor in repo.get_actors():
        if actor.actor_full_name[0] == search_letter:
            actor_list.append(actor)
    return actor_list

def get_genres(repo: 'AbstractRepository'):
    return repo.get_genres()

def get_movie_info(movie_name: str, date: int, repo: 'AbstractRepository') -> dict:
    a_movie = Movie(movie_name, date)
    selected_movie = None
    for movie in repo.get_movies():
        if a_movie == movie:
            selected_movie = movie
            break
    if selected_movie is None:
        return None
    else:
        return {'title': selected_movie.title,
                'release_year': selected_movie.release_year,
                'description': selected_movie.description,
                'director': selected_movie.director.director_full_name,
                'actors': selected_movie.actors,
                'genres': selected_movie.genres,
                'runtime': selected_movie.runtime_minutes}
