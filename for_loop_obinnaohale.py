# Obinna Ohale
# Introduction to Programming with Python
# Script 8: "For Loops, and List Enumeration"

print("\nWelcome to Lab 8 on Loops, and List Enumeration")

for num in range(1, 11):
    print(num)

countdown = 10
print("Countdown value:", countdown)

for i in range(1, 11):
    countdown -= 1
    print("Countdown value:", countdown, "Range index:", i)

user_input = input("Enter a value to search for: ")
alpha = ["abcd", "efg", "hijk", "lmnop", "qrs", "tuv", "wxyz"]

# Print values in alpha using enumerate
print("The values in alpha are:", end=" ")
for index, value in enumerate(alpha):
    if index != len(alpha) - 1:
        print(value, end=", ")
    else:
        print(value)

# Ask user for input value
user_input = input("Please enter a value to search for: ")

# Search for the input value in the alpha list
found = False
for item in alpha:
    if user_input == item:
        found = True

if found:
    print("The value", user_input, "was found in the collection.")
else:
    print("Sorry, the value", user_input, "was not found.")

print("\nThank you for your participation in Lab 8 For Loops, and List Enumeration")
print("\tHave a fantastic rest of your day")



