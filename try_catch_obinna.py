# Obinna Ohale
# Introduction to Programming with Python
# Script 20: "Object Creation and Error Handling as Try-Except"

print("\nScript 20: Object Creation and Error Handling as Try-Except")

# File: try_catch_yourname.py

class Error_Class:
    def __init__(self):
        print('The Error_Class constructor has been called.')

    def catch_zero(self):
        try:
            bad_result = 5 / 0
        except ZeroDivisionError as e:
            print("The catch_zero() method detected a ZeroDivisionError Error as {}".format(e))

    def catch_file_not_found(self):
        try:
            with open("not there.txt"):
                pass
        except FileNotFoundError as e:
            print("The catch_file_not_found() method detected a FileNotFoundError Error as {}".format(e))

    def catch_import_error(self):
        try:
            import non_existent_module
        except ImportError as e:
            print("The catch_import_error() method detected an ImportError Exception as {}".format(e))


def main():
    print("\nScript 20: Object Creation and Error Handling as Try-Except")
    e1 = Error_Class()
    print("\nWelcome! You can choose from the following options:")
    while True:
        print("\n1. Catch ZeroDivisionError")
        print("2. Catch FileNotFoundError")
        print("3. Catch ImportError")
        print("4. Exit")
        choice = input("\nEnter your choice (1/2/3/4): ")

        if choice == '1':
            e1.catch_zero()
        elif choice == '2':
            e1.catch_file_not_found()
        elif choice == '3':
            e1.catch_import_error()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please choose a valid option.")

    print("\nHave a fantastic rest of your day, goodbye!")

if __name__ == '__main__':
    main()


