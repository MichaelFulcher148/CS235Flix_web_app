import pytest
import CS235Flix.memory_repository.abtractrepository as repo
from CS235Flix.memory_repository.memory_repository import MemoryRepository, populate
from file_reader.file_reader import MovieFileCSVReader

@pytest.fixture
def a_memory_repo():
    repo.repository_instance = MemoryRepository()
    populate('CS235Flix\\memory_repository\\Data1000Movies.csv', repo.repository_instance)
    return repo.repository_instance

@pytest.fixture
def a_file_reader():
    reader = MovieFileCSVReader('CS235Flix\\memory_repository\\Data1000Movies.csv')
    reader.read_csv_file()
    return reader
