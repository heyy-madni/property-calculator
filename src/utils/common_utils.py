from colorama import Fore, Style, init
from time import sleep 
import os , sys
#* //////////////////////////

#* COLOURS & STYLE
init(autoreset=True)
RED = Fore.RED
GREEN = Fore.GREEN
WHITE = Fore.LIGHTWHITE_EX
YELLOW = Fore.YELLOW
BLUE = Fore.BLUE
CYAN = Fore.CYAN
PINK=Fore.LIGHTMAGENTA_EX
GRAY=Fore.LIGHTBLACK_EX
LIGHT_GREEN=Fore.LIGHTGREEN_EX
LIGHT_YELLOW=Fore.LIGHTYELLOW_EX
LIGHT_CYAN=Fore.LIGHTCYAN_EX

RESET = Style.RESET_ALL
BOLD = Style.BRIGHT
DIM = Style.DIM



#* //////////////////////////
# loading bar

def loading_bar():
    for i in range(10):
        print(f"\rLoading... {i+1}/10", end="")
        sleep(0.5)
    print("\rLoading... Done!          ")

#* //////////////////////////
# clear console

def clear_console(sleep_time=0):

    sleep(sleep_time)
    os.system('cls' if os.name == 'nt' else 'clear')

#* //////////////////////////
def type_text(text, typing_speed=0.1, writer=None):
    if writer is None:
        writer = sys.stdout

    for char in text:
        writer.write(char)
        writer.flush()
        sleep(typing_speed)

#* //////////////////////////
def print_creator_info():
    print(f"""{LIGHT_CYAN}{BOLD}
 Property Investment Calculator
 made by: Madni abid khan
 email: madnikhan.work@gmail.com,
        abidkhan1983@gmail.com
 whatapp: +91 90997 16001
""")