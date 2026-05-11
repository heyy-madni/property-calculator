#  Property Investment Calculator
#* made by: Madni abid khan
#*email: madnikhan.work@gmail.com
#*whatapp: +91 90997 16001





#! imports
from random import randrange
import common_utils as utils
import terminal_colors as colors
import analysis_engine as analysis
from user_input import  get_data
from terminal_report_generator import show_terminal_report
import agreement_manager  as agreement_mod
from pdf_report_library import view_previous_pdfs
from pdf_report_generator import generate_property_report
import financial_calculations as financials

test_data = {
    "price": 5000000,
    "loan_amount": 3000000,
    "rent": 25000,
    "emi": 15000,
    "locality_quality": 8,
    "future_development": 7,
    "rental_demand": 8,
    "political_stability": 9,
    "cash_invested": 2000000,
    "appreciation": 0.05,
    "rent_growth": 0.03,
    "vacancy_rate": 0.1,
    "maintenance_annual": 12000
}
def generate_random_data():
    return {
        "price": randrange(1000000, 10000000, 500000),
        "loan_amount": randrange(500000, 7000000, 500000),
        "rent": randrange(5000, 50000, 5000),
        "emi": randrange(5000, 40000, 5000),
        "locality_quality": randrange(1, 11),
        "future_development": randrange(1, 11),
        "rental_demand": randrange(1, 11),
        "political_stability": randrange(1, 11),
        "cash_invested": randrange(500000, 7000000, 500000),
        "appreciation": randrange(1, 11) / 100,
        "rent_growth": randrange(1, 11) / 100,
        "vacancy_rate": randrange(0, 11) / 100,
        "maintenance_annual": randrange(5000, 20000, 1000)
    }


#! Main Program


def main():

    utils.create_log_of_this_session()
    utils.clear_console()
    utils.print_creator_info()
    agreement_mod.show_greeting()

    #! Agreement handling
    if agreement_mod.check_agreement():
        print(f"{colors.LIGHT_GREEN}\nYou have already accepted the agreement.{colors.RESET}")
    else:
        print(f"{colors.LIGHT_YELLOW}\nYou have not accepted the User Agreement.{colors.RESET}")
        if agreement_mod.agreement():
            agreement_mod.save_agreement()
        else:
            print(f"{colors.RED}\nYou did not accept the agreement. Exiting.{colors.RESET}")
            return

    #! Main menu loop
    while True:

        print("\n --- Property Investment Calculator ---\n")
        print("1. New Calculation")
        print("2. View Previous Reports")
        print("3. Use Inbuilt Test Data")
        print("4. Use Random Generated Data")
        print("5. Exit")

        menu_choice = input("Choose option: ").strip()
        utils.clear_console()

        #* Exit
        if menu_choice == "5":
            print("Exiting program. Goodbye!")
            break

        #* View previous
        if menu_choice == "2":
            view_previous_pdfs()
            continue

        #* Data selection
        if menu_choice == "3":
            data_source = test_data
            print("Using Inbuilt Test Data.")

        elif menu_choice == "4":
            data_source = generate_random_data()
            print("Using Random Generated Data.")
            print(data_source)

        elif menu_choice == "1":
            data_tuple = get_data()
            keys = list(test_data.keys())
            data_source = dict(zip(keys, data_tuple))

        else:
            print("Invalid choice.")
            continue

        
        #! Calculations start here
        

        price = data_source["price"]
        loan_amount = data_source["loan_amount"]
        rent = data_source["rent"]
        emi = data_source["emi"]
        locality_quality = data_source["locality_quality"]
        future_development = data_source["future_development"]
        rental_demand = data_source["rental_demand"]
        political_stability = data_source["political_stability"]
        cash_invested = data_source["cash_invested"]
        appreciation = data_source["appreciation"]
        rent_growth = data_source["rent_growth"]
        vacancy_rate = data_source["vacancy_rate"]
        maintenance_annual = data_source["maintenance_annual"]

        effective_rent = rent * (1 - vacancy_rate)
        vacancy_loss = rent * 12 * vacancy_rate
        cashflow = financials.calculate_cashflow(effective_rent, emi, maintenance_annual)
        annual_cashflow = financials.calculate_annual_cashflow(cashflow)
        rental_yield = financials.calculate_rental_yield(effective_rent, price)
        ltv = financials.calculate_ltv(loan_amount, price)


        net_annual_cashflow = annual_cashflow - maintenance_annual - vacancy_loss
        real_roi = (net_annual_cashflow / cash_invested * 100) if cash_invested > 0 else 0
        rent_to_emi_coverage = (effective_rent / emi * 100) if emi > 0 else 0
        future_value = financials.calculate_future_value(price, appreciation)
        future_rent = financials.calculate_future_rent(effective_rent, rent_growth)

        location_score = (
            locality_quality +
            future_development +
            rental_demand +
            political_stability
        ) / 4

        decision, score = analysis.calculate_score(
            real_roi=real_roi,
            cashflow=cashflow,
            rent_to_emi_coverage=rent_to_emi_coverage,
            ltv=ltv,
            location_score=location_score
        )

        risk_score, risklabel, risk_reasons = financials.risk_check(
            location_score=location_score,
            ltv=ltv,
            real_roi=real_roi,
            vacancy_loss=vacancy_loss,
            rent_to_emi_coverage=rent_to_emi_coverage,
            cashflow=cashflow
        )

        deal_type = analysis.classify_deal(
            cashflow,
            real_roi,
            rental_yield,
            future_value,
            risk_score
        )

        giveinsight = analysis.get_Insight(
            cashflow,
            real_roi,
            rental_yield,
            vacancy_loss,
            ltv,
            rent_to_emi_coverage,
            location_score
        )

        
        #! output selection
        

        while True:
            choice = input("\nGenerate PDF or Terminal report? (PDF / TER): ").strip().lower()

            if choice == "pdf":
                utils.clear_console()
                utils.loading_bar()
                generate_property_report(
                    price=price,
                    cashflow=cashflow,
                    annual_cashflow=annual_cashflow,
                    net_annual_cashflow=net_annual_cashflow,
                    real_roi=real_roi,
                    rental_yield=rental_yield,
                    ltv=ltv,
                    future_value=future_value,
                    future_rent=future_rent,
                    location_score=location_score,
                    risk_score=risk_score,
                    risk_label=risklabel,
                    reasons=risk_reasons,
                    decision=decision,
                    score=score,
                    deal_type=deal_type,
                    insights=giveinsight
                )
                break

            elif choice == "ter":
                utils.clear_console()
                utils.loading_bar()
                show_terminal_report(
                    price=price,
                    cashflow=cashflow,
                    annual_cashflow=annual_cashflow,
                    net_annual_cashflow=net_annual_cashflow,
                    real_roi=real_roi,
                    rental_yield=rental_yield,
                    ltv=ltv,
                    future_value=future_value,
                    future_rent=future_rent,
                    location_score=location_score,
                    risk=risk_score,
                    risklabel=risklabel,
                    reasons=risk_reasons,
                    decision=decision,
                    score=score,
                    deal_type=deal_type,
                    insight=giveinsight,
                    effective_rent=effective_rent
                )
                break

            else:
                print("Invalid choice.")
        








#! run program 
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"{colors.RED}An error occurred: {e}{colors.RESET}")







