import add_books,show_books,issue_books,return_books

# MAIN BODY ! --------------
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