from random import randrange
from data.user_input import get_data #type:ignore


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


def select_data_source(choice):

    if choice == "1":
        return get_data()

    elif choice == "3":
        print("Using Inbuilt Test Data")
        return test_data

    elif choice == "4":
        data = generate_random_data()
        print("Using Random Generated Data")
        return data

    return None