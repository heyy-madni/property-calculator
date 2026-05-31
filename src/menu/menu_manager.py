
import utils.common_utils as utils # type: ignore
import agreement.agreement_manager  as agreement_mod  # type: ignore
from reports.pdf_report import generate_property_report # type: ignore
from reports.terminal_report import  show_terminal_report # type: ignore
from data.data_sources import select_data_source # type: ignore
from core.property_analyzer import analyze_property # type: ignore





def setup_program():

    utils.clear_console()
    utils.print_creator_info()
    agreement_mod.show_greeting()



def handle_agreement():

    if agreement_mod.check_agreement():
        print(
            f"{utils.LIGHT_GREEN}\nAgreement already accepted.{utils.RESET}"
        )
        return True

    print(
        f"{utils.LIGHT_YELLOW}\nAgreement not accepted.{utils.RESET}"
    )

    if agreement_mod.agreement():
        agreement_mod.save_agreement()
        return True

    print(f"{utils.RED}\nAgreement rejected.{utils.RESET}")
    return False



def output_results(results):

    while True:

        choice = input(
            "\nGenerate PDF or Terminal report? (PDF / TER): "
        ).strip().lower()

        if choice == "pdf":
            generate_property_report(results)
            break

        elif choice == "ter":
            show_terminal_report(results)
            break

        else:
            print("Invalid choice")


def main():

    setup_program()

    if not handle_agreement():
        return

    while True:
        input("\nPress Enter to continue...")
        utils.clear_console()
        print("\n--- Property Investment Calculator ---\n")
        print("1. New Calculation")
        print("2. View Previous Reports")
        print("3. Use Inbuilt Test Data")
        print("4. Use Random Generated Data")
        print("5. Exit")

        choice = input("Choose option: ").strip()

        if choice == "5":
            print("Goodbye")
            break

        if choice == "2":
            from reports.pdf_report_library import view_previous_pdfs # type: ignore
            view_previous_pdfs()
            continue

        data = select_data_source(choice)

        if data is None:
            print("Invalid choice")
            continue

        results = analyze_property(data)

        output_results(results)


