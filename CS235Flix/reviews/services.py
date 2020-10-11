from CS235Flix.memory_repository.abtractrepository import AbstractRepository
from obj.movie import Review, Movie

def add_review(user_name: str, movie_title: str, movie_release_date: int, review_text: str, rating_num: int, repo: 'AbstractRepository'):
    a_movie = Movie(movie_title, movie_release_date)
    a_user = repo.find_user(user_name)
    a_user.add_review(Review(a_movie, review_text, rating_num))

def get_reviews(title: str, date: int, repo: 'AbstractRepository'):
    reviews_data = list()
    for user in repo.get_users():
        for review in user.reviews:
            if review.movie.title == title and review.movie.release_year == date:
                a_review = dict()
                a_review['text'] = review.review_text
                a_review['rating'] = review.rating
                a_review['date'] = review.timestamp.strftime('%d-%m-%Y %H:%M:%S')
                a_review['author'] = user.username
                reviews_data.append(a_review)
                break
    if len(reviews_data) > 0:
        reviews_data.reverse()
        return reviews_data
    else:
        return None

def check_movie_exists(title: str, date: int, repo: 'AbstractRepository') -> bool:
    a_movie = Movie(title, date)
    for movie in repo.get_movies():
        if movie == a_movie:
            return True
    return False
