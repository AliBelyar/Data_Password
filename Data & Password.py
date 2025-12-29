import sys
from colorama import Fore, Style, init
init(autoreset = True)
print(Fore.YELLOW + "Answer only with (y/n)!")
print("")
b1 = input(Fore.MAGENTA + "Do you want watch Data? " + Fore.CYAN)
if b1 == "n":
	sys.exit()
elif b1 != "y" and b1 != "n":
	print("")
	print(Fore.RED + "Error!")
	sys.exit()
print("")
print(Fore.MAGENTA + "For watching Data, You have to enter Password!")
b2 = input(Fore.MAGENTA + "Do you want to Continue? " + Fore.CYAN)
if b2 == "n":
	sys.exit()
elif b2 != "y" and b2 !="n":
	print("")
	print(Fore.RED + "Error!")
	sys.exit()
print("")
a = input(Fore.CYAN + "Enter Password: " + Fore.GREEN)
pw = "Python2025"
i = 5
while pw != a:
	print(Fore.RED + "Incorrect!")
	if i == 1:
		a = input(Fore.CYAN + f"Try Again (Last Chances!): " + Fore.GREEN)
	else:
		a = input(Fore.CYAN + f"Try Again ({i} Chances!): " + Fore.
		GREEN)
	i = i - 1
	if i == 0:
		break
if a == pw:
	print(Fore.GREEN + "Correct.")
else:
	print(Fore.RED + "Sorry, You can't watch Data!")
	sys.exit()
print("")
print(Fore.CYAN + "Data: " + Fore.YELLOW + "There's no Data... (>.<)")