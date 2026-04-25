from utils import books,issued_books

#^ RETURN BOOKS ---------------------
def return_books():
    name = input("Enter book name : ")
    if name in issued_books:
        issued_books.remove(name)
        books.append(name)
        print(name,"returned")
    else:
        print(name,"not issued")