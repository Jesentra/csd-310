# Creating import statements
import sys
import mysql.connector
from mysql.connector import errorcode

# Server configuration
config = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "whatabook",
    "raise_on_warnings": True
}

# Defining functions
# Main Menu functions
def show_menu():
    print("\n  -- Main Menu --")

    print("    1. View Books\n    2. View Store Locations\n    3. My Account\n    4. Exit Program")

    try:
        choice = int(input('      <Please type the number for the desired option here>: '))

        return choice
    except ValueError:
        print("\n  Invalid number, program terminated...\n")

        sys.exit(0)

# Book List function
def show_books(cursor):
    cursor.execute("SELECT book_id, book_name, author, details from book")

    books = cursor.fetchall()

    print("\n  -- DISPLAYING BOOK LISTING --")
    
    for book in books:
        print("  Book Name: {}\n  Author: {}\n  Details: {}\n".format(book[0], book[1], book[2]))

# Shop Locations Function
def show_locations(cursor):
    cursor.execute("SELECT store_id, locale from store")

    locations = cursor.fetchall()

    print("\n  -- DISPLAYING STORE LOCATIONS --")

    for location in locations:
        print("  Locale: {}\n".format(location[1]))

# Select User Function
def validate_user():

    try:
        user_id = int(input('\n      Enter a customer id <Example: Enter 1 for user_id 1>: '))

        if user_id < 0 or user_id > 3:
            print("\n  Invalid customer number, program terminated...\n")
            sys.exit(0)

        return user_id
    except ValueError:
        print("\n  Invalid number, program terminated...\n")

        sys.exit(0)

# Select User Account Function
def show_account_menu():

    try:
        print("\n      -- Customer Menu --")
        print("        1. Wishlist\n        2. Add Book\n        3. Main Menu")
        account_option = int(input('        <Example: Enter 1 for "Wishlist">: '))

        return account_option
    except ValueError:
        print("\n  Invalid number, program terminated...\n")

        sys.exit(0)

# Show User's Wishlist
def show_wishlist(cursor, user_id):

    cursor.execute("SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author " + 
                    "FROM wishlist " + 
                    "INNER JOIN user ON wishlist.user_id = user.user_id " + 
                    "INNER JOIN book ON wishlist.book_id = book.book_id " + 
                    "WHERE user.user_id = {}".format(user_id))
    
    wishlist = cursor.fetchall()

    print("\n        -- DISPLAYING WISHLIST ITEMS --")

    for book in wishlist:
        print("        Book Name: {}\n        Author: {}\n".format(book[4], book[5]))

# Show books available to add to wishlist
def show_books_to_add(cursor, user_id):

    query = ("SELECT book_id, book_name, author, details "
            "FROM book "
            "WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = {})".format(user_id))

    cursor.execute(query)

    books_to_add = cursor.fetchall()

    print("\n        -- DISPLAYING AVAILABLE BOOKS --")

    for book in books_to_add:
        print("        Book Id: {}\n        Book Name: {}\n".format(book[0], book[1]))

# Add books to wishlist function
def add_book_to_wishlist(cursor, user_id, book_id):
    cursor.execute("INSERT INTO wishlist(user_id, book_id) VALUES({}, {})".format(user_id, book_id))

try:

    # Connect to database 
    db = mysql.connector.connect(**config) 

    # Establish cursor
    cursor = db.cursor()

    print("\n  Welcome to WhatABook!")

    # Show main menu
    user_selection = show_menu()  

    # Menu Selection Calls
    while user_selection != 4:

        if user_selection == 1:
            show_books(cursor)

        if user_selection == 2:
            show_locations(cursor)

        if user_selection == 3:
            my_user_id = validate_user()
            account_option = show_account_menu()

            while account_option != 3:

                if account_option == 1:
                    show_wishlist(cursor, my_user_id)

                if account_option == 2:

                    show_books_to_add(cursor, my_user_id)

                    book_id = int(input("\n        Enter the id of the book you want to add: "))

                    # Error message if incorrect number was put in
                    if book_id < 0 or book_id > 9:
                        print("\n       Invalid option, please retry...")
                        book_id = int(input("\n        Enter the id of the book you want to add: "))
                    
                    add_book_to_wishlist(cursor, my_user_id, book_id)

                    db.commit()

                    print("\n        Book id: {} was added to your wishlist!".format(book_id))
 
                if account_option < 0 or account_option > 3:
                    print("\n      Invalid option, please retry...")

                account_option = show_account_menu()
        
        if user_selection < 0 or user_selection > 4:
            print("\n      Invalid option, please retry...")
            
        user_selection = show_menu()

    print("\n\n  Program terminated...")

except mysql.connector.Error as err:

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

finally:
    db.close()