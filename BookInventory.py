def add_book(inventory, title, author, genre, quantity):
    book_details = (author, genre, quantity)
    inventory[title] = book_details
    print(f"Book '{title}' added to the inventory.")

def display_book(inventory, title):
    if title in inventory:
        author, genre, quantity = inventory[title]
        print(f"Title: {title}\nAuthor: {author}\nGenre: {genre}\nQuantity in stock: {quantity}")
    else:
        print(f"Book '{title}' not found in the inventory.")

def update_quantity(inventory, title, new_quantity):
    if title in inventory:
        author, genre, _ = inventory[title]
        inventory[title] = (author, genre, new_quantity)
        print(f"Quantity for book '{title}' updated to {new_quantity}.")
    else:
        print(f"Book '{title}' not found in the inventory.")

def display_all_books(inventory):
    print("\nList of all books in the inventory:")
    for title, details in inventory.items():
        author, genre, quantity = details
        print(f"Title: {title}, Author: {author}, Genre: {genre}, Quantity in stock: {quantity}")
    print()

def main():
    inventory = {}

    while True:
        print("\nBookstore Inventory Management")
        print("1. Add a new book")
        print("2. Display details of a book")
        print("3. Update quantity of a book")
        print("4. Display list of all books")
        print("5. Quit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            title = input("Enter the title of the book: ")
            author = input("Enter the author of the book: ")
            genre = input("Enter the genre of the book: ")
            quantity = int(input("Enter the quantity in stock: "))
            add_book(inventory, title, author, genre, quantity)

        elif choice == '2':
            title = input("Enter the title of the book: ")
            display_book(inventory, title)

        elif choice == '3':
            title = input("Enter the title of the book: ")
            new_quantity = int(input("Enter the new quantity in stock: "))
            update_quantity(inventory, title, new_quantity)

        elif choice == '4':
            display_all_books(inventory)

        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if _name_ == "_main_":
    main()