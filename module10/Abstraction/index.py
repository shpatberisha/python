from abc import ABC,abstractmethod

class Printable(ABC):

    @abstractmethod
    def print_info(self):
        pass

class Book(Printable):
    def __init__(self,tittle,author):
        self.tittle=tittle
        self.author=author

    def print_info(self):
        print(f"Book:{self.tittle} by {self.author}")

book=Book("The Great Gatsby","F. Scott Fitzgerald")

book.print_info()