library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

def add_book(book_details):
    if book_details in library:
        print(f"{book_details[0]} by {book_details[1]} is already in the list.")
    else:
        library.append(book_details)
        print(f"{book_details[0]} by {book_details[1]} has been added.")

test = ("Moby Dick", "Herman Melville")
add_book(test)
add_book(test)
print(library)