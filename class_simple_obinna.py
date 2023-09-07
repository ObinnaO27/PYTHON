# Obinna Ohale
# Introduction to Programming with Python
# Script 18: "Simple Class Declaration"

print("\nWelcome to Script 18: Simple Class Declaration")

class Person:
    preferred_name = ""
    life_goal = ""

    def __init__(self, name, goal):

        self.preferred_name = name
        self.life_goal=goal

    def describe_person(self):
        print("\nThe goal of {} is to {}.".format(self.preferred_name, self.life_goal))
        return


def main():
    me = Person("Chris", "learn")
    me_2 = Person("John", "be the best me")
    me.describe_person()
    me_2.describe_person()

    return


main()

print("\nHave a fantastic rest of your day, goodbye!")