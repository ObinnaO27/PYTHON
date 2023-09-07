# Obinna Ohale
# Introduction to Programming with Python
# Script 4: "User Input, Data Type(s)"

string_data = "20"
integer_data = 10
modify_data = 5.0
print("The string_data variable is: {} {}".format(string_data, type(string_data)))

# print(string_data + modify_data)
my_sum = integer_data + modify_data
print("integer_data + modify_data= {} {}".format(my_sum, type(my_sum)))

my_var = int(string_data)
print("new_var + modify_data = {}".format(my_var + modify_data))

int_user_data = int(input("Please enter a whole number: "))
str_user_data = input("Please enter a whole number: ")
print("int_user_data is {} {}".format(int_user_data, type(int_user_data)))
print("str_user_data is {} {}".format(str_user_data, type(str_user_data)))
