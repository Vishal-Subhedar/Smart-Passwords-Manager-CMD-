import setDetails
import getDetails
import thankYou
from colorama import Back,Fore,Style

def detail():
    choice = input("type 'q' to quit else Enter s for set details or g for get details (s/g): ")
    if choice == "s":
        setDetails.saveDetails()
    elif choice == "g":
        getDetails.getDetails()
    elif choice == 'q':
        thankYou.thank_you()
    else:
        print(Fore.RED+"Warning : -------> Invalid Input <-------\n")
        print(Style.RESET_ALL)
        detail()


