from domainmodel.publisher import Publisher
from domainmodel.author import Author


class Book:
    def __init__(self, new_book_id:int, new_title:str):
        self.authors = []
        self.title = new_title
        self._release_year = None
        if new_book_id<0 or not isinstance(new_book_id, int):
            raise ValueError()
        self._book_id = new_book_id


    @property
    def book_id(self):
        return self._book_id

    @property
    def title(self):
        return self._title
    @title.setter
    def title(self, new_title):
        if not isinstance(new_title, str):
            raise ValueError()
        else:
            new_title = new_title.strip()
        if new_title == "":
            raise ValueError()
        self._title = new_title

    @property
    def description(self):
        return self._description
    @description.setter
    def description(self, new_description):
        if isinstance(new_description, str):
            new_description = new_description.strip()
        if new_description!="":
            self._description = new_description

    @property
    def publisher(self):
        return self._publisher
    @publisher.setter
    def publisher(self, new_publisher):
        if isinstance(new_publisher, Publisher):
            self._publisher = new_publisher


    @property
    def release_year(self):
        return self._release_year
    @release_year.setter
    def release_year(self, new_release_year):
        if isinstance(new_release_year, int) and new_release_year>0:
            self._release_year = new_release_year
        else:
            raise ValueError()

    @property
    def ebook(self):
        return self._ebook
    @ebook.setter
    def ebook(self, new_ebook):
        if isinstance(new_ebook, bool):
            self._ebook=new_ebook

    @property
    def num_pages(self):
        return self._num_pages
    @num_pages.setter
    def num_pages(self, book_pages):
        if book_pages>0 or isinstance(new_book_id, int):
            self._num_pages = book_pages



    def __repr__(self):
        return f'<Book {self.title}, book id = {self.book_id}>'

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self.book_id == other.book_id

    def __lt__(self, other):
        if isinstance(other, self.__class__):
            return self.book_id<other.book_id

    def __hash__(self):
        return hash(self.book_id)

    def add_author(self, new_author):
        if isinstance(new_author, Author) and new_author not in self.authors:
            self.authors.append(new_author)
    def remove_author(self, author):
        if isinstance(author, Author) and author in self.authors:
            self.authors.remove(author)

