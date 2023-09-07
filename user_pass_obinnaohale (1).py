# Obinna Ohale
# Introduction to Programming with Python
# Program #2-2: Source Code (Implementation)

def validate_credentials(username, password):
    validInput = True

    if len(username) < 5 or len(username) > 10:
        print("Username must be between 5 and 10 characters.")
        validInput = False

    if not username[0].isalpha():
        print("Username must start with a letter.")
        validInput = False

    if " " in username:
        print("Username cannot contain spaces.")
        validInput = False

    if len(password) < 5 or len(password) > 10:
        print("Password must be between 5 and 10 characters.")
        validInput = False

    if not password[0].isalpha():
        print("Password must start with a letter.")
        validInput = False

    if " " in password:
        print("Password cannot contain spaces.")
        validInput = False

    if username == password:
        print("Username and password cannot be the same.")
        validInput = False

    return validInput

# User Prompt
username = input("Please enter a username (5 to 10 characters, no spaces): ")
password = input("Please enter a password (5 to 10 characters, no spaces): ")

# Validate credentials
if validate_credentials(username, password):
    print("Your username and password are:")
    print("Username: " + username)
    print("Password: " + password)

    daily_hour_total = 2
    daily_min_total = 30

    print("Your Average Daily Screen time is {}:{}".format(daily_hour_total, daily_min_total))
    print("Thank you for your participation in this Username and Password Validation App")
    print("Have a fantastic rest of your day, goodbye!")
else:
    print("Please correct the errors in your input.")
