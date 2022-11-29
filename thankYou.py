import sys
from termcolor import cprint 
from pyfiglet import figlet_format

def thank_you():
    cprint(figlet_format('Thanks for using :)', font='starwars'),'yellow', 'on_red', attrs=['bold'])
    return