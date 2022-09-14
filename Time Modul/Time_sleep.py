import time
from colorama import *
init()
# from playsound import *   

coloring = "Etwas"

def step_print(string): 
    print(string)   

    time.sleep(0.1)

while coloring != "3":
    step_print("")
    menu = """
        ["#", "#", "#", "#", "#", "#", "#", "#", "#",]
        ["#",                                    "#",]
        ["#",                                    "#",]
        ["#",                                    "#",]
        ["#",          "W E L C O M E",          "#",]
        ["#",                                    "#",]
        ["#",                                    "#",]
        ["#",                                    "#",]
        ["#", "#", "#", "#", "#", "#", "#", "#", "#",]
"""
      
    step_print("(1) RED-Menu1 (2) GREE-Menu2 (3) Exit")
    coloring = input("Choose: ") 

    
    if coloring == "1":
        step_print("")
        step_print(Fore.RED + menu + Fore.RESET)
    elif coloring == "2":
        step_print("")
        step_print(Fore.GREEN + menu + Fore.RESET)
    elif coloring == "3":
        step_print("")
        step_print(Fore.BLUE + "See you!" + Fore.RESET)
 