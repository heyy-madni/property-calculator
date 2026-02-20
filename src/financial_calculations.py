# imports
# No external imports

# =========================
#! calculation
# =========================
#^cashflow
def calculate_cashflow(rent, emi):
    return rent - emi

#^annual cashflow
def calculate_annual_cashflow(cashflow):
    return cashflow * 12

#^roi
def calculate_roi(annual_cashflow, cash_invested):
    return (annual_cashflow / cash_invested * 100) if cash_invested > 0 else 0

#^rental yield
def calculate_rental_yield(rent, price):
    return (rent * 12 / price * 100) if price > 0 else 0

#^ltv
def calculate_ltv(loan_amount, price):
    return (loan_amount / price * 100) if price > 0 else 0

#^future value
def calculate_future_value(price, appreciation, years=5):
    return price * ((1 + appreciation) ** years)

#^future rent
def calculate_future_rent(rent, rent_growth, years=5):
    return rent * ((1 + rent_growth) ** years)



# =========================
#!risk module
# =========================

def calculate_risk_location(location_score):
    if location_score < 2:
        return 3, "Very Low Location Score"
    elif location_score < 4:
        return 2, "Low Location Score"
    elif location_score < 6:
        return 1, "Moderate Location Score"
    elif location_score > 8:
        return -2, "High Location Score"
    return 0, "Neutral Location Score"


def calculate_ltv_risk(ltv):
    if ltv > 80:
        return 2.5, "High Loan-to-Value Ratio"
    elif ltv > 70:
        return 1.5, "Elevated Loan-to-Value Ratio"
    elif ltv > 60:
        return 1, "Moderate Loan-to-Value Ratio"
    elif ltv < 50:
        return -1, "Low Loan-to-Value Ratio"
    return 0, "Neutral Loan-to-Value Ratio"


def calculate_real_roi_risk(real_roi):
    if real_roi < 2:
        return 3.5, "Very Low Real ROI"
    elif real_roi < 4:
        return 2, "Low Real ROI"
    elif real_roi < 6:
        return 1, "Moderate Real ROI"
    elif real_roi > 10:
        return -2, "High Real ROI"
    return 0, "Neutral Real ROI"

def calculate_vacancy_risk(vacancy_loss):
    if vacancy_loss > 10:
        return 3, "High Vacancy Loss"
    elif vacancy_loss > 7:
        return 2, "Moderate Vacancy Loss"
    elif vacancy_loss > 5:
        return 1, "Slightly Elevated Vacancy Loss"
    elif vacancy_loss < 2:
        return -1, "Low Vacancy Loss"
    return 0, "Neutral Vacancy Loss"


def calculate_rent_to_emi_coverage_risk(rent_to_emi_coverage):
    if rent_to_emi_coverage < 70:
        return 3, "Poor Rent to EMI Coverage"
    elif rent_to_emi_coverage < 80:
        return 2, "Below Average Rent to EMI Coverage"
    elif rent_to_emi_coverage < 90:
        return 1, "Slightly Low Rent to EMI Coverage"
    elif rent_to_emi_coverage > 120:
        return -1, "High Rent to EMI Coverage"
    elif rent_to_emi_coverage > 100:
        return -0.5, "Average Rent to EMI Coverage"
    return 0, "Neutral Rent to EMI Coverage"


def calculate_cashflow_risk(cashflow):
    if cashflow < 0:
        return 3, "Negative Cashflow"
    elif cashflow < 1000:
        return 2, "Low Cashflow"
    elif cashflow < 2000:
        return 1, "Moderate Cashflow"
    elif cashflow > 5000:
        return -1, "High Cashflow"
    return 0, "Neutral Cashflow"



def risk_check(location_score, ltv, real_roi, vacancy_loss, rent_to_emi_coverage, cashflow):
    risk = 0
    labels = []

    loc_risk, loc_label = calculate_risk_location(location_score)
    ltv_risk, ltv_label = calculate_ltv_risk(ltv)
    roi_risk, roi_label = calculate_real_roi_risk(real_roi)
    vac_risk, vac_label = calculate_vacancy_risk(vacancy_loss)
    cov_risk, cov_label = calculate_rent_to_emi_coverage_risk(rent_to_emi_coverage)
    cash_risk, cash_label = calculate_cashflow_risk(cashflow)

    risk += loc_risk + ltv_risk + roi_risk + vac_risk + cov_risk + cash_risk
    risk = max(risk, 0)

    labels.extend([
        loc_label, ltv_label, roi_label,
        vac_label, cov_label, cash_label
    ])

    if risk > 10:
        risk_label = "High Risk"
    elif risk > 6.5:
        risk_label = "Elevated Risk"
    elif risk > 5:
        risk_label = "Moderate Risk"
    elif risk > 3:
        risk_label = "Low to Moderate Risk"
    else:
        risk_label = "Low Risk"

    return risk, risk_label, labels
