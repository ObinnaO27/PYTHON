# Obinna Ohale
# Introduction to Programming with Python
# Script 13: "Multi-Dimensional Arrays"

print("\nWelcome to Script 13: Multi-Dimensional Arrays")
def print_table_by_rows():

    table = [
        ['X', 'R', 'S'],
        ['L', 'Y', 'T'],
        ['M', 'N', 'Z']
    ]

    for row in table:
        for item in row:
            print(item, end=' ')
        print()
def print_table_by_columns():

    table = [
        ['X', 'R', 'S'],
        ['L', 'Y', 'T'],
        ['M', 'N', 'Z']
    ]

    for i in range(len(table[0])):
        for j in range(len(table)):
            print(table[j][i], end=' ')
        print()
def create_clone_list():

    table = [
        ['X', 'R', 'S'],
        ['L', 'Y', 'T'],
        ['M', 'N', 'Z']
    ]


    clone_list = [item for row in table for item in row]

    return clone_list

def main():

    print("Table printed by rows:")
    print_table_by_rows()
    print()

    print("Table printed by columns:")
    print_table_by_columns()
    print()

    clone_list = create_clone_list()
    print("clone_list:")
    print(clone_list)

if __name__ == '__main__':
    main()