#  Property Investment Calculator
#* made by: Madni abid khan
#*email: madnikhan.work@gmail.com
#*whatapp: +91 90997 16001


# print you already accepted agreement if accepted before


#!imports
from random import randrange
from common_utils import loading_bar, clear_console , create_log_of_this_session ,print_creator_info
from terminal_colors import RED, GREEN, YELLOW, WHITE, CYAN, PINK, LIGHT_CYAN, LIGHT_YELLOW, LIGHT_GREEN, RESET, BOLD
from analysis_engine import calculate_score, get_Insight, classify_deal 
from user_input import  get_data
from terminal_report_generator import show_terminal_report
from agreement_manager import agreement, show_greeting,check_agreement,save_agreement
from pdf_report_library import view_previous_pdfs
from pdf_report_generator import generate_property_report
from financial_calculations import (
    calculate_cashflow,
    calculate_annual_cashflow,
    calculate_rental_yield,
    calculate_ltv,
    calculate_future_value,
    calculate_future_rent,
    risk_check
    )
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
random_used_data = {"price": randrange(1000000, 10000000, 500000),
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
                    "maintenance_annual": randrange(5000, 20000, 1000)}


#! Main Program


def main():

    create_log_of_this_session()

    clear_console()

    print_creator_info()

    show_greeting()

    
    #! agreement handling
    

    if check_agreement():
        print(f"{LIGHT_GREEN}\nYou have already accepted the agreement.{RESET}")
    else:
        print(f"{LIGHT_YELLOW}\nYou have not accepted the User Agreement.{RESET}")
        accepted = agreement()

        if accepted:
            save_agreement()
        else:
            print(f"{RED}\nYou did not accept the agreement. Exiting.{RESET}")
            return



    
    #! Main Menu
    

    while True:
        try:
            print("\n🏠 --- Property Investment Calculator ---\n")
            print("1. New Calculation")
            print("2. View Previous Reports")
            print("3. use inbuilt test data")
            print("4. use random used data")
            print("5. Exit")

            menu_choice = input("Choose option: ").strip()
            clear_console()


            if menu_choice == "5":
                print("Exiting program. Goodbye!")
                return

            elif menu_choice == "2":
                view_previous_pdfs()

            elif menu_choice == "3":
                #! use inbuilt test data
                pass
            elif menu_choice == "4":
                #! use random used data
                pass

            elif menu_choice != "1":
                print("Invalid choice.")
                return

            elif menu_choice == "1":
                    #! Main Calculation
                   continue

        except Exception as e:
            print(f"{RED}An error occurred: {e}{RESET}")




        
        #! Get Inputs
        
        (
            price,
            loan_amount,
            rent,
            emi,
            locality_quality,
            future_development,
            rental_demand,
            political_stability,
            cash_invested,
            appreciation,
            rent_growth,
            vacancy_rate,
            maintenance_annual,

        ) = get_data()

        
        #! calculations
        
        effective_rent = rent * (1 - vacancy_rate)

        cashflow = calculate_cashflow(effective_rent, emi, maintenance_annual)

        annual_cashflow = calculate_annual_cashflow(cashflow)

        rental_yield = calculate_rental_yield(effective_rent, price)

        ltv = calculate_ltv(loan_amount, price)

        vacancy_loss = effective_rent * 12 * vacancy_rate



        net_annual_cashflow = annual_cashflow - maintenance_annual - vacancy_loss 

        real_roi = (net_annual_cashflow / cash_invested * 100) if cash_invested > 0 else 0

        rent_to_emi_coverage = (effective_rent / emi * 100) if emi > 0 else 0

        future_value = calculate_future_value(price, appreciation)

        future_rent = calculate_future_rent(effective_rent, rent_growth)

        location_score = (
            locality_quality +future_development +rental_demand +political_stability ) / 4


        
        #! decision & risk
        

        decision, score = calculate_score(
            real_roi=real_roi,
            cashflow=cashflow,
            rent_to_emi_coverage=rent_to_emi_coverage,
            ltv=ltv,
            location_score=location_score
        )


        risk_score, risklabel, risk_reasons = risk_check(
            location_score=location_score,
            ltv=ltv,
            real_roi=real_roi,
            vacancy_loss=vacancy_loss,
            rent_to_emi_coverage=rent_to_emi_coverage,
            cashflow=cashflow
        )


        deal_type = classify_deal(
            cashflow,
            real_roi,
            rental_yield,
            future_value,
            risk_score
        )


        giveinsight = get_Insight(
            cashflow,
            real_roi,
            rental_yield,
            vacancy_loss,
            ltv,
            rent_to_emi_coverage,
            location_score
        )




        #! output choice

        while True:
            choice = input("\nGenerate PDF or Terminal report? (PDF / TER): ").strip().lower()

            if choice == "pdf":
                clear_console()
                loading_bar()
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

            if choice == "ter":
                clear_console()
                loading_bar()
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

            print("Invalid choice.")








#! run program 
if __name__ == "__main__":
    main()







