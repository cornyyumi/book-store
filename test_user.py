import pytest
from domainmodel.user import User
from domainmodel.author import Author
from datareader.jsondatareader import BooksJSONReader
from domainmodel.publisher import Publisher
from domainmodel.book import Book
class TestPublisher:


    def testConstructor(self):
        user1 = User('Shyamli', 'pw12345')
        user2 = User('    ', 'p890')
        user3 = User('Daniel', 'pw87465')
        assert user1.user_name == "shyamli"
        assert user1.password == "pw12345"
        assert user2.user_name == None
        assert user2.password == None

        books = [Book(874658, "Harry Potter"), Book(89576, "Lord of the Rings")]
        books[0].num_pages = 107
        books[1].num_pages = 121
        user = User("Martin", "pw12345")
        print(user.read_books)
        print(user.pages_read)
        for book in books:
            user.read_a_book(book)
        print(user.read_books)
        print(user.pages_read)