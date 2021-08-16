import pytest


from domainmodel.publisher import Publisher
from domainmodel.author import Author
from domainmodel.book import Book


class TestBook:
    def testConstructor(self):
        book1 = Book(1234, "Testing")
        assert str(book1)=="<Book Testing, book id = 1234>"
        with pytest.raises(Exception):
            book1 = Book(1234, 1234)
            book1 = Book(1234, "    ")
            book1 = Book("1234", "Testing")
            book1 = Book(-1, "Testing")
            assert book1.description==None

    def testSetter(self):
        book1 = Book(1234, "Testing")
        publisher1 = Publisher("test")
        book1.publisher = publisher1
        assert str(book1.publisher)== str(publisher1)
        book1.publisher = 1234
        assert book1.publisher == publisher1
        book1.publisher = "asdad"
        assert book1.publisher == publisher1
        book1.publisher = "     "
        assert book1.publisher == publisher1



    def testSort(self):
        book1 = Book(1234, "A")
        book2 = Book(1235, "B")
        book3 = Book(1236, "C")
        list1 = [book1, book2, book3]
        list2 = [book3, book1, book2]
        assert list1==sorted(list2)

    def testEqual(self):
        book1 = Book(1234, "A")
        book2 = Book(1234, "B")
        book3 = Book(1235, "A")
        assert book1==book2
        assert  book1!=book3

    def testAddRemoveAuthor(self):
        book1 = Book(1234, "A")
        book2 = Book(1235, "B")
        book3 = Book(1236, "C")

        author1 = Author(1, "author1")
        author2 = Author(2, "author2")
        book1.add_author(author1)
        assert book1.authors == [author1]
        book2.add_author(author1)
        book2.add_author(author1)
        assert book2.authors == [author1]

        book1.add_author(author2)
        assert book1.authors == [author1, author2]

        book1.remove_author(author1)
        assert book1.authors == [author2]
        book1.remove_author(author1)
        book1.remove_author(author2)
        assert book1.authors == []









