import os
import time
from colorama import Fore
from plugins.plate_search import plate
from plugins.ip_lookup import lookup


def main_menu():
    os.system("clear")

    print("""
    
    \033[1;32m░██████╗██╗░░██╗██╗██████╗░████████╗██████╗░░█████╗░░█████╗░███████╗██████╗░
    ██╔════╝██║░██╔╝██║██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
    ╚█████╗░█████═╝░██║██████╔╝░░░██║░░░██████╔╝███████║██║░░╚═╝█████╗░░██████╔╝
    ░╚═══██╗██╔═██╗░██║██╔═══╝░░░░██║░░░██╔══██╗██╔══██║██║░░██╗██╔══╝░░██╔══██╗
    ██████╔╝██║░╚██╗██║██║░░░░░░░░██║░░░██║░░██║██║░░██║╚█████╔╝███████╗██║░░██║
    ╚═════╝░╚═╝░░╚═╝╚═╝╚═╝░░░░░░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚══════╝╚═╝░░╚═╝
                                                            Coded By Samuel20354
    
    
1. Plate search
2. Sherlock
3. IP search
4. Exit
 -""")

    option = str(input("OPTION: "))

    if option == "1":
        plate()

    elif option == "2":
        print(" -")
        sherlock_username = input("Username to scan for: ")
        print("")
        os.system("clear")
        plugins = "plugins/"
        os.chdir(plugins)
        os.system("python3 sherlock.py " + sherlock_username)
        input(Fore.BLUE + "Press Enter to continue..." + Fore.RESET)
        main_menu()


    elif option == "3":
        lookup()

    elif option == "4":
        print(" -")
        print("Goodbye! [\033[0m\]")
        exit()

    else:
        print(" -")
        print("Invalid option, please try again.")
        print(" -")
        time.sleep(3)
        main_menu()


if __name__ == "__main__":
    main_menu()

main_menu()
