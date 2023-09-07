# Obinna Ohale
# Introduction to Programming with Python
# Script 15: "File IO: File Create, Write and Close"


def create_file(file_name):

    file_handle = open(file_name, 'w')
    file_handle.close()


def write_data(file_name):

    file_handle = open(file_name, 'w')
    file_handle.write("Steps to file management:\n\n")
    file_handle.write("1: Create or open a file.\n\n")
    file_handle.write("2: Write or read data from the file.\n\n")
    file_handle.write("3: Close the file connection or handle.\n")
    file_handle.close()  # Close the file handle


def print_data(file_name):

    file_handle = open(file_name, 'r')
    print(file_handle.read())  # Print the contents of the file
    file_handle.close()  # Close the file handle


def main():
    file_name = "data_file.data"
    create_file(file_name)  # Create the file
    write_data(file_name)  # Write data to the file
    print_data(file_name)  # Print the data from the file

main()


print("Have a fantastic rest of your day, goodbye!")