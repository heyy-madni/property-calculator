#import
from paths import PDF_DIR
from os import startfile



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
        return

    if not choice.isdigit():
        print("Invalid input.")
        return

    choice = int(choice)

    if choice < 1 or choice > len(pdf_files):
        print("Invalid report number.")
        return

    startfile(pdf_files[choice - 1])