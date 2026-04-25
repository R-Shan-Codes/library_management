from utils import books


#^ SHOW BOOKS  -----------------------
def show_books():
    if len(books) == 0:
        print("No books available")
    else:
        print("Available books : ",end="")
        for book in books:
            print(book,end=" ")
        print("")