from domainmodel.book import Book
from domainmodel.review import Review
class User:
    def __init__(self, user_name:str, password:str):
        self._read_books = []
        self._reviews = []
        self.pages_read =0


        if isinstance(user_name, str):
            user_name = user_name.strip()
            if user_name !="":
                self._user_name = user_name.lower()
            else:
                self._user_name = None
        else:
            self._user_name = None

        if isinstance(password, str):
            password = password.strip()
            if password !="" and len(password)>=7:
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
            self.pages_read+=book.num_pages

    def add_review(self, review):
        if isinstance(review, Review) and review not in self._reviews:
            self._reviews.append(review)

