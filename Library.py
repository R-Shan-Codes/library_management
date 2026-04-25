#~ LIBRARY   -----------------------------
books = {}

#^ ADD BOOKS  ----------------------
def add_books():
    name = input("Enter the book name : ")
    books[name] = True
    print(f"{name} added successfully") 

#^ SHOW BOOKS  -----------------------
def show_books():
    if len(books) == 0:
        print("No books available")
    else:
        print("Available books : ",end="")
        for k,v in books.items():
            if books[k] == True:
                print(k,end=" ")
        print("")
        


#^ ISSUE BOOKS  --------------------
def issue_books():
    name = input("Enter book name : ")
    if name in books.keys() and books[name] == True:
        books[name] = False
        print(name,"Issued")
    else:
        print(name,"not available")


#^ RETURN BOOKS ---------------------
def return_books():
    name = input("Enter book name : ")
    if name in books.keys() and books[name] == False:
        books[name] = True
        print(name,"returned")
    else:
        print(name,"not issued")


#   MAIN BODY ! --------------------------
def library():
    while True:
        print("----------------------------------------------------")
        print("1. Add Books")
        print("2. Show Books")
        print("3. Issue Books")
        print("4. Return Books")
        print("5. Exit")
        print("----------------------------------------------------")
        choice = int(input("Enter your choice : "))

        if choice == 1:
            add_books()
        elif choice == 2:
            show_books()
        elif choice == 3:
            issue_books()
        elif choice == 4:
            return_books()
        elif choice == 5:
            print("Thank You")
            break
        else:
            print("Invalid Choice")
            break
        
#? RUN    -----------------------------
library()
