import json
import hashlib

global permitted

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register(username, password):
    try:
        with open('users.json', 'r') as f:
            users = json.load(f)
    except FileNotFoundError:
        users = {}
    
    if username in users:
        return "User already exists"
    
    users[username] = {
        "id" : len(users),
        "password" : hash_password(password),
        "books" : [],
        "is_admin" : False
    }
    
    with open('users.json', 'w') as f:
        json.dump(users, f)
    
    return "Successfully registered"


def login(username, password):
    global permitted
    with open('users.json', 'r') as f:
        users = json.load(f)
    
    if username not in users:
        return "User not found"
    
    if users[username]["password"] == hash_password(password):
        print("Successfully logged in")
        permitted= True
        print(f"login{permitted}")
    else:
        print("Invalid password")
        permitted = False
        print(f"login{permitted}")
    
login("admin", "admin")