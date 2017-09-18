# Write a program that opens a file called "my-file.txt", then prints
# each of lines form the file.
# If the program is unable to read the file (for example it does not exists),
# then it should print an error message like: "Unable to read file: my-file.txt"

def open_me():
    try:
        file = open("my-file.txt", "r")
        text=file.read()
        print(text)
        file.close
    except FileNotFoundError:
        print('Hey, this file does not exist!')
open_me()