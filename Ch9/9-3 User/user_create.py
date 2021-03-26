import user
import admin

user1 = user.User('Trent', 'Reznor', 'TReznor', 'treznor@nin.com')
user2 = user.User('Jiimy', 'Page', 'jPage', 'jpage@lz.com')
user3 = user.User('tonny', 'stark', 'IronMan', 'ironman@avengers.marvel')

admin = admin.Admin('admin', 'adminson', 'TheAdmin', 'admin@leavealone.me')

user_objects = (user1, user2, user3)

for user_object in user_objects:
    user_object.describe_user()

user1.greet_user('name')
user2.greet_user('name')
user3.greet_user('user')

user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print(user1.login_attempts)

user1.reset_login_attempts()
print(user1.login_attempts)

admin.privileges.show_privileges()