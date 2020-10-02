from .abtractrepository import AbstractRepository

class MemoryRepository(AbstractRepository):
    def __init__(self) -> None:
        self.__movies = list()
        self.__genres = list()
        self.__actors = list()
        self.__directors = list()

    def get_genres(self):
        return self.__genres

    def get_movies(self):
        return self.__movies

    def get_actors(self):
        return self.__actors

    def get_directors(self):
        return self.__directors

    def add_movie(self, a_movie: 'Movie'):
        self.__movies.append(a_movie)

    def add_genre(self, a_genre: 'Genre'):
        self.__genres.append(a_genre)

    def add_actor(self, a_actor: 'Actor'):
        self.__actors.append(a_actor)

    def add_director(self, a_director: 'Director'):
        self.__directors.append(a_director)

    def tidy_up(self):
        self.__movies.sort()
        self.__directors.sort()
        self.__actors.sort()
        self.__genres.sort()
