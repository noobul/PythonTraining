class User:
    def __init__(self, first_name, last_name, user_name, user_email):
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.user_email = user_email
        self.login_attempts = 0 #9-4

    def describe_user(self):
        user_summary = {
            'first name' : self.first_name.title(),
            'last name' : self.last_name.title(),
            'user name' : self.user_name,
            'email' : self.user_email,
        }

        print(user_summary)

    def greet_user(self, greet_request):
        if greet_request == 'name':
            print(f"Hello {self.first_name} {self.last_name}!")
        elif greet_request == 'user':
            print(f"Wazzup {self.user_name}!")
        else:
            print(f'{greet_request}')

    def increment_login_attempts(self):
        self.login_attempts +=1
    
    def reset_login_attempts(self):
        self.login_attempts = 0