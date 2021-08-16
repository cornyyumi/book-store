from domainmodel.book import Book
class BooksInventory:
    def __init__(self):
        self.books_collection = []

    def add_book(self, book, price, nr_books_in_stock):
        if isinstance(price, int):
            price = float(price)
        else:
            raise ValueError()
        if isinstance(book, Book) and isinstance(price, float) and price>=0 and isinstance(nr_books_in_stock, int) and nr_books_in_stock>=0:
            for book_data in self.books_collection:
                if book_data["book"] == book:
                    book_data["book"] = book
                    book_data["price"] = price
                    book_data["nr_books_in_stock"] = nr_books_in_stock
                    return
            new_book_data = {"book": book, "price": price, "nr_books_in_stock": nr_books_in_stock}
            self.books_collection.append(new_book_data)


        else:
            raise ValueError()

    def remove_book(self, book_id):
        if isinstance(book_id, int) and book_id >= 0:
            for book in self.books_collection:
                if (book["book"].book_id) == book_id:
                    self.books_collection.remove(book)

    def find_book(self, book_id):
        if isinstance(book_id, int) and book_id>=0:
            for book in self.books_collection:
                if (book["book"].book_id) == book_id:
                    return book["book"]
        return None

    def find_price(self, book_id):
        if isinstance(book_id, int) and book_id >= 0:
            for book in self.books_collection:
                if (book["book"].book_id) == book_id:
                    return int(book["price"])
        return None


    def find_stock_count(self, book_id):
        if isinstance(book_id, int) and book_id >= 0:
            for book in self.books_collection:
                if (book["book"].book_id) == book_id:
                    return book["nr_books_in_stock"]
        return None

    def search_book_by_title(self, title):
        if isinstance(title, str):
            title = title.strip()
            if title !="":
                for book in self.books_collection:
                    if (book["book"].title) == title:
                        return book["book"]
        return None


class User:
    def __init__(self, user_name :str, password :str):
        self._read_books = []
        self._reviews = []
        self.pages_read =0

        if isinstance(user_name, str):
            user_name = user_name.strip()
            if user_name != "":
                self._user_name = user_name.lower()
            else:
                self._user_name = None
        else:
            self._user_name = None

        if isinstance(password, str):
            password = password.strip()
            if password != "" and len(password) >= 7:
                self._password = password
            else:
                self._password = None
        else:
            self._password = None

    @property
    def user_name(self):
        return self._user_name

    @property
    def password(self):
        return self._password

    @property
    def read_books(self):
        return self._read_books

    @property
    def reviews(self):
        return self._reviews

    def __repr__(self):
        return f"<User {self.user_name}>"

    def __eq__(self, other):
        if isinstance(other, User):
            return self._user_name == other.user_name
        else:
            return False

    def __lt__(self, other):
        if isinstance(other, User):
            return self._user_name < other.user_name

    def __hash__(self):
        return hash(self.user_name)

    def read_a_book(self, book):
        if isinstance(book, Book) and book not in self._read_books:
            self._read_books.append(book)
            self.pages_read += book.num_pages

    def add_review(self, review):
        if isinstance(review, Review) and review not in self._reviews:
            self._reviews.append(review)
