import random
import string

def password(pw_length):
        #to get all the characters we can use in password
        char1 = string.ascii_lowercase
        char2 = string.ascii_uppercase
        char3 = string.digits
        char4 = string.punctuation


        pw = list()
        pw.extend(list(char1)) #to add all the available characters in a list
        pw.extend(list(char2))
        pw.extend(list(char3))
        pw.extend(list(char4))
        random.shuffle(pw) #randomly shuffles the list to get random character selection
        print("We have successfully generated your password.\nYour password is : ")
        print("".join(pw[0:pw_length]))


pw_length = int(input("Enter the required length for password : \n"))
password(pw_length)
print("Is it a good password? y = yes  n =no")
x = input("")
if x == 'Y' or x == 'y':
    exit()
else:
    password(pw_length)
