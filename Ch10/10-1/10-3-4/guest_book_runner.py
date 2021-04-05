import guest_book_class

book = input("Enter book name: ")
guest_book_file = f"{book}.txt"

runner = True

while runner:
    prompt = "Write your name or 'q' to quit: "
    guest = input(prompt)
    if guest == 'q':
        runner = False
    else:
        guest_book = guest_book_class.GuestBook(guest)
        guest_book.write_in_guest_book(guest_book_file, guest)