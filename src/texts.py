from colorama import Fore, Back

optionsText = """ ------------------ Available Move Options ---------------------
|   { n } North | { s } South |  { w } West | { e } East        |
|                                                               |
 ------------------- Other Options -----------------------------
|   { get 'item name' } | { take 'item name' } To carry an item |
|                                                               |
 --------------- { Q } to Exit the Adventure -------------------"""

selectOptionText = Back.BLACK + Fore.YELLOW + \
    "Select an option >>>" + Back.RESET + Fore.WHITE + " "

playerNameText = Back.BLACK + Fore.YELLOW + \
    "Enter Your character name to get started >>>" + Back.RESET + Fore.WHITE + " "

welcomeMessage = Back.RESET + Fore.GREEN + \
    "\n****** WELCOME TO THE GREAT ADVENTURE GAME *********\n"


playerWinsText = Fore.BLACK + Back.GREEN + \
    "\n*** Congrats, you made it to the Treasure room. All the left items are yours. ***\n"
