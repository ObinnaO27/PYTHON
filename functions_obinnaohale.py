# Obinna Ohale
# Introduction to Programming with Python
# Script 10: "Functions as Reusable/Callable Code"

# functions_yourname.py

def test_call():
    """
    Function that does not take or return any data.
    """
    print("Now inside of test_call.")

def test_return(value):
    """
    Function that takes an integer, updates it, and returns it to the caller.
    """
    print("Inside test_return")
    print("Found", value, "updating and returning", value + 1)
    value += 1
    return value

def empty_or_max(user_data, status):

    max_length = 10  # Example max length
    if status == 1:
        if len(user_data) > max_length or len(user_data) == 0:
            status = 0
    return status

def main():

    print("Welcome!")

    test_call()

    try:
        value = test_return(5)
        print("Returned value:", value)
    except Exception as e:
        print("Error occurred:", str(e))

    user_data = input("Enter user data: ")
    status = int(input("Enter status (1 or 0): "))

    updated_status = empty_or_max(user_data, status)
    print("Updated status:", updated_status)

if __name__ == '__main__':
    main()


    print("\nthis was Lab 10 Functions on Reusable/Callable Code, thank you for your time")




