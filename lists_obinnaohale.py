# Obinna Ohale
# Introduction to Programming with Python
# Script 12: "Arrays (Lists, Tuples and Sets); Read/Write"

def main():
    binary_numbers = (1000, 1001, 1010, 1011, 1100, 1101, 1110, 1111)
    one_to_ten = ("one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten")

    print("Contents of binary_numbers:", binary_numbers)
    print("Contents of one_to_ten:", one_to_ten)

    print("Third value of binary_numbers:", binary_numbers[2])
    print("Fifth value of binary_numbers:", binary_numbers[4])
    print("Seventh value of binary_numbers:", binary_numbers[6])
    print("Third value of one_to_ten:", one_to_ten[2])
    print("Fifth value of one_to_ten:", one_to_ten[4])
    print("Seventh value of one_to_ten:", one_to_ten[6])

    print("Fourth value of binary_numbers:", binary_numbers[3])
    print("Fifth value of binary_numbers:", binary_numbers[4])
    print("Sixth value of binary_numbers:", binary_numbers[5])
    print("Seventh value of binary_numbers:", binary_numbers[6])
    print("Eighth value of binary_numbers:", binary_numbers[7])
    print("Fourth value of one_to_ten:", one_to_ten[3])
    print("Fifth value of one_to_ten:", one_to_ten[4])
    print("Sixth value of one_to_ten:", one_to_ten[5])
    print("Seventh value of one_to_ten:", one_to_ten[6])
    print("Eighth value of one_to_ten:", one_to_ten[7])

    binary_zeroth = binary_numbers[0]
    binary_last = binary_numbers[8]
    print("Zeroth value of binary_numbers:", binary_zeroth)
    print("Last value of binary_numbers:", binary_last)

    one_to_ten_zeroth = one_to_ten[-1]
    one_to_ten_last = one_to_ten[10]
    print("Zeroth value of one_to_ten:", one_to_ten_zeroth)
    print("Last value of one_to_ten:", one_to_ten_last)


one_to_twelve = list()
for num in range(11):
    one_to_twelve.append(num)

one_to_twelve.insert(11, 11)
one_to_twelve.append(13)

one_to_twelve.pop(0)

if __name__ == '__main__':
    main()
else:
    pass

print("Values of one_to_twelve (ascending order):", one_to_twelve)

print("Values of one_to_twelve (descending order):", sorted(one_to_twelve, reverse=True))
