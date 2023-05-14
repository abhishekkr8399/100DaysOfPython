#|----------------------------------------------------------------|
#|Description    :    Library Management Program
#|----------------------------------------------------------------|
#|Author         :    ABHISHEK KUMAR, Computer Science Student
#|----------------------------------------------------------------|
#|Organization   :    NMAMIT, Nitte
#|----------------------------------------------------------------|
#|E-Mail         :    abhishekkumar8399@gmail.com
#|----------------------------------------------------------------|
class Library:
    def __init__(self):
        self.noOfBooks = 0
        self.books=[]

    def addBooks(self, book):
        self.books.append(book)
        self.noOfBooks = len(self.books)

    def showInfo(self):
        print(f"The Library has {self.noOfBooks} books. The books are:")
        for book in self.books:
            print(book)


l1=Library()
l1.addBooks("Harry Potter")
l1.showInfo()