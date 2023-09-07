# Obinna Ohale
# Introduction to Programming with Python
# Script 18: "Simple Class Declaration"


print("\nWelcome to Script 18: Simple Class Declaration")


class User_Data:
    user_name = ""
    user_role = ""
    user_id = 0

    def __init__(self):
        print('\nThe User_Data class constructor has been called.')

    def set_user_name(self, new_name):
        self.user_name = new_name
        return

    def get_user_name(self):
        return self.user_name

    def get_user_role(self):
        return self.user_role

    def set_user_role(self, new_role):
        self.user_role = new_role
        return

    def set_user_id(self, new_id):
        self.user_role = new_id
        return

    def get_user_id(self):
        return self.user_id


def main():
    ud_1 = User_Data()

    ud_1.set_user_name("john")
    print(ud_1.get_user_name)

    ud_1.set_user_role("admin")
    print(ud_1.get_user_role)

    ud_1.set_user_id("0")
    print(ud_1.get_user_id)

    return


main()

print("\nHave a fantastic rest of your day, goodbye!")
