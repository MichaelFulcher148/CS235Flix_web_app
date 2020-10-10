from CS235Flix.memory_repository.abtractrepository import AbstractRepository
from obj.movie import Review, Movie

def add_review(movie_title: str, movie_release_date: int, review_text: str, rating_num: int, repo: 'AbstractRepository'):
    a_movie = Movie(movie_title, movie_release_date)
    repo.add_review(Review(a_movie, review_text, rating_num))

def get_reviews(title: str, date: int, repo: 'AbstractRepository'):
    reviews = repo.get_reviews(Movie(title, date))
    if reviews is None:
        return None
    else:
        reviews_data = list()
        for review in reviews:
            a_review = dict()
            a_review['text'] = review.review_text
            a_review['rating'] = review.rating
            a_review['date'] = review.timestamp.strftime('%d-%m-%Y %H:%M:%S')
            reviews_data.append(a_review)
        reviews_data.reverse()
        return reviews_data

def check_movie_exists(title: str, date: int, repo: 'AbstractRepository') -> bool:
    a_movie = Movie(title, date)
    for movie in repo.get_movies():
        if movie == a_movie:
            return True
    return False
