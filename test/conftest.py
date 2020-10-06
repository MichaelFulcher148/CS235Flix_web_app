import pytest
import CS235Flix.memory_repository.abtractrepository as repo
from CS235Flix.memory_repository.memory_repository import MemoryRepository, populate


@pytest.fixture
def a_memory_repo():
    repo.repository_instance = MemoryRepository()
    populate('CS235Flix\\memory_repository\\Data1000Movies.csv', repo.repository_instance)
    return repo.repository_instance
