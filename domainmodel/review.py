from domainmodel.book import Book
from datetime import datetime
class Review:
    def __init__(self, book, review_text: str, rating:int):

        if isinstance(book, Book):
            self._book = book
        else:
            self._book = None

        if isinstance(review_text, str):
            review_text = review_text.strip()
            if review_text!="":
                self._review_text = review_text
            else:
                self._review_text = "N/A"
        else:
            self._review_text = "N/A"

        time = datetime.now()
        self._timestamp = datetime.timestamp(time)

        if isinstance(rating, int) and rating>0 and rating<6:
            self._rating = rating
        else:
            raise ValueError()



    @property
    def book(self):
        return self._book
    @property
    def review_text(self):
        return self._review_text
    @property
    def rating(self):
        return self._rating
    @property
    def timestamp(self):
        return self._timestamp


    def __repr__(self):
        return "pppopo"

    def __eq__(self, other):
        if isinstance(other, Review) or self.book!=other.book or self.review_text!=other.review_text or self.rating!=other.rating or self.timestamp!=other.timestamp:
            return False
        else:
            return True
