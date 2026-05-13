#import
import sys
import subprocess
from utils.paths import PDF_DIR #type: ignore
from utils.common_utils import clear_console#type: ignore


def open_file(path):
    if sys.platform == "win32":
        from os import startfile
        startfile(path)
    elif sys.platform == "darwin":
        subprocess.run(["open", str(path)])
    else:
        subprocess.run(["xdg-open", str(path)])
    

def view_previous_pdfs():
    if not PDF_DIR.exists():
        print("No previous reports found.")
        return

    pdf_files = sorted(PDF_DIR.glob("*.pdf"))

    if not pdf_files:
        print("No previous reports found.")
        return

    print("\nPrevious Property Reports:\n")

    for index, pdf in enumerate(pdf_files, start=1):
        print(f"{index}. {pdf.name}")

    choice = input("\nEnter report number to open (or press Enter to cancel): ").strip()

    if choice == "":
        clear_console()
        return

    if not choice.isdigit():
        print("Invalid input.")
        return

    choice = int(choice)

    if choice < 1 or choice > len(pdf_files):
        print("Invalid report number.")
        return

    open_file(pdf_files[choice - 1])



    