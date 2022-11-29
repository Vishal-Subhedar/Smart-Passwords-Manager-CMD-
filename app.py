import auth
import time
from colorama import Back,Fore,Style
def welcome():
    welcome = "WELCOME TO SMART PASSWORD MANEGEMENT SYSTEM"
    for i in welcome:
        print(Fore.MAGENTA+i,end="")
        time.sleep(.1)
    print(Style.RESET_ALL)
    print("Enter Credentials to proceed further.........")
welcome()
auth.auth()