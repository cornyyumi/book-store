import pytest

from domainmodel.author import Author
from datareader.jsondatareader import BooksJSONReader
from domainmodel.publisher import Publisher
from domainmodel.review import Review
from domainmodel.book import Book


class TestPublisher:
    def testConstructor(self):
        book = Book(2675376, "Harry Potter")
        review_text = "  This book was very enjoyable.   "
        rating = 4
        review = Review(book, review_text, rating)
