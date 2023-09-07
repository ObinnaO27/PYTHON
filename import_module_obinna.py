# Obinna Ohale
# Introduction to Programming with Python
# Script 21: "External Class File and the Import Statement"

print("\nWelcome to Script 21: External Class File and the Import Statement")

from System_User import System_User

def main():
    try:
        while True:
            print("\nMenu:\n1. Create User\n2. Exit")
            choice = int(input("Please enter your choice (1/2): "))

            if choice == 1:
                try:
                    u_id = int(input("Please enter user ID: "))
                    u_name = input("Please enter user name: ")
                    u_role = input("Please enter user role: ")
                    u1 = System_User(u_id, u_name, u_role)
                    print("\nUser created successfully!")
                except ValueError:
                    print("Invalid input. User ID should be an integer.")
                except Exception as e:
                    print("An error occurred:", e)

            elif choice == 2:
                print("Exiting User Management System...")
                break

            else:
                print("Invalid choice. Please select a valid option (1/2).")

    except Exception as e:
        print("An unexpected error occurred:", e)

if __name__ == "__main__":
    main()

print("Have a fantastic rest of your day, goodbye!")