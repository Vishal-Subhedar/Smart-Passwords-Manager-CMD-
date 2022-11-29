import re
import simplejson
import time
import details
from colorama import Fore,Back,Style
def grabJSON(s):
    FLAGS = re.VERBOSE | re.MULTILINE | re.DOTALL
    WHITESPACE = re.compile(r'[\t\n\r]*', FLAGS)
    decoder = simplejson.JSONDecoder()
    obj, end = decoder.raw_decode(s)
    end = WHITESPACE.match(s, end).end()
    return obj, s[end:]
def getDetails():
    platformName = input("Enter Platform Name: ")
    print(10*"*")
    with open("passwords.txt") as f:
        s = f.read()
    count = 0
    while True:
        obj, remaining = grabJSON(s)
        if obj['Platform Name'].upper() == platformName.upper() or obj['Platform Name'].lower() == platformName.lower():
            for key,value in obj.items():
                time.sleep(.2)
                print(key.upper() + " : " + value)
            print()
            count+=1
        s = remaining
        if not remaining.strip():
            break
    if count:
        if count == 1:
            print(Back.GREEN,count,"Entry Found !!!")
            print(Style.RESET_ALL)
        else:
            print(Back.GREEN,count,"Entries Found !!!")
            print(Style.RESET_ALL)
    else:
        print(Fore.RED,"No Entries Found !!!")
        print(Style.RESET_ALL)
    details.detail()
# getDetails()