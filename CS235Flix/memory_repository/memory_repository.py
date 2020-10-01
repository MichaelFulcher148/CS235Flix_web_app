from .abtractrepository import AbstractRepository

class MemoryRepository(AbstractRepository):
    def __init__(self, movies: list, genres: set, actors: set, directors: set) -> None:
        self.__movies = movies
        self.__genres = list(genres)
        self.__actors = list(actors)
        self.__directors = list(directors)

    def get_genres(self):
        return self.__genres

    def get_movies(self):
        return self.__movies

    def get_actors(self):
        return self.__actors

    def get_directors(self):
        return self.__directors
