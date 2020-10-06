import pytest

import CS235Flix.browsing.services
from obj.movie import Director, Genre, Actor

def test_browse_by_get_movie_info(a_memory_repo):
    movie_info = CS235Flix.browsing.services.get_movie_info("Split", 2016, a_memory_repo)
    assert movie_info == {'title': "Split",
                'release_year': 2016,
                'description': "Three girls are kidnapped by a man with a diagnosed 23 distinct personalities. They must try to escape before the apparent emergence of a frightful new 24th.",
                'director': "M. Night Shyamalan",
                'actors': [Actor("James McAvoy"), Actor("Anya Taylor-Joy"), Actor("Haley Lu Richardson"), Actor("Jessica Sula")],
                'genres': [Genre("Horror"), Genre("Thriller")],
                'runtime': 117}

def test_browse_by_get_non_existant_movie_info(a_memory_repo):
    assert CS235Flix.browsing.services.get_movie_info("Nope", 2016, a_memory_repo) == None
