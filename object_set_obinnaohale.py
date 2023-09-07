# Obinna Ohale
# Introduction to Programming with Python
# Script 22: "Class Object Collections; Array of Objects"

print("\nWelcome to Script 22: Class Object Collections; Array of Objects")

from System_User import System_User

def print_users():
    if not object_list:
        print("No users in the list.")
    else:
        print("\nList of Users:")
        for user in object_list:
            print(f"ID: {user.user_id}, Name: {user.name}, Role: {user.role}")
user_id = 1
def main_menu():
    print("\nMain Menu")
    print("\t1) Add a new user to the list")
    print("\t2) Print all users in the list")
    print("\t3) Update user name and role")
    print("\t4) Exit")
def user_menu():
    print("\nUser Menu")
    print("\t1) Print the user details")
    print("\t2) Update the name")
    print("\t3) Update the role")
object_list = list()
def add_new_user():
    global user_id
    name = input("\tEnter the user's name: ")
    role = input("\tEnter the user's role: ")
    new_user = System_User(user_id, name, role)
    object_list.append(new_user)
    user_id += 1
    print(f"User with ID {user_id - 1} created!")

def update_user_details(user):
    user_menu()
    user_select = int(input("\n\tPlease make a selection: "))

    if user_select == 1:
        print(f"\nUser ID: {user.user_id}, Name: {user.name}, Role: {user.role}")
    elif user_select == 2:
        new_name = input("Enter the updated name: ")
        user.name = new_name
        print("Name updated successfully.")
    elif user_select == 3:
        new_role = input("Enter the updated role: ")
        user.role = new_role
        print("Role updated successfully.")
    else:
        print("Invalid selection. Returning to main menu.")

def main():
    print("\nWelcome to the System User App")

    main_select = -1
    while main_select != 4:
        main_menu()
        main_select = int(input("Please make a selection:"))
        if main_select == 1:
            pass
        elif main_select == 2:
            pass
        elif main_select == 3:
            user_select = -1
            while user_select not in [1, 2, 3]:
                user_menu()
                user_select = int(input("\tPlease make a selection:"))
                if user_select == 1:
                    pass
                elif user_select == 2:
                    pass
                elif user_select == 3:
                    pass
                else:
                    print("\n\tinvalid selection returning to main menu")
if __name__ == "__main__":
    main()

