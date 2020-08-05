import random
import string
from password_strength import PasswordPolicy

def password(pw_length):
        char1 = string.ascii_lowercase
        char2 = string.ascii_uppercase
        char3 = string.digits
        char4 = string.punctuation


        pw = list()
        pw.extend(list(char1))
        pw.extend(list(char2))
        pw.extend(list(char3))
        pw.extend(list(char4))
        random.shuffle(pw)
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
