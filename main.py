import json
import login
import books
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
            print(login.login(username, password))
            if login.permitted:
                global user
                user = username
                print(user)
                break
            else:
                print("Invalid username or password")
        elif choice == "2":
            username = input("Enter username: ")
            password = input("Enter password: ")
            print(login.register(username, password))
        else:
            print("Invalid choice")
        
        with open('users.json', 'r') as f:
            users = json.load(f)

        if users[username].get("is_admin", False):
            while True:
                print("1. Lent book")
                print("2. Return book")
                print("3. Exit")
                choice = input("Enter choice: ")

                if choice == "1":
                    book_isbn = input("Enter ISBN: ")
                    print(lent_book(user, book_isbn))
                elif choice == "2":
                    pass
                elif choice == "3":
                    break
                else:
                    print("Invalid choice")
        if users[username].get("is_admin", True):
            while True:
                print("1. Add book")
                print("2. Remove book")
                print("3. Exit")
                choice = input("Enter choice: ")
                
                if choice == "1":
                    print(books.add_book())
                elif choice == "2":
                    print(books.remove_book())
                elif choice == "3":
                    break
                else:
                    print("Invalid choice")
            

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

main()