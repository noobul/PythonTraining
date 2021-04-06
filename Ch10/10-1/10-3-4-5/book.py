class Book:

    def __init__(self, data):
        self.data = data

    def append_in_book(self, book_name, data):
        with open(book_name, 'a') as file_object:
            file_object.write(f"{data}\n")