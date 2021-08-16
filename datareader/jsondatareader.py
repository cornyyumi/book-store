import json
from domainmodel.publisher import Publisher
from domainmodel.author import Author
from domainmodel.book import Book

class BooksJSONReader:

    def __init__(self, books_file_name: str, authors_file_name: str):
        self.__dataset_of_books = []
        self.__dataset_of_authors = []

        try:
            books_file_name = books_file_name.strip()
            authors_file_name = authors_file_name.strip()
        except:
            raise ValueError()
        if books_file_name=="" or authors_file_name=="":
            raise ValueError()


        self.books_filename = books_file_name
        self.authors_filename = authors_file_name

    @property
    def dataset_of_books(self) -> list:
        return self.__dataset_of_books
    @dataset_of_books.setter
    def dataset_of_books(self, new_book) -> list:
        if isinstance(new_book, Book):
            self.__dataset_of_books.append(new_book)



    def read_json_files(self):

        try:
            f1= open("data/" + self.books_filename, 'r')
            f2 = open("data/" + self.authors_filename, 'r')
            data_books = f1.readlines()
            data_authors = f2.readlines()
            f1.close()
            f2.close()
        except FileNotFoundError:
            raise ValueError()


        for i in data_authors:
            data_authors = json.loads(i)
            author = Author(int(data_authors["author_id"]), data_authors["name"])
            self.__dataset_of_authors.append(author)

        for i in data_books:
            book_files = json.loads(i)
            book= Book(int(book_files["book_id"]), book_files["title"])
            self.__dataset_of_books.append(book)
            book.publisher = Publisher(book_files["publisher"])
            book.description = book_files["description"]
            book.num_pages = (book_files["num_pages"])

            book.ebook = bool(book_files["is_ebook"])

            for authors in book_files["authors"]:
                for author in self.__dataset_of_authors:
                    if int(authors["author_id"]) ==author.unique_id:
                        book.add_author(author)

            try:
                book_files["publication_year"] = int(book_files["publication_year"])
            except:
                continue
            else:
                book.release_year = book_files["publication_year"]











