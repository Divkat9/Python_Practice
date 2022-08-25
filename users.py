
class Users:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
 

    def describe_user(self):
        print(f"The user's first name is {self.first_name}")

    def greet_user(self):
        print(f"Hello! {self.first_name}")
        

new_user = Users('divya', 'katakam') 

print(new_user.describe_user())
print(new_user.greet_user())