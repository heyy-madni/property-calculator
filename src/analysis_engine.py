#impots
#No external imports


#! calculate_score
def calculate_score_cashflow(cashflow):
    score = 0
    # Cashflow rules
    if cashflow > 5000:
        score += 2
    elif cashflow > 1000:
        score += 1
    elif cashflow <= 0:
        score -= 3
    return score


def calculate_score_real_roi(real_roi):
    score = 0
    # ROI rules
    if real_roi > 8:
        score += 3
    elif real_roi > 5:
        score += 2
    elif real_roi > 2:
        score += 1
    else:
        score -= 2
    return score

def calculate_score_location(location_score):
    score = 0
    # LOCATION rules
    if location_score >= 8:
        score += 2
    elif location_score >= 5:
        score += 1
    elif location_score > 3:
        score -= 1
    else:
        score -= 2
    return score


def calculate_score_rental_yield(rental_yield):
    score = 0
    if rental_yield > 3:
        score += 2
    elif rental_yield > 2:
        score += 1
    elif rental_yield < 2:
        score -= 2
    return score
def calculate_score_ltv(ltv):
    score = 0
    if ltv > 80:
        score -= 2
    elif ltv < 60:
        score += 1
    return score

def calculate_score_rent_to_emi(rent_to_emi_coverage):
    score = 0
    if rent_to_emi_coverage >= 100:
        score += 2
    elif rent_to_emi_coverage <= 90:
        score += 1
    elif rent_to_emi_coverage < 70:
        score -= 1
    elif rent_to_emi_coverage < 60:
        score -= 2
    return score
#& this is decision that use score
def make_decision(score):
    if score >= 8:
        return "Excellent Deal. Buy Immediately"
    elif score >= 5:
        return "Strong Deal. Negotiate and Buy"
    elif score >= 2:
        return "Good Deal. Think Before Proceeding"
    elif score >= -1:
        return "Borderline. Needs More Analysis"
    elif score >= -5:
        return "Weak Deal. Avoid If Possible"
    else:
        return "Terrible Deal. Walk Away"

def calculate_score(
    real_roi,
    cashflow,
    rent_to_emi_coverage,
    ltv,
    location_score
):
    score = 0
    score += calculate_score_real_roi(real_roi)
    score += calculate_score_cashflow(cashflow)
    score += calculate_score_rent_to_emi(rent_to_emi_coverage)
    score += calculate_score_ltv(ltv)
    score += calculate_score_location(location_score)
    decision = make_decision(score)
    return decision,score

#! Insight section
def Insight_cashflow(cashflow):
    if cashflow < 0:
        return "Cash flow is negative. Operating expenses exceed rental income."
    elif cashflow < 1000:
        return "Cash flow is weak. Small changes in income or expenses can impact sustainability."
    elif cashflow < 2000:
        return "Cash flow is positive but limited. Financial margin is narrow."
    else:
        return "Cash flow is stable. Rental income comfortably exceeds expenses."


def Insight_roi(real_roi):
    if real_roi < 4:
        return "ROI is below inflation-adjusted benchmarks. Real purchasing power declines over time."
    elif real_roi < 6:
        return "ROI is moderate. Returns are sensitive to holding period and exit price."
    else:
        return "ROI is high relative to conservative benchmarks."


def Insight_rental_yield(rental_yield):
    if rental_yield < 2:
        return "Rental yield is low. Returns rely primarily on non-rental factors."
    elif rental_yield < 3:
        return "Rental yield is moderate. Cash flow contribution is limited."
    else:
        return "Rental yield is strong relative to typical residential ranges."


def Insight_vacancy_loss(vacancy_loss):
    # VACANCY BASED INSIGHT
    if vacancy_loss > 10:
        return "Vacancy impact is high. Rental income shows significant interruption risk."
    elif vacancy_loss > 5:
        return "Vacancy impact is moderate. Income variability is present."
    else:
        return "Vacancy impact is low. Rental income appears consistent."


def Insight_ltv(ltv):
    if ltv > 80:
        return "Loan-to-value ratio is high. Leverage exposure is elevated."
    elif ltv > 70:
        return "Loan-to-value ratio is moderately high. Debt sensitivity exists."
    else:
        return "Loan-to-value ratio is conservative."


def Insight_rent_to_emi_coverage(rent_to_emi_coverage):
    if rent_to_emi_coverage < 70:
        return "Rent covers a small portion of EMI. External cash dependency is high."
    elif rent_to_emi_coverage < 90:
        return "Rent covers most of the EMI. Partial income support is required."
    else:
        return "Rent sufficiently covers EMI obligations."


def Insight_location_score(location_score):
    # LOCATION INSIGHT
    if location_score < 4:
        return "Location score is low based on selected parameters."
    elif location_score < 6:
        return "Location score is average within the evaluated range."
    else:
        return "Location score is high relative to the defined criteria."


def get_Insight(
    cashflow,
    real_roi,
    rental_yield,
    vacancy_loss,
    ltv,
    rent_to_emi_coverage,
    location_score
):
    output = []
    output.append(Insight_cashflow(cashflow))
    output.append(Insight_roi(real_roi))
    output.append(Insight_rental_yield(rental_yield))
    output.append(Insight_vacancy_loss(vacancy_loss))
    output.append(Insight_rent_to_emi_coverage(rent_to_emi_coverage))
    output.append(Insight_ltv(ltv))
    output.append(Insight_location_score(location_score))
    return output








def classify_deal(cashflow, real_roi, rental_yield, future_value_growth, risk):
    """
    future_value_growth = % appreciation per year (ex: 6 = 6%)
    risk = risk score from risk module
    """

    # 1. CASHFLOW DEAL
    if cashflow > 2500 and rental_yield >= 3 and real_roi >= 6:
        return "Cashflow Deal"

    # 2. APPRECIATION DEAL
    if cashflow < 1500 and rental_yield < 2.5 and future_value_growth >= 6:
        return "Appreciation Deal"

    # 3. BALANCED DEAL
    if cashflow >= 1500 and real_roi >= 4 and rental_yield >= 2.5:
        return "Balanced Deal"

    # 4. SPECULATIVE DEAL
    if future_value_growth >= 8 and risk >= 6:
        return "Speculative Deal"

    # 5. RISKY DEAL
    if risk >= 8:
        return "Risky Deal"

    # 6. TRASH DEAL (everything weak)
    if cashflow < 0 and real_roi < 3 and rental_yield < 2:
        return "Trash Deal"

    # DEFAULT
    return "Neutral / Hard to classify"


def Price_sensitivity(price, score):

    if score >= 7:
        return f" ₹{price}, deal metrics remain aligned with the evaluated score."
    
    elif score >= 6:
        return f" ₹{price}, deal metrics show mild sensitivity to pricing assumptions."
    
    elif score >= 5:
        return f" ₹{price}, returns are sensitive to small variations in entry price."
    
    elif score >= 4:
        return f" ₹{price}, returns show high sensitivity to entry price and assumptions."
    
    elif score >= 3:
        return f" ₹{price}, financial margins are thin and pricing sensitivity is elevated."
    
    else:
        return f" ₹{price}, deal viability is highly dependent on favorable pricing conditions."



SURAT_BENCHMARKS = {
    "rental_yield": 2.4,
    "appreciation": 7.0,
    "vacancy": 4,
    "ideal_ltv": 60,
    "ideal_emi_coverage": 80,
    "ideal_roi_min": 6,
    "ideal_roi_max": 10
}

def compare_to_benchmark(value, benchmark, higher_is_better=True):
    if higher_is_better:
        if value > benchmark:
            return "above"
        elif value == benchmark:
            return "equal"
        else:
            return "below"
    else:
        if value < benchmark:
            return "above"
        elif value == benchmark:
            return "equal"
        else:
            return "below"



