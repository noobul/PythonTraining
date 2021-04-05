class GuestBook:

    def __init__(self, guest):
        self.guest = guest

    def write_in_guest_book(self, guest_book, guest):
        with open(guest_book, 'a') as file_object:
            file_object.write(f"{guest.title()}\n")