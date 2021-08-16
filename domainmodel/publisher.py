class Publisher:

    def __init__(self, publisher_name: str):
        try:
            publisher_name= publisher_name.strip()
        except:
            self.__name = "N/A"
        else:
            if publisher_name=="":
                self.__name = "N/A"
            else:
             self.__name = publisher_name





    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, publisher_name):
        self.__name = publisher_name

    def __repr__(self):
        # we use access via the property here
        return f'<Publisher {self.name}>'

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return other.name == self.name

    def __lt__(self, other):
        return self.name<other.name

    def __hash__(self):
        return hash(self.__name)
