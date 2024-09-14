import json

def add_book():
    title = input("Enter title: ")
    author = input("Enter author: ")
    isbn = input("Enter ISBN: ")

    try:
        with open('books.json', 'r') as f:
            books = json.load(f)
    except FileNotFoundError:
        books = {}
    except json.JSONDecodeError:
        return "Error reading books.json"

    if isbn in books:
        return "Book already exists"

    books[isbn] = {
        'title': title,
        'author': author,
        'available': True
    }

    try:
        with open('books.json', 'w') as f:
            json.dump(books, f)
    except OSError as e:
        return f"Error writing to books.json: {e}"

    return "Successfully added book"

def remove_book():
    isbn = input("Enter ISBN: ")

    try:
        with open('books.json', 'r') as f:
            books = json.load(f)
    except FileNotFoundError:
        return "books.json not found"
    except json.JSONDecodeError:
        return "Error reading books.json"

    if isbn not in books:
        return "Book not found"

    del books[isbn]

    try:
        with open('books.json', 'w') as f:
            json.dump(books, f)
    except OSError as e:
        return f"Error writing to books.json: {e}"

    return "Successfully removed book"