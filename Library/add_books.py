from utils import books


#^ ADD BOOKS  ----------------------
def add_books():
    name = input("Enter the book name : ")
    books.append(name)
    print(f"{name} added successfully")    