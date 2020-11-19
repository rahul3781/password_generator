'''
Password cracking using Brute Force.
For faster results only use alphabetic passwords
'''

# importing random
from random import *

# taking input from user
user_password = input("Enter your password : ")

# storing alphabet letter to use thm to crack password
password = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
            'w', 'x', 'y', 'z', ]

# initializing an empty string
guess_pass = ""

# run the loop to generate passwords until it matches user's password
while (guess_pass != user_password):
    guess_pass = ""
    # generating random passwords using for loop
    for letter in range(len(user_password)):
        guess_letter = password[randint(0, 25)]
        guess_pass = str(guess_letter) + str(guess_pass)
    # printing guessed passwords
    print(guess_pass)

# printing the matched password
print("Your password is : ", guess_pass)
