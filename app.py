from colorama import Fore, Style, init

# initialize colorama
init(autoreset=True)

# define color variables

green = Fore.GREEN

yellow = Fore.YELLOW
reset = Style.RESET_ALL

# use them
print(red + "This is red text" + reset)
print(green + "This is green text" + reset)
print(blue + "This is blue text" + reset)
print(yellow + "This is yellow text" + reset)

# mixing styles
print(blue + Style.BRIGHT + "Bright Blue Text" + reset)

