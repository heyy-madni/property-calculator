import core.financial_calculations as financials #type:ignore 
import core.analysis_engine as analysis #type:ignore 



def analyze_property(data):

    effective_rent = data["rent"] * (1 - data["vacancy_rate"])

    vacancy_loss = (
        data["rent"] * 12 * data["vacancy_rate"]
    )

    cashflow = financials.calculate_cashflow(
        effective_rent,
        data["emi"],
        data["maintenance_annual"]
    )

    annual_cashflow = financials.calculate_annual_cashflow(cashflow)

    rental_yield = financials.calculate_rental_yield(
        effective_rent,
        data["price"]
    )

    ltv = financials.calculate_ltv(
        data["loan_amount"],
        data["price"]
    )

    net_annual_cashflow = (
        annual_cashflow
        - data["maintenance_annual"]
        - vacancy_loss
    )

    real_roi = (
        net_annual_cashflow / data["cash_invested"] * 100
        if data["cash_invested"] > 0
        else 0
    )

    rent_to_emi_coverage = (
        effective_rent / data["emi"] * 100
        if data["emi"] > 0
        else 0
    )

    future_value = financials.calculate_future_value(
        data["price"],
        data["appreciation"]
    )

    future_rent = financials.calculate_future_rent(
        effective_rent,
        data["rent_growth"]
    )

    location_score = (
        data["locality_quality"]
        + data["future_development"]
        + data["rental_demand"]
        + data["political_stability"]
    ) / 4

    decision, score = analysis.calculate_score(
        real_roi=real_roi,
        cashflow=cashflow,
        rent_to_emi_coverage=rent_to_emi_coverage,
        ltv=ltv,
        location_score=location_score
    )

    risk_score, risk_label, risk_reasons = financials.risk_check(
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

    insight = analysis.get_Insight(
        cashflow,
        real_roi,
        rental_yield,
        vacancy_loss,
        ltv,
        rent_to_emi_coverage,
        location_score
    )

    return {
        "price": data["price"],
        "effective_rent": effective_rent,
        "cashflow": cashflow,
        "annual_cashflow": annual_cashflow,
        "net_annual_cashflow": net_annual_cashflow,
        "real_roi": real_roi,
        "rental_yield": rental_yield,
        "ltv": ltv,
        "future_value": future_value,
        "future_rent": future_rent,
        "location_score": location_score,
        "risk_score": risk_score,
        "risk_label": risk_label,
        "risk_reasons": risk_reasons,
        "decision": decision,
        "score": score,
        "deal_type": deal_type,
        "insight": insight
    }