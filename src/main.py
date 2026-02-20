#  Property Investment Calculator
#* made by: Madni abid khan
#*email: madnikhan.work@gmail.com
#*whatapp: +91 90997 16001


# print you already accepted agreement if accepted before


#!imports

from common_utils import loading_bar, clear_console , create_log_of_this_session ,print_creator_info
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




#! Main Program


def main():

    create_log_of_this_session()

    clear_console()

    print_creator_info()

    show_greeting()

    
    #! agreement handling
    

    if not check_agreement():
        print("You have not accepted the User Agreement.")
        accepted = agreement()
        if accepted:
            save_agreement()
        else:
            print("You did not accept the agreement. Exiting.")
            return



    
    #! Main Menu
    

    while True:
        print("\n🏠 --- Property Investment Calculator ---\n")
        print("1. New Calculation")
        print("2. View Previous Reports")
        print("3. Exit")

        menu_choice = input("Choose option: ").strip()
        clear_console()


        if menu_choice == "2":
            view_previous_pdfs()
            clear_console()
            continue

        if menu_choice == "3":
            print("Exiting program. Goodbye!")
            return

        if menu_choice != "1":
            print("Invalid choice.")
            continue

        
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
        

        cashflow = calculate_cashflow(rent, emi)

        annual_cashflow = calculate_annual_cashflow(cashflow)

        rental_yield = calculate_rental_yield(rent, price)

        ltv = calculate_ltv(loan_amount, price)

        vacancy_loss = rent * 12 * vacancy_rate



        net_annual_cashflow = annual_cashflow - maintenance_annual - vacancy_loss 

        real_roi = (net_annual_cashflow / cash_invested * 100) if cash_invested > 0 else 0

        rent_to_emi_coverage = (rent / emi * 100) if emi > 0 else 0

        future_value = calculate_future_value(price, appreciation)

        future_rent = calculate_future_rent(rent, rent_growth)

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
                
                )
                break

            print("Invalid choice.")








#! run program 
if __name__ == "__main__":
    main()







