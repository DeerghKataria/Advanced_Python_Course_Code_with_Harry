# Library Management System
class Library:
    def __init__(self, listOfBooks):
        self.books = listOfBooks

    def availableBooks(self):
        print("Books present in the library are: ")
        for i in range(len(self.books)):
            print(f"{i+1}. {self.books[i]}")

    def borrowBook(self, bookName):
        if bookName in self.books:
            print(f"You have been issued the book {bookName}. Please keep it safely and return it within 7 days.")
            self.books.remove(bookName)
            return True
        else:
            print("Sorry, the following book is currently unavailable!")
            return False

    def returnBook(self, bookName):
        self.books.append(bookName)
        print("Thank you for returning the book on time!")

class Student:
    def __init__(self):
        self.bookList = []

    def requestBook(self):
        self.book = input("Enter the name of the book that you want to borrow:")
        return self.book
    
    def returnBook(self):
        self.book = input("Enter the name of the book that you want to borrow:")
        return self.book

if __name__ == "__main__":
    centralLibrary = Library(["Rich Dad Poor Dad", "Intelligent Investor", 
        "48 Laws of Power", "Think and Grow Rich", "7 Habits of Highly Effective People",
        "12 Rules For Life", "Ikigai", "Man's Search for Meaning", "The Richest Man in Babylon",
        "The Alchemist", "Attitude is Everything"])

    stud = Student()

    # For menu driven functionality

    while(True):
        welcomeMessage = '''**** Welcome to Central Library ****
            Please Choose an Option:
            1. Listing all the books
            2. Request a book
            3. Return a book
            4. Exit the Library
            '''
        ch = int(input("Enter choice: "))
        if ch == 1:
            centralLibrary.availableBooks()
        elif ch == 2:
            centralLibrary.borrowBook(stud.requestBook())
        elif ch == 3:
            centralLibrary.returnBook(stud.returnBook())
        elif ch == 4:
            print("Thank you for choosing the Central Library!")
            exit()
        else:
            print("Enter a valid choice!")
        print(welcomeMessage)