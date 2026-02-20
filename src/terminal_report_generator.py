# imports

from terminal_colors import (
    # colours
    RED, 
    GREEN ,
    YELLOW ,
    WHITE,
    CYAN ,
    PINK,
    LIGHT_CYAN,
    LIGHT_YELLOW,
    LIGHT_GREEN,


    # syles
    RESET,
    BOLD,

    )



def decision_color(decision):
    return GREEN if decision == "buy" else RED if decision == "sell" else YELLOW


def print_header(title):
    print(RED + "\n" + "=" * 60)
    print(f"{WHITE}{BOLD}{title.center(60)}{RESET}")
    print(RED + "=" * 60 + RESET)


def print_section(title):
    print(f"\n{PINK}{BOLD}{title}{RESET}")
    print(RED + "-" * 60 + RESET)


def print_table(title, headers, rows, col_width=24):
    print(f"\n{PINK}{BOLD}{title}{RESET}")
    print(RED + "-" * (col_width * len(headers)) + RESET)

    header_row = ""
    for h in headers:
        header_row += f"{BOLD}{h:<{col_width}}{RESET}"
    print(header_row)

    print(RED + "-" * (col_width * len(headers)) + RESET)

    for row in rows:
        row_str = ""
        for cell in row:
            row_str += f"{CYAN}{str(cell):<{col_width}}{RESET}"
        print(row_str)

    print(RED + "-" * (col_width * len(headers)) + RESET)


def print_bar(label, value, max_value=10, color=GREEN):
    bars = int(min(value, max_value))
    print(f"{label:<25}: {color}{'█' * bars}{RESET} ({value})")



#& Summary Report


def show_terminal_report(
    price,
    cashflow,
    annual_cashflow,
    net_annual_cashflow,
    real_roi,
    rental_yield,
    ltv,
    future_value,
    future_rent,
    location_score,
    risk,
    risklabel,
    reasons,
    decision,
    score,
    deal_type,
    insight,
):
    print_header("PROPERTY ANALYSIS REPOT")

    #& Decision Block
    d_color = decision_color(decision)
    s_color = GREEN if score >= 8 else RED if score <= 3 else YELLOW

    print(f"\nDecision        : {d_color}{decision.upper()}{RESET}")
    print(f"Investment Score: {s_color}{score}/10{RESET}")
    print(f"Deal Type       : {LIGHT_GREEN}{deal_type}{RESET}")

    #& Financial Metrics Table
    print_table(
        "Financial Metrics",
        ["Metric", "Value"],
        [
            ("Property Price", f"₹{price:,.0f}"),
            ("Monthly Cashflow", f"₹{cashflow:,.0f}"),
            ("Annual Cashflow", f"₹{annual_cashflow:,.0f}"),
            ("Net Annual (After Tax)", f"₹{net_annual_cashflow:,.0f}"),
            ("Real ROI", f"{real_roi:.2f}%"),
            ("Rental Yield", f"{rental_yield:.2f}%"),
            ("Loan-to-Value (LTV)", f"{ltv:.1f}%"),
        ]
    )

    print_bar("ROI Strength", real_roi)

    #& 5-Year Projections
    print_table(
        "5-Year Projections",
        ["Projection", "Estimated Value"],
        [
            ("Property Value", f"₹{future_value:,.0f}"),
            ("Monthly Rent", f"₹{future_rent:,.0f}")
        ]
    )

    #& Location & Risk Overview
    print_table(
        "Location & Risk Overview",
        ["Factor", "Score", "Comment"],
        [
            ("Location", f"{location_score}/10", "Demand & connectivity"),
            ("Risk", f"{risk}/10", risklabel),
        ]
    )

    print_bar("Location Strength", location_score)
    print_bar("Risk Exposure", risk, color=YELLOW)



    #& Risk Factors
    print_section("Major Risk Factors")
    for r in reasons:
        print(f"{LIGHT_CYAN}- {r}{RESET}")

    #& Insights
    print_section("Key Insights")
    for line in insight:
        print(f"{LIGHT_CYAN}- {line}{RESET}")



    print(RED + "\n" + "=" * 20)
    print(LIGHT_YELLOW + "End of Report" + RESET)
    print(RED + "=" * 20)







# ##* TEST
# show_summary(
#     price=1000000,
#     cashflow=10000,
#     annual_cashflow=120000,
#     net_annual_cashflow=100000,
#     real_roi=10.0,
#     rental_yield=5.0,
#     ltv=50.0,
#     future_value=1500000,
#     future_rent=150000,
#     location_score=8.0,
#     risk=7.0,
#     risklabel="Medium",
#     reasons=["High vacancy", "Low rental yield"],
#     decision="buy",
#     score=8,
#     deal_type="Investment",
#     insight=["Seek professional advice"],
#     # sensitivity=NONE
# )



