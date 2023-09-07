# Obinna Ohale
# Introduction to Programming with Python
# Script 5: "If, Elif, Else"

print("Welcome to Lab 5 on If, Elif, Else statements ")
year = 2023
user_data = input("\nplease enter a year (four digit int, i.e., 2023): ")
int_user_data = int(user_data)

print("\tint_user_data {} {}" .format(int_user_data, type(int_user_data)))

if year == int_user_data:
    print("\tyour entry {} is exactly the same as {}".format(int_user_data, year))
elif year > int_user_data:
    print("\tyour entry {} is less than {}".format(int_user_data, year))
else:
    print("\tyour entry {} is greater than {}".format(int_user_data, year))

print("\nThank you for your participation in Lab 5 on If, Elif, Else statements")
print("\tHave a fantastic rest of your day")
