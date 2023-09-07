# Obinna Ohale
# Introduction to Programming with Python
# Script 13: "Multi-Dimensional Arrays"

def main():

    print("\nWelcome to lab 13, Multi-Dimensional Arrays")

    r1 = ('X','R','S')
    r2 = ('L','Y','T')
    r3 = ('M','N','Z')

    c1 = ('X','L','M')
    c2 = ('R','Y','N')
    c3 = ('S','T','Z')

#Using only row variables and a loop, print the table (without the labels)
#Using only column variables and a loop, print the table (without the labels)

#Using list comprehension or a loop, create a new list clone_list = list() which contains as a multi-dimensional array, all the values contained in either the comprehensive row or column list.
#Print out the value of clone_list, which should look exactly the same as the table printed before.

    print("\nPrinting raw row variables")
    row_lists = r1, r2, r3
    for each, value in enumerate(row_lists):
        print("{}    {}     {}".format(row_lists[each][0],row_lists[each][1], row_lists[each][2]))

    print("\nPrinting raw column variables")
    column_lists = c1, c2, c3
    for each, value in enumerate(column_lists):
        print("{}    {}    {}".format(column_lists[0][each],column_lists[1][each], column_lists[2][each]))


    print("Printing List Comprehension")

    row_comp = [x for x in row_lists]
    print("\nPrinting Clone row list {}".format(row_comp))

    clmn_comp= [x for x in column_lists]
    print("\nPrinting Clone Column list {}".format(clmn_comp))

    print("\nThank you for your time")
    print("This was Lab 13, Multi Dimensional Arrays")
    print("\nHave a great day!")
if __name__ == '__main__':
    main()




