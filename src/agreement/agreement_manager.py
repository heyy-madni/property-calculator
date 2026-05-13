import os
import utils.common_utils as utils #type: ignore
from utils.paths import AGREEMENT_FILE #type: ignore
 


def check_agreement():
    if not os.path.exists(AGREEMENT_FILE):
        return False

    with open(AGREEMENT_FILE, "r") as file:
        return file.read().strip() == "True"


def save_agreement():
    with open(AGREEMENT_FILE, "w") as file:
        file.write("True")


def show_greeting():
    print("Welcome to the Property Investment Calculator!")
    print("Please read and accept the limitation agreement to continue.")
    input("Press Enter to view the agreement...")


def slowed_agreement_text():
    return (
        "\n⚠️ Property Investment Calculator – Disclaimer & Usage Scope ⚠️\n\n"
        "Before using this tool, you must read and accept the following terms:\n\n"
    )
def agreement_text():
    return (
        "\n⚠️ Property Investment Calculator – Disclaimer & Usage Scope ⚠️\n\n"
        "Before using this tool, you must read and accept the following terms:\n\n"
        "1. This calculator provides estimates based on user inputs and general assumptions. It is not a substitute for professional financial advice.\n"
        "2. The tool does not account for all variables such as market fluctuations, legal issues, or personal circumstances that may affect investment outcomes.\n"
        "3. Users should conduct their own due diligence and consult with qualified professionals before making any investment decisions.\n"
        "4. The creators of this tool are not liable for any financial losses or damages resulting from the use of this calculator.\n\n"
        "By typing 'agree', you acknowledge that you have read, understood, and accepted these terms."
    )

def agreement():
    while True:
        utils.type_text(slowed_agreement_text())
        print(agreement_text())
        choice = input(f"{utils.LIGHT_YELLOW}{utils.BOLD}\nType 'agree' to accept and continue: {utils.RESET}").strip().lower()
        if choice == "agree":
            utils.clear_console()
            return True
        utils.type_text(f"{utils.RED}You must type 'agree' to continue.{utils.RESET}")