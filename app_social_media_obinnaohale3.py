# Obinna Ohale
# Introduction to Programming with Python
#Program #1-2: Source Code (Implementation)

print("\nWelcome to a Social Media Screen-Time Tracking Simulation")
print("Select 1 to enter total minutes for the week")
print("Select 2 to enter total hours for the week")

user_selection = input("Enter your choice (1 or 2): ")

if user_selection == '1':
    minutes_spent = int(input("How many minutes did you spend on social media total (week)? "))
    daily_minutes = minutes_spent / 7
elif user_selection == '2':
    hours_spent = float(input("How many hours did you spend on social media total (week)? "))
    daily_minutes = (hours_spent * 60) / 7

daily_hour_total = int(daily_minutes // 60)
daily_min_total = int(daily_minutes % 60)


if user_selection == '1':
    print(f"Your Average Daily Screen time is {daily_min_total} minutes")
elif user_selection == '2':
    print(f"Your Average Daily Screen time is {daily_hour_total} hours")


print("\nThank you for your participation in this Social Media Screen-Time Tracking Simulation")
print("Have a fantastic rest of your day, goodbye")
