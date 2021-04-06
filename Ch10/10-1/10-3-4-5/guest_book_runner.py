import book

book_name = input("Enter book name: ")
guest_book_file = f"{book_name}.txt"

runner = True

while runner:
    prompt = "Write your name or 'q' to quit: "
    guest = input(prompt)
    if guest == 'q':
        runner = False
    else:
        guest_book = book.Book(guest)
        print(f'Welcome {guest.title()}')
        guest_book.append_in_book(guest_book_file, guest.title())