# Obinna Ohale
# Introduction to Programming with Python
# Script 6: "If statements (employing AND and OR)"

print("\nWelcome to Lab 6 on multiple evaluation (employing AND and OR) ")

my_min, my_max = 0, 256

user_data = int(input("\n\tPlease enter a byte-sized int (from zero - 255):"))

if user_data >= my_min and user_data < my_max:
    print("\tValid: greater than or equal to min, or less than max")
elif (user_data < my_min) or (user_data <= my_max):
    print("\tInvalid: less than zero, or greater than or equal to max")
else:
    print("\tNull: you will never get here")

print("\nThank you for your participation in Lab 6 on multiple evaluation (employing AND and OR)")

print("\tHave a fantastic rest of your day")
