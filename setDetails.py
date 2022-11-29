import generator
import datetime
import pyperclip
from tkinter import messagebox
import json
import details
import time
from colorama import Fore,Back,Style


def psl():
    psLength =input("For generating new password\nEnter required length of password: ")
    if psLength.isdigit() and int(psLength)>6:
        return int(psLength)
    elif int(psLength)<5:
        print(Fore.RED +"Warning : Password length must greater then 6")
        print(Style.RESET_ALL)
        psl()
    else:
        print(Fore.RED +"Warning : Password length must be an integer")
        print(Style.RESET_ALL)
        psl()

def ch():
    choice = input("Want to store existing password ? \nEnter y to go with existing password OR \nn to generate new password (y/n):")
    password = ""
    if choice == "y":
        password = input("Enter Password and Press Enter to Proceed: ")
        return password
    elif choice == "n":
        # Flag = 1
        x=psl()
        password = generator.generate(x)
        return password
    else:
        print(Fore.RED +"Enter relevent charactor please.")
        print(Style.RESET_ALL)
        time.sleep(.2)
        ch()
def saveDetails():
    companyName = input("Enter Platform Name: ")
    userName = input("Enter Username: ")
    password = ch()
    remark = input("Enter Remark: ")
    print("\n*************************************************\n")
    temp = input("Press Enter to save details :")
    e = datetime.datetime.now()
    if int(e.hour) < 12:
        h =e.hour
    else:
        h = int(e.hour)-12
    myDict = {
        "Date": str(("%s/%s/%s" % (e.day, e.month, e.year))),
        "Time":str(("%s:%s:%s" % (h, e.minute, e.second))),
        "Platform Name":companyName,
        "username" :userName,
        "password": password,
        "remark" :remark
    }
    file = open("passwords.txt","a") 
    pas = json.dumps(myDict)
    file.write(pas)
    file.close() 
    print(Back.GREEN+"*********************************Details Saved Successfully*******************************")
    print(Style.RESET_ALL)
    pyperclip.copy(password)
    print(Fore.RED +'Password Copied to Clipboard')
    print(Style.RESET_ALL)
    details.detail()