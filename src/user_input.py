#import


from terminal_colors import RED,  PINK, RESET

#! ---------- FLOAT INPUT FUNCTION ----------
def get_float(prompt):
    """Safely gets float input from user."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")



#! ---------- INPUT DATA FUNCTION ----------
def get_data():



    price = get_float(PINK + "\nEnter property price (₹): " + RESET)
    if price <=0:
        print(RED + "Price must be greater than zero. Please re-enter the data." + RESET)
        return get_data()



    loan_amount = get_float(PINK + "Enter loan amount (₹): " + RESET)
    if loan_amount <0 or loan_amount > price:
        print(RED + "Loan amount must be between 0 and the property price. Please re-enter the data." + RESET)
        return get_data()

    elif loan_amount == 0:
        emi = 0
        cash_invested = price

    else:
        cash_invested = get_float(
            PINK + "Enter your total cash invested (₹): " + RESET)
        emi = get_float(PINK + "Enter monthly EMI (₹): " + RESET)
        if emi <0:
         print(RED + "EMI cannot be negative, EMI can be zero. Please re-enter the data. " + RESET)
        return get_data()



    rent = get_float(PINK + "Enter monthly rent (₹): " + RESET)
    if rent <=0:
        print(RED + "Rent must be greater than zero. Please re-enter the data." + RESET)
        return get_data()



    locality_quality = get_float(PINK + "Rate the location (1-10) " + RESET)
    if locality_quality <1 or locality_quality >10:
        print(RED + "Location score must be between 1 and 10. Please re-enter the data." + RESET)
        return get_data()



    future_development = get_float(PINK + "Rate future development potential (1-10) " + RESET)
    if future_development <1 or future_development >10:
        print(RED + "Location score must be between 1 and 10. Please re-enter the data." + RESET)
        return get_data()



    rental_demand = get_float(PINK + "Rate rental demand (1-10) " + RESET)
    if rental_demand <1 or rental_demand >10:
        print(RED + "Location score must be between 1 and 10. Please re-enter the data." + RESET)
        return get_data()



    political_stability = get_float(PINK + "Rate political stability (1-10) " + RESET)
    if political_stability <1 or political_stability >10:
        print(RED + "Location score must be between 1 and 10. Please re-enter the data." + RESET)
        return get_data()



    appreciation = get_float(PINK + "Expected annual appreciation (e.g., 0.05 for 5%): " + RESET)

    rent_growth = get_float(PINK + "Expected annual rent growth (e.g., 0.03 for 3%): " + RESET)

    vacancy_rate = get_float(PINK + "Expected vacancy rate (e.g., 0.08 for 8%): " + RESET)
    if vacancy_rate <0 or vacancy_rate >=100:
        print(RED + "Vacancy rate must be between 0 and 100. Please re-enter the data." + RESET)
        return get_data()
    
    maintenance_annual = get_float(PINK + "Annual maintenance cost (₹): " + RESET)


    return (
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

)


