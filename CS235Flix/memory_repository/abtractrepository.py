import abc

class AbstractRepository(abc.ABC):
    @abc.abstractmethod
    def get_genres(self):
        raise NotImplementedError

    @abc.abstractmethod
    def get_movies(self):
        raise NotImplementedError

    @abc.abstractmethod
    def get_actors(self):
        raise NotImplementedError

    @abc.abstractmethod
    def get_directors(self):
        raise NotImplementedError