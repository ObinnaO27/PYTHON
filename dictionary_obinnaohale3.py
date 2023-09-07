# Obinna Ohale
# Introduction to Programming with Python
# Script 14: "Data Search: Array and Dictionary"
def main():
    print("Welcome to lab 14, Data Search: Array and Dictionary ")
    user_1 = {
        'username': 'admin',
        'password': 'x\\zm/s.y',
        'strength': 'strong'}

    user_2 = {
        'username': 'manager',
        'password': 'xr,ly.zn',
        'strength': 'strong'}

    user_3 = {
        'username': 'editor',
        'password': 'xrytnz',
        'strength': 'fair'}

    user_4 = {
        'username': 'creator',
        'password': 'xyzzts',
        'strength': 'fair'}

    user_5 = {
        'username': 'guest',
        'password': 'xrs',
        'strength': 'weak'}

    user_6 = {
        'username': 'visitor',
        'password': 'lxm',
        'strength': 'weak'}

    user_access = [user_1, user_2, user_3, user_4, user_5, user_6]

    print("User access list:")
    for user in user_access:
        print(user)
    print()

    print("Username and password strength:")
    for user in user_access:
        username = user['username']
        password_strength = user['strength']
        print("Username: ", username, " Password Strength: ", password_strength)
    print()

    print("Users with password strength better than weak:")
    for user in user_access:
        if user['strength'] != 'weak':
            print(user['username'])
    print()

    print("Users with strong password strength:")
    for user in user_access:
        if user['strength'] == 'strong':
            print(user['username'])

if __name__ == '__main__':
    main()


    print("\nThank you for your time")
    print("\nHave a great day!")