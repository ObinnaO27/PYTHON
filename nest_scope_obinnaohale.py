# Obinna Ohale
# Introduction to Programming with Python
# Script 11: "Statement Nesting and Variable Scope"

def multiverse_0(visitor):
    return visitor

def multiverse_1(visitor):
    return visitor + " from Multiverse 1"

def multiverse_2(visitor):
    return "There is no escape from Multiverse 2"

def main():
    user_name = input("Enter your name: ")

    mv_1 = multiverse_1(user_name)
    print("mv_1:", mv_1)

    mv_0 = multiverse_0(user_name)
    print("mv_0:", mv_0)

    mv_1 = multiverse_1(user_name)
    print("mv_1:", mv_1)

    mv_2 = multiverse_2(user_name)
    print("mv_2:", mv_2)

    mv_0_nested = multiverse_0(multiverse_1(user_name))
    print("mv_0 (nested):", mv_0_nested)

    mv_0_nested_2 = multiverse_0(multiverse_2(user_name))
    print("mv_0 (nested):", mv_0_nested_2)

    mv_0_nested_both = multiverse_0(multiverse_1(multiverse_2(user_name)))
    print("mv_0 (nested):", mv_0_nested_both)

# Call the main function
main()

print("\nThank you for your participation in Lab 11 For Statement Nesting and Variable Scope")
print("\tHave a fantastic rest of your day")