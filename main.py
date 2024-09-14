import json
import login
import booksmanager
import search



def main():
    while True:
        print("Welcome to the library")
        print("1. Login")
        print("2. Register")
        choice = input("Enter choice: ")
        
        if choice == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")
            login.login(username, password)
            if login.permitted:
                global user
                user = username
                print(f"main{login.permitted}")
                break
            if login.permitted == False:
                print("Invalid username or password")
                print(f"main{login.permitted}")
        elif choice == "2":
            username = input("Enter username: ")
            password = input("Enter password: ")
            print(login.register(username, password))
        else:
            print("Invalid choice")
        
    with open('users.json', 'r') as f:
        users = json.load(f)

    if users[user]["is_admin"]:
        while True:
            print("1. Add book")
            print("2. Remove book")
            print("3. Search book")
            print("4. List all books")
            print("5. List all users")
            print("6. Logout")
            choice = input("Enter choice: ")

            if choice == "1":
                print(booksmanager.add_book())

            elif choice == "2":
                booksmanager.remove_book()

            elif choice == "3":
                print("1. Search by title")
                print("2. Search by author")
                search_choice = input("Enter choice: ")

                if search_choice == "1":
                    title = input("Enter title: ")
                    print(search.search_book(title))

                elif search_choice == "2":
                    author = input("Enter author: ")
                    print(search.search_author(author))
            
            elif choice == "4":
                with open('books.json', 'r') as f:
                        books = json.load(f)
                for  book in books.items():
                    print(book)

            elif choice == "5":
                print(users.list_users())

            elif choice == "6":
                login.permitted = False
                print("Successfully logged out")
                break

def lent_book(user, book_isbn):
    with open('books.json', 'r') as f:
        books = json.load(f)
    
    if book_isbn not in books:
        return "Book not found"
    
    book = books[book_isbn]
    
    if not book.get("available", True):
        return "Book not available"
    
    book["available"] = False
    book["user"] = user
    
    with open('books.json', 'w') as f:
        json.dump(books, f)
    
    with open('users.json', 'r') as f:
        users = json.load(f)
    
    if user not in users:
        users[user] = {"books": []}
    
    users[user]["books"].append(book_isbn)
    
    with open('users.json', 'w') as f:
        json.dump(users, f)
    
    return "Successfully lent book"

def return_book(user, book_isbn):
    with open('books.json', 'r') as f:
        books = json.load(f)
    
    if book_isbn not in books:
        return "Book not found"
    
    book = books[book_isbn]
    
    if book.get("available", True):
        return "Book already available"
    
    if book.get("user", "") != user:
        return "Book not lent by you"
    
    book["available"] = True
    book["user"] = ""
    
    with open('books.json', 'w') as f:
        json.dump(books, f)
    
    with open('users.json', 'r') as f:
        users = json.load(f)
    
    users[user]["books"].remove(book_isbn)
    
    with open('users.json', 'w') as f:
        json.dump(users, f)
    
    return "Successfully returned book"

if __name__ == "__main__":
    main()