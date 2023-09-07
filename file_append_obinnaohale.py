# Obinna Ohale
# Introduction to Programming with Python
# Script 16: "File IO: File Append and Update"

print("\nWelcome to Script 16: File IO: File Append and Update")

def line_counter(file_name):
    file_line_count = 0
    file_handle = open(file_name, 'r')
    for _ in file_handle:
        file_line_count += 1
    file_handle.close()
    return file_line_count

def append_file(file_name, file_line_count):
    file_handle = open(file_name, 'a')
    file_handle.write(f"{file_name} had {file_line_count} lines of data, and now it has {file_line_count + 1}\n")
    file_handle.close()

def confirm_append(file_name):
    file_handle = open(file_name, 'r')
    file_content = file_handle.read()
    file_handle.close()
    print(file_content)

def append_to_ten(file_name):
    file_line_count = line_counter(file_name)
    while file_line_count <= 9:
        append_file(file_name, file_line_count)
        file_line_count = line_counter(file_name)

    append_file(file_name, file_line_count)

    confirm_append(file_name)

def main():
    file_name = "data_file.data"
    append_to_ten(file_name)

main()

print("Have a fantastic rest of your day, goodbye!")

#I am not sure why it is printing so many lines
# I was messing around with it for a wile but cannot find what the problem is
# im not sure if i am overthinking this but wanted to see if you knew the solution
# in the meantime I am going to recode this from scratch