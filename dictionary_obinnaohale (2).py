# Obinna Ohale
# Introduction to Programming with Python
# Script 14: "Data Search: Array and Dictionary"
def main():
    user_access = [
        {
            'username': 'admin',
            'password': 'x\\zm/s.y',
            'strength': 'strong'
        },
        {
            'username': 'manager',
            'password': 'xr,ly.zn',
            'strength': 'strong'
        },
        {
            'username': 'editor',
            'password': 'xrytnz',
            'strength': 'fair'
        },
        {
            'username': 'creator',
            'password': 'xyzzts',
            'strength': 'fair'
        },
        {
            'username': 'guest',
            'password': 'xrs',
            'strength': 'weak'
        },
        {
            'username': 'visitor',
            'password': 'lxm',
            'strength': 'weak'
        }
    ]

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
