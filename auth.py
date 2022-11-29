import re
import simplejson
from turtle import textinput
from tkinter import messagebox
import thankYou
import details
from colorama import Back,Fore,Style
def auth():
    username,password = enterDetails()
    user = checkUser(username,password)
    if user :
        print(Back.GREEN+'Login Successfull')
        print(Style.RESET_ALL)
        # print('Login Successfull')
        # let user do work
        details.detail()
    else:
        # redirect user to the login window
        # messagebox.showinfo('Alert', '')
        choice = input(Fore.RED +"Invalid Login Credentials !!!One more try...? (y/n)")
        print(Style.RESET_ALL)
        if choice == 'y':
            auth()
        elif choice == 'n':
            thankYou.thank_you()
            # messagebox.showinfo('Alert', 'Thanks for using :)')
            # print("")
        # print(choice)



def enterDetails():
    username = input("Username: ")
    password = input("Password: ")
    return username,password

def grabJSON(s):
    FLAGS = re.VERBOSE | re.MULTILINE | re.DOTALL
    WHITESPACE = re.compile(r'[\t\n\r]*', FLAGS)
    decoder = simplejson.JSONDecoder()
    obj, end = decoder.raw_decode(s)
    end = WHITESPACE.match(s, end).end()
    return obj, s[end:]

def checkUser(username,password):
    with open("users.txt") as f:
        s = f.read()
    while True:
        obj, remaining = grabJSON(s)
        if obj['username'] == username and obj['password'] == password :
            return True
        s = remaining
        if not remaining.strip():
            break
    return False

