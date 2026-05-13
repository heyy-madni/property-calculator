import utils.common_utils as utils #type: ignore


def get_float(prompt):
    try:
        return float(input(prompt))
    except ValueError:
        print(utils.RED + "Please enter a valid number.")

def get_financial_data():
    price = get_float(utils.PINK + "Enter property price (₹): ")

    if price <= 0:#type: ignore
        print(utils.RED + "Price must be greater than zero.")
        return get_financial_data()

    loan_amount = get_float(utils.PINK + "Enter loan amount (₹): ")

    if loan_amount < 0 or loan_amount > price:#type: ignore
        print(utils.RED + "Invalid loan amount.")
        return get_financial_data()

    if loan_amount == 0:
        emi = 0
        cash_invested = price

    else:
        cash_invested = get_float(utils.PINK + "Enter total cash invested (₹): ")
        emi = get_float(utils.PINK + "Enter monthly EMI (₹): ")

        if emi < 0:#type: ignore
            print(utils.RED + "You have entered an invalid EMI.")
            return get_financial_data()

    rent = get_float(utils.PINK + "Enter monthly rent (₹): ")

    if rent <= 0:#type: ignore
        print(utils.RED + "Rent must be greater than zero.")
        return get_financial_data()

    maintenance_annual = get_float(utils.PINK + "Annual maintenance cost (₹): ")

    return {
        "price": price,
        "loan_amount": loan_amount,
        "emi": emi,
        "cash_invested": cash_invested,
        "rent": rent,
        "maintenance_annual": maintenance_annual
    }

def get_area_quality_data():
    def spcore(prompt):
        try:
            score = float(input(prompt))
            if 1 <= score <= 10:
                return score
            else:
                print(utils.RED + "Score must be between 1 and 10.")
                return spcore(prompt)
        except ValueError:
            print(utils.RED + "Please enter a valid number.")
            return spcore(prompt)

    locality_quality = spcore("Rate location (1-10): ")
    future_development = spcore("Future development (1-10): ")
    rental_demand = spcore("Rental demand (1-10): ")
    political_stability = spcore("Political stability (1-10): ")


    return {
        "locality_quality": locality_quality,
        "future_development": future_development,
        "rental_demand": rental_demand,
        "political_stability": political_stability
    }

def get_growth_data():

    appreciation = get_float(utils.PINK + "Expected appreciation: ")
    rent_growth = get_float(utils.PINK + "Expected rent growth: ")
    vacancy_rate = get_float(utils.PINK + "Vacancy rate: ")

    if vacancy_rate < 0 or vacancy_rate >= 100: #type: ignore
        print(utils.RED + "Invalid vacancy rate.")
        return get_growth_data()

    return {
        "appreciation": appreciation,
        "rent_growth": rent_growth,
        "vacancy_rate": vacancy_rate
    }


def get_data():

    financial = get_financial_data()
    area = get_area_quality_data()
    growth = get_growth_data()

    data = {
        **financial,
        **area,
        **growth
    }

    return data