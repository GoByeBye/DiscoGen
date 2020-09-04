import random
import string
from colorama import Fore, init
import os
from tqdm import tqdm

__author__ = "Daddie#1337"
__version__ = "1.0.1"
__tag__ = """

██████╗ ██╗███████╗ ██████╗ ██████╗  ██████╗ ███████╗███╗   ██╗
██╔══██╗██║██╔════╝██╔════╝██╔═══██╗██╔════╝ ██╔════╝████╗  ██║
██║  ██║██║███████╗██║     ██║   ██║██║  ███╗█████╗  ██╔██╗ ██║
██║  ██║██║╚════██║██║     ██║   ██║██║   ██║██╔══╝  ██║╚██╗██║
██████╔╝██║███████║╚██████╗╚██████╔╝╚██████╔╝███████╗██║ ╚████║
╚═════╝ ╚═╝╚══════╝ ╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝╚═╝  ╚═══╝

"""
# Cross platform clear
def cls():
    os.system("cls" if os.name == "nt" else "clear")


cls()

# Logo
print(
    f"{Fore.CYAN}{__tag__}                                                  {Fore.GREEN}Version {Fore.CYAN}>{Fore.WHITE} {__version__}\n                                                  {Fore.GREEN}Made by {Fore.CYAN}>{Fore.WHITE} {__author__}"
)
# User options
amount = int(input("How many codes do you want to generate?\n> "))

for i in tqdm (range(amount), desc="Making codes..."):
    try:
        # Gen code
        code = "https://discord.gift/" + ("").join(
            random.choices(string.ascii_letters + string.digits, k=16)
        )

        # Make/Edit file for all codes
        f = open("codes.txt", "a+")
        f.write(f"{code}\n")
        f.close()

        # Add to value so we don't waste time
        value += 1
    except Exception as e:
        print(f"{Fore.RED}GEN [-] ERROR:\n>{Fore.WHITE}{e}")

print(f"{Fore.WHITE}Finished generating codes :)")
