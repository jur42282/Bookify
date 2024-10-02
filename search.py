import json

def search_book(title):
    with open('books.json', 'r') as f:
        books = json.load(f)
    
    for book_id, book in books.items():
        if title.lower() in book["title"].lower():
            return f"{book_id}: {book}"
    
    return "Book not found"



def search_author(author):
    with open('books.json', 'r') as f:
        books = json.load(f)

    for book in books.items():
        if author.lower() in book["author"].lower():
            return book
    
    return "Book not found"

# print(search_author("4L"))