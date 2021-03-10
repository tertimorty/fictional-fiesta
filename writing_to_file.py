# This file has examples on how to use python to write to file and or read,
# clear file
pasword_text = 'password = text_for_pasword'
username_text = 'username = Kaspars'
file = 'example_file.txt'


def write_function(input_string):
    # this function writes each statement to new line
    with open(f'{file}', 'a+') as used_file:
        used_file.seek(0)
        data = used_file.read()
        if len(data) > 0:
            used_file.write('\n')
        used_file.write(f'{input_string}')


def read_function():
    with open(f'{file}', 'r') as used_file:
        read_file = used_file.read()
        print(read_file)


write_function(username_text)
write_function(pasword_text)

# read_function()

# this is example on how to use for loop to iterate through files lines
for line in open(f'{file}', 'r'):
    print(line)


def clear_the_file():
    with open(f'{file}', 'w') as file_to_be_owerwriten:
        file_to_be_owerwriten.write()

# clears the file by owervriting existing file and writing nothing to the file
# clear_the_file()
