class Library():
    def __init__(self, Title, Author, ISBN):
        self.Books = []
        self.Title = Title
        self.Author = Author
        self.ISBN = ISBN

    def showBooks(self):
        if not self.Books:
            print("Library Catalog: Empty")
        else:
            print("Library Catalog:")
            for book in self.Books:
                print(f"Title: {book[0]} | Author: {', '.join(book[1])} | ISBN: {book[2]}")

    def addBook(self):
        Title = input("Enter Book Title: ").upper()
        Author = input("Enter Book Author(s) (comma-separated): ").split(",")
        Author = [x.strip().upper() for x in Author]

        if len(Author) < 1:
            print("Error: At least one author must be provided.")
            return

        ISBN = input("Enter Book ISBN: ")

        if len(ISBN) != 13:
            print("Error: ISBN must be a 13-digit number.")
            return

        self.Books.append([Title, Author, ISBN])
        print("Book added successfully.")

    def search_Title(self):
        title = input("Enter Book Title to search: ").upper()
        found = False
        for book in self.Books:
            if title in book[0]:
                print("Book Found:")
                print(f"Title: {book[0]} | Author: {', '.join(book[1])} | ISBN: {book[2]}")
                found = True
                break
        if not found:
            print("Book not found in the library.")

    def search_Author(self):
        author = input("Enter Author Name to search: ").upper()
        found = False
        for book in self.Books:
            if author in book[1]:
                print("Book Found:")
                print(f"Title: {book[0]} | Author: {', '.join(book[1])} | ISBN: {book[2]}")
                found = True
        if not found:
            print("No books found by this author.")

    def search_ISBN(self):
        isbn = input("Enter ISBN to search: ")
        found = False
        for book in self.Books:
            if isbn == book[2]:
                print("Book Found:")
                print(f"Title: {book[0]} | Author: {', '.join(book[1])} | ISBN: {book[2]}")
                found = True
                break
        if not found:
            print("No book found with this ISBN.")

library = Library("My Library", "Unknown Author", "9781614841002")

while True:
    print("\nLibrary Management System")
    print("1. Show all Books")
    print("2. Add Book")
    print("3. Search Book By Title")
    print("4. Search Book By Author")
    print("5. Search Book By ISBN")
    print("6. Exit")

    choice = input("Enter Your Choice (1-6): ")

    if choice == "1":
        library.showBooks()
    elif choice == "2":
        library.addBook()
    elif choice == "3":
        library.search_Title()
    elif choice == "4":
        library.search_Author()
    elif choice == "5":
        library.search_ISBN()
    elif choice == "6":
        print("Thank you for using the Library Management System. Goodbye.")
        break
    else:
        print("Invalid Choice. Please try again.")
