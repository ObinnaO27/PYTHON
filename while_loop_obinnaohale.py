# Obinna Ohale
# Introduction to Programming with Python
# Script 7: "While Loops, using counter variables"

print("Welcome to Lab 7")

counter, my_max, my_min = 0, 10, 1

print("Counting up to 10")
while counter <= my_max:
    print("\tCounter is less than min : counter = {}".format(counter))
    counter += 1

print("Counting down from 10")
while counter >= my_min:
    counter -= 1
    print("\tCounter is greater than min : counter = {}".format(counter))


user_input = 1
user_counter = 0
while user_input >= 0:
    user_counter += 1
    user_input = int(input("Enter a positive number: "))

user_counter = 0

while user_input < 0:
    user_input = int(input("Enter a negative number to exit:"))
    user_counter += 1

print("Final user_counter value:", user_counter)

print("\nThank you for your participation in Lab 7 on While Loops, using counter variables")
print("\tHave a fantastic rest of your day")
