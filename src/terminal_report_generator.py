# imports

import terminal_colors as colors



def decision_color(decision):
    return colors.GREEN if decision == "buy" else colors.RED if decision == "sell" else colors.YELLOW


def print_header(title):
    print(colors.RED + "\n" + "=" * 60)
    print(f"{colors.WHITE}{colors.BOLD}{title.center(60)}{colors.RESET}")
    print(colors.RED + "=" * 60 + colors.RESET)


def print_section(title):
    print(f"\n{colors.PINK}{colors.BOLD}{title}{colors.RESET}")
    print(colors.RED + "-" * 60 + colors.RESET)


def print_table(title, headers, rows, col_width=24):
    print(f"\n{colors.PINK}{colors.BOLD}{title}{colors.RESET}")
    print(colors.RED + "-" * (col_width * len(headers)) + colors.RESET)

    header_row = ""
    for h in headers:
        header_row += f"{colors.BOLD}{h:<{col_width}}{colors.RESET}"
    print(header_row)

    print(colors.RED + "-" * (col_width * len(headers)) + colors.RESET)

    for row in rows:
        row_str = ""
        for cell in row:
            row_str += f"{colors.CYAN}{str(cell):<{col_width}}{colors.RESET}"
        print(row_str)

    print(colors.RED + "-" * (col_width * len(headers)) + colors.RESET)


def print_bar(label, value, max_value=10, color=colors.GREEN):
    bars = int(min(value, max_value))
    print(f"{label:<25}: {color}{'█' * bars}{colors.RESET} ({value})")



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
    effective_rent,
):
    print_header("PROPERTY ANALYSIS REPORT")

    #& Decision Block
    d_color = decision_color(decision)
    s_color = colors.GREEN if score >= 8 else colors.RED if score <= 3 else colors.YELLOW

    print(f"\nDecision        : {d_color}{decision.upper()}{colors.RESET}")
    print(f"Investment Score: {s_color}{score}/10{colors.RESET}")
    print(f"Deal Type       : {colors.LIGHT_GREEN}{deal_type}{colors.RESET}")

    #& Financial Metrics Table
    print_table(
        "Financial Metrics",
        ["Metric", "Value"],
        [
            ("Property Price", f"₹{price:,.0f}"),
            ("Monthly Cashflow", f"₹{cashflow:,.0f}"),
            ("Annual Cashflow", f"₹{annual_cashflow:,.0f}"),
            ("Net Annual (After Tax)", f"₹{net_annual_cashflow:,.0f}"),
            ("Effective Rent", f"₹{effective_rent:,.0f}"),
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
    print_bar("Risk Exposure", risk, color=colors.YELLOW)



    #& Risk Factors
    print_section("Major Risk Factors")
    for r in reasons:
        print(f"{colors.LIGHT_CYAN}- {r}{colors.RESET}")

    #& Insights
    print_section("Key Insights")
    for line in insight:
        print(f"{colors.LIGHT_CYAN}- {line}{colors.RESET}")



    print(colors.RED + "\n" + "=" * 20)
    print(colors.LIGHT_YELLOW + "End of Report" + colors.RESET)
    print(colors.RED + "=" * 20)





