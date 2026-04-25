from utils import books,issued_books


#^ ISSUE BOOKS  --------------------
def issue_books():
    name = input("Enter book name : ")
    if name in books:
        books.remove(name)
        issued_books.append(name)
        print(name,"Issued")
    else:
        print(name,"not available")