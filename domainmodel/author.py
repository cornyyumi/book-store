class Author:
    def __init__(self, author_id: int, author_full_name: str):
        self.full_name  = author_full_name
        if author_id<0 or not isinstance(author_id, int):
            raise ValueError()
        self._unique_id = author_id
        self.coAuthorList = []

    @property
    def unique_id(self):
        return self._unique_id
    @property
    def full_name(self)-> str:
        return self._full_name

    @full_name.setter
    def full_name(self, author_full_name):
        if not isinstance(author_full_name, str):
            raise ValueError()
        else:
            author_full_name = author_full_name.strip()
        if author_full_name == "":
            raise ValueError()
        self._full_name = author_full_name


    def __repr__(self):
        return f'<Author {self.full_name}, author id = {self.unique_id}>'
    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return other.unique_id  == self.unique_id

    def __lt__(self, other):
        if isinstance(other, self.__class__):
            return self.unique_id <other.unique_id

    def __hash__(self):
        return hash(self.unique_id)

    def add_coauthor(self, coauthor):
        if isinstance(coauthor, self.__class__) and coauthor not in self.coAuthorList:
            self.coAuthorList.append(coauthor)
            coauthor.coAuthorList.append(self)

    def check_if_this_author_coauthored_with(self, author):
        for person in self.coAuthorList:
            if person==author:
                return True
        return False