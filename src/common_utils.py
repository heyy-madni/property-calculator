#import 
import sys
import os
import time
from datetime import datetime
from paths import LOG_FILE
from terminal_colors import LIGHT_CYAN, BOLD

def print_creator_info():
    print(f"""{LIGHT_CYAN}{BOLD}
 Property Investment Calculator
 made by: Madni abid khan
 email: madnikhan.work@gmail.com,
        abidkhan1983@gmail.com
 whatapp: +91 90997 16001
""")



#! ---------- LOG CREATION FUNCTION ----------
def create_log_of_this_session():
    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"START {timestamp}\n")


#!---loading bar---
def loading_bar():
    for i in range(10):
        print(f"\rLoading... {i+1}/10", end="")
        time.sleep(0.5)
    print("\rLoading... Done!          ")


#! ---------- CLEAR CONSOLE FUNCTION ----------
def clear_console():
    """Clears the console screen."""
    
    os.system('cls' if os.name == 'nt' else 'clear')


#! ---------- TYPING EFFECT ----------
TYPING_SPEED = 0.1 # seconds per character

def type_text(text, writer=None):
    NO_CONSOLE = getattr(sys, 'frozen', False)
    if NO_CONSOLE:
        print(text)
    

    if writer is None:
            writer = sys.stdout

    if writer is None:
        print(text)
        return

    for char in text:
        writer.write(char)
        writer.flush()