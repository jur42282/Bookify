import json


def add_book():
    title = input("Enter title: ")
    author = input("Enter author: ")
    isbn = input("Enter ISBN: ")
    
    with open('books.json', 'r') as f:
        books = json.load(f)
    
    if isbn in books:
        return "Book already exists"
    
    books[isbn] = {
        'title': title,
        'author': author,
        'available': True
    }
    
    with open('books.json', 'w') as f:
        json.dump(books, f)
    
    return "Successfully added book"

def remove_book():
    isbn = input("Enter ISBN: ")
    
    with open('books.json', 'r') as f:
        books = json.load(f)
    
    if isbn not in books:
        return "Book not found"
    
    del books[isbn]
    
    with open('books.json', 'w') as f:
        json.dump(books, f)
    
    return "Successfully removed book"

# print(remove_book())
# print(add_book())