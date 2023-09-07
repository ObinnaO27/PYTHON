# Obinna Ohale
# Introduction to Programming with Python
# Script 9: "Outer and Inner Loops (Nested Loops)"


print("\nWelcome to Script 9: Outer and Inner Loops (Nested Loops)")

stop_at = 3
outer_count = 1

print("Now printing incrementing nested loop:")
for each in range(1, 4):
    inner_count = 1
    for each in range(1, 4):
        print("\tOuter Value {}, Inner Value {}".format(outer_count, inner_count))
        inner_count +=1
    outer_count +=1


start_max = 3
outer_count = 3

print("\nNow printing decrementing nested loop:")
for each in range(0, start_max):
    inner_count = 3
    for each in range(0, start_max):
        print("\tOuter Value {}, Inner Value {}".format(outer_count, inner_count))
        inner_count -=1
    outer_count -=1

print("\nHave a fantastic rest of your day, goodbye!")
