import pytest

from domainmodel.author import Author
from datareader.jsondatareader import BooksJSONReader
from domainmodel.publisher import Publisher
from domainmodel.book import Book
from domainmodel.bookinventory import BooksInventory

class TestPublisher:


    def testConstructor(self):
        inventory = BooksInventory()

        publisher1 = Publisher("Avatar Press")

        book1 = Book(17, "Lord of the Rings")
        book1.publisher = publisher1

        book2 = Book(64, "Our Memoires")
        book2.publisher = publisher1

        inventory.add_book(book1, 20, 7)
        inventory.add_book(book2, 30, 2)

        print(inventory.find_price(64))
        print(inventory.find_stock_count(17))
        print(inventory.find_book(99))
readlist = ReadingList()

readlist.add_book(Book(635, "Hitchhiker's Guide to the Galaxy"))
readlist.add_book(Book(273, "Harry Potter"))
readlist.add_book(Book(108, "Lord of the Rings"))
readlist = readlist(readlist)
print(next(readlist))
print(next(readlist))
print(next(readlist))

readlist = ReadingList()

readlist.add_book(Book(635, "Hitchhiker's Guide to the Galaxy"))
readlist.add_book(Book(273, "Harry Potter"))
readlist.add_book(Book(108, "Lord of the Rings"))
readlist = iter(readlist)
try:
    while True:
        print(next(readlist))
except:
    print()


"""
    def testConstructotr(self):

        author4 = Author(124, "Test")
        assert author4.unique_id == 124
        with pytest.raises(Exception):
            author1 = Author(123, "  ")
            author2 = Author(123, 123)
            author3 = Author("123", "author")
            author3 = Author("author", 123)
            author5 = Author(-1, "Test")

    def testSetter(self):
        author1 = Author(1234, "Test")
        with pytest.raises(AttributeError):
            author1.unique_id = "42"
            author1.unique_id = 42



    def testEqual(self):
        author1 = Author(3675, "Barack Obama")
        author2 = Author(3674, "Barack Obama")
        assert author1!=author2
        author3 = Author(3674, "Barack Obama")
        assert author2 == author3
        author4 = Author(3675, "Barack Obama")
        assert author2 != author4

    def testSort(self):
        author1 = Author(3675, "A")
        author2 = Author(3676, "B")
        author3 = Author(3677, "C")
        authorlist = [author1, author2, author3]
        testingList = sorted([author3, author1, author2])
        assert authorlist==testingList

    def testCoAuthor(self):
        author1= Author(3675, "A")
        author2 = Author(3676, "B")
        author3 = Author(3677, "C")
        author1.add_coauthor(author2)
        assert author1.check_if_this_author_coauthored_with(author2)==True
        assert author2.check_if_this_author_coauthored_with(author1) == True
        assert author2.check_if_this_author_coauthored_with(author3) == False
"""