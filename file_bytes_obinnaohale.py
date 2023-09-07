# Obinna Ohale
# Introduction to Programming with Python
# Script 17: "File IO: Read, Write Byte-Data

print("\nWelcome to Script 17: File IO: Read, Write Byte-Data")


def write_bytes(file_name, string_data):
    with open(file_name, 'w') as file_handle:
        byte_data: bytes = bytes(string_data, encoding='utf8')
        file_handle.write(byte_data)

def print_bytes(file_name):
    with open(file_name, 'rb') as file_handle:
        byte_data = file_handle.read()
        print(byte_data)

def print_strings(rd_byte_file):
    with open(rd_byte_file, 'rb') as binary_file:
        byte_data = binary_file.read()
        string_data = byte_data.decode("utf-8")
        print(string_data)

def main():
    file_name = "byte_file.bytes"
    user_input = input("Enter a name or a word: ")
    write_bytes(file_name, user_input)
    print("Byte Data:")
    print_bytes(file_name)
    print("String Data:")
    print_strings(file_name)

main()



