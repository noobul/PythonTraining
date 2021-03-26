import user
import privileges

class Admin(user.User):

    def __init__(self, first_name, last_name, user_name, user_email):
        super().__init__(first_name, last_name, user_name, user_email)
        self.privileges = privileges.Privileges()