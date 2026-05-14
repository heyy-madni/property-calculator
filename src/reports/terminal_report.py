import utils.common_utils as utils#type:ignore




#& Terminal Report Generator
def decision_color(decision):
    return utils.GREEN if decision == "buy" else utils.RED if decision == "sell" else utils.YELLOW


def print_header(title):
    print(utils.RED + "\n" + "=" * 60)
    print(f"{utils.WHITE}{utils.BOLD}{title.center(60)}{utils.RESET}")
    print(utils.RED + "=" * 60 + utils.RESET)


def print_section(title):
    print(f"\n{utils.PINK}{utils.BOLD}{title}{utils.RESET}")
    print(utils.RED + "-" * 60 + utils.RESET)


def print_table(title, headers, rows, col_width=24):
    print(f"\n{utils.PINK}{utils.BOLD}{title}{utils.RESET}")
    print(utils.RED + "-" * (col_width * len(headers)) + utils.RESET)

    header_row = ""
    for h in headers:
        header_row += f"{utils.BOLD}{h:<{col_width}}{utils.RESET}"
    print(header_row)

    print(utils.RED + "-" * (col_width * len(headers)) + utils.RESET)

    for row in rows:
        row_str = ""
        for cell in row:
            row_str += f"{utils.CYAN}{str(cell):<{col_width}}{utils.RESET}"
        print(row_str)

    print(utils.RED + "-" * (col_width * len(headers)) + utils.RESET)


def print_bar(label, value, max_value=10, color=utils.GREEN):
    bars = int(min(value, max_value))
    print(f"{label:<25}: {color}{'█' * bars}{utils.RESET} ({value})")



#& Summary Report


def show_terminal_report(results):
    utils.clear_console()
    print_header("PROPERTY ANALYSIS REPORT")

    #& Decision Block
    d_color = decision_color(results['decision'])
    s_color = utils.GREEN if results['score'] >= 8 else utils.RED if results['score'] <= 3 else utils.YELLOW

    print(f"\nDecision        : {d_color}{results['decision'].upper()}{utils.RESET}")
    print(f"Investment Score: {s_color}{results['score']}/10{utils.RESET}")
    print(f"Deal Type       : {utils.LIGHT_GREEN}{results['deal_type']}{utils.RESET}")

    #& Financial Metrics Table
    print_table(
        "Financial Metrics",
        ["Metric", "Value"],
        [
            ("Property Price", f"₹{results['price']:,.0f}"),
            ("Monthly Cashflow", f"₹{results['cashflow']:,.0f}"),
            ("Annual Cashflow", f"₹{results['annual_cashflow']:,.0f}"),
            ("Net Annual (After Tax)", f"₹{results['net_annual_cashflow']:,.0f}"),
            ("Effective Rent", f"₹{results['effective_rent']:,.0f}"),
            ("Real ROI", f"{results['real_roi']:.2f}%"),
            ("Rental Yield", f"{results['rental_yield']:.2f}%"),
            ("Loan-to-Value (LTV)", f"{results['ltv']:.1f}%"),
        ]
    )

    print_bar("ROI Strength", results['real_roi'])

    #& 5-Year Projections
    print_table(
        "5-Year Projections",
        ["Projection", "Estimated Value"],
        [
            ("Property Value", f"₹{results['future_value']:,.0f}"),
            ("Monthly Rent", f"₹{results['future_rent']:,.0f}")
        ]
    )

    #& Location & Risk Overview
    print_table(
        "Location & Risk Overview",
        ["Factor", "Score", "Comment"],
        [
            ("Location", f"{results['location_score']}/10", "Demand & connectivity"),
            ("Risk", f"{results['risk_score']}/10", results['risk_label']),
        ]
    )

    print_bar("Location Strength", results['location_score'])
    print_bar("Risk Exposure", results['risk_score'], color=utils.YELLOW)



    #& Risk Factors
    print_section("Major Risk Factors")
    for r in results['risk_reasons']:
        print(f"{utils.LIGHT_CYAN}- {r}{utils.RESET}")

    #& Insights
    print_section("Key Insights")
    for line in results['insight']:
        print(f"{utils.LIGHT_CYAN}- {line}{utils.RESET}")



    print(utils.RED + "\n" + "=" * 20)
    print(utils.LIGHT_YELLOW + "End of Report" + utils.RESET)
    print(utils.RED + "=" * 20)
    input(f"\n{utils.LIGHT_YELLOW}Press Enter to return to main menu...{utils.RESET}")


