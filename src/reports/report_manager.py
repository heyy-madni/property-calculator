# imports



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



#!  PDF Report Generator

from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.utils import simpleSplit
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from utils.paths import FONTS_DIR, PDF_DIR #type: ignore
from datetime import datetime


#* FONT  

pdfmetrics.registerFont(TTFont("Normal", str(FONTS_DIR / "DejaVuSans.ttf")))
pdfmetrics.registerFont(TTFont("Bold",   str(FONTS_DIR / "DejaVuSans-Bold.ttf")))


#* colors & layout constants 

C = {
    # base
    "bg":          colors.HexColor("#F7F8FA"),   # page background tint
    "white":       colors.white,
    "ink":         colors.HexColor("#111827"),   # primary text
    "muted":       colors.HexColor("#6B7280"),   # secondary text
    "border":      colors.HexColor("#E5E7EB"),   # card borders

    # brand
    "navy":        colors.HexColor("#0F172A"),   # header bar
    "teal":        colors.HexColor("#0D9488"),   # accent / values
    "teal_light":  colors.HexColor("#CCFBF1"),   # accent bg tint

    # decision
    "buy":         colors.HexColor("#16A34A"),
    "buy_bg":      colors.HexColor("#DCFCE7"),
    "sell":        colors.HexColor("#DC2626"),
    "sell_bg":     colors.HexColor("#FEE2E2"),
    "hold":        colors.HexColor("#D97706"),
    "hold_bg":     colors.HexColor("#FEF3C7"),

    # section accents
    "section_fin": colors.HexColor("#1D4ED8"),   # blue  – Financial
    "section_prj": colors.HexColor("#7C3AED"),   # violet – Projections
    "section_loc": colors.HexColor("#0D9488"),   # teal  – Location
    "section_rsk": colors.HexColor("#DC2626"),   # red   – Risk
    "section_ins": colors.HexColor("#D97706"),   # amber – Insights
}

PAGE_W      = 595
PAGE_H      = 842
MARGIN      = 40
CONTENT_W   = PAGE_W - MARGIN * 2
PAGE_BOTTOM = 70
PAGE_TOP    = PAGE_H - MARGIN


#* help for drawing in low

def rounded_rect(pdf, x, y, w, h, r=6, fill=None, stroke=None, line_w=0.5):
    """Draw a rounded rectangle. y is TOP of the rect (we convert internally)."""
    pdf.saveState()
    if fill:
        pdf.setFillColor(fill)
    if stroke:
        pdf.setStrokeColor(stroke)
        pdf.setLineWidth(line_w)
    # ReportLab y-origin is bottom-left; y here is the TOP edge
    pdf.roundRect(x, y - h, w, h, r,
                  fill=1 if fill else 0,
                  stroke=1 if stroke else 0)
    pdf.restoreState()


def left_bar(pdf, x, y, h, color, w=4):
    """Vertical accent bar on left edge of a card."""
    pdf.saveState()
    pdf.setFillColor(color)
    pdf.rect(x, y - h, w, h, fill=1, stroke=0)
    pdf.restoreState()


def check_y(pdf, y, needed):
    if y - needed < PAGE_BOTTOM:
        pdf.showPage()
        _draw_page_bg(pdf)
        return PAGE_TOP
    return y


def _draw_page_bg(pdf):
    """Subtle off-white background on every page."""
    pdf.saveState()
    pdf.setFillColor(C["bg"])
    pdf.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
    pdf.restoreState()


#* SECTION HEADER 

def section_header(pdf, title, accent, y):
    """
    Pill-style section header:  ▐ TITLE ─────────────────
    Returns y after the header (ready to draw content).
    """
    needed = 42
    y = check_y(pdf, y, needed)

    # accent pill
    pill_w = 10
    rounded_rect(pdf, MARGIN, y, pill_w, 22, r=3, fill=accent)

    # title text
    pdf.saveState()
    pdf.setFont("Bold", 13)
    pdf.setFillColor(accent)
    pdf.drawString(MARGIN + pill_w + 8, y - 16, title.upper())
    pdf.restoreState()

    # rule line
    text_end = MARGIN + pill_w + 8 + pdf.stringWidth(title.upper(), "Bold", 13) + 10
    pdf.saveState()
    pdf.setStrokeColor(accent)
    pdf.setLineWidth(0.8)
    pdf.line(text_end, y - 11, MARGIN + CONTENT_W, y - 11)
    pdf.restoreState()

    return y - 34


#* metric row (for financials and projections)

def metric_row(pdf, label, value, y, value_color=None):
    needed = 24
    y = check_y(pdf, y, needed)
    vc = value_color or C["teal"]

    pdf.saveState()
    pdf.setFont("Normal", 11)
    pdf.setFillColor(C["muted"])
    pdf.drawString(MARGIN + 16, y - 14, label)

    pdf.setFont("Bold", 11)
    pdf.setFillColor(vc)
    pdf.drawRightString(MARGIN + CONTENT_W - 12, y - 14, value)

    # dotted rule between label and value
    lw = pdf.stringWidth(label, "Normal", 11)
    vw = pdf.stringWidth(value, "Bold", 11)
    gap_x1 = MARGIN + 16 + lw + 6
    gap_x2 = MARGIN + CONTENT_W - 12 - vw - 6
    if gap_x2 > gap_x1:
        pdf.setStrokeColor(C["border"])
        pdf.setLineWidth(0.5)
        pdf.setDash(1, 4)
        pdf.line(gap_x1, y - 16, gap_x2, y - 16)
    pdf.restoreState()

    return y - 24


#* card wrapper

def open_card(pdf, y, accent=None):
    """Call before drawing rows. Returns inner_y (top of content area)."""
    # We don't know card height yet; draw background after close_card.
    # Instead, use a simple top padding.
    if accent:
        left_bar(pdf, MARGIN, y, 4, accent)  # tiny top bar, will extend in close
    return y - 6


def draw_card_bg(pdf, y_top, y_bottom, accent=None):
    """
    Draw the card background retroactively.
    y_top: y value BEFORE open_card padding
    y_bottom: y value after last row
    """
    h = y_top - y_bottom + 10
    rounded_rect(pdf, MARGIN, y_top + 4, CONTENT_W, h,
                 r=6, fill=C["white"], stroke=C["border"], line_w=0.6)
    if accent:
        left_bar(pdf, MARGIN, y_top + 4, h, accent, w=4)


#* bullet item 

def bullet_item(pdf, text, y, accent, max_width=CONTENT_W - 36, line_h=17):
    """
    Wraps long text across multiple lines.
    Returns updated y.
    """
    lines = simpleSplit(text, "Normal", 11, max_width)
    needed = len(lines) * line_h + 6
    y = check_y(pdf, y, needed)

    # bullet dot
    pdf.saveState()
    pdf.setFillColor(accent)
    pdf.circle(MARGIN + 20, y - 10, 3, fill=1, stroke=0)

    pdf.setFont("Normal", 11)
    pdf.setFillColor(C["ink"])
    for i, line in enumerate(lines):
        pdf.drawString(MARGIN + 30, y - 14 - i * line_h, line)
    pdf.restoreState()

    return y - needed


#* header

def draw_header(pdf, decision, score, deal_type):
    # dark navy band
    pdf.saveState()
    pdf.setFillColor(C["navy"])
    pdf.rect(0, PAGE_H - 90, PAGE_W, 90, fill=1, stroke=0)

    # title
    pdf.setFont("Bold", 20)
    pdf.setFillColor(C["white"])
    pdf.drawString(MARGIN, PAGE_H - 38, "PROPERTY ANALYSIS REPORT")

    # subtitle / date
    pdf.setFont("Normal", 9)
    pdf.setFillColor(C["muted"])
    date_str = datetime.now().strftime("%B %d, %Y")
    pdf.drawRightString(PAGE_W - MARGIN, PAGE_H - 38, date_str)

    pdf.restoreState()

    #* Decision badge 
    d = decision.upper()
    if d == "BUY":
        dc, dbc = C["buy"], C["buy_bg"]
    elif d == "SELL":
        dc, dbc = C["sell"], C["sell_bg"]
    else:
        dc, dbc = C["hold"], C["hold_bg"]

    badge_y = PAGE_H - 90 - 18       # just below the band

    
    cx, cy = MARGIN + 28, badge_y - 28
    pdf.saveState()
    pdf.setFillColor(C["navy"])
    pdf.circle(cx, cy, 28, fill=1, stroke=0)
    pdf.setFillColor(C["white"])
    pdf.setFont("Bold", 18)
    pdf.drawCentredString(cx, cy - 7, str(score))
    pdf.setFont("Normal", 7)
    pdf.setFillColor(C["muted"])
    pdf.drawCentredString(cx, cy - 17, "/ 10")
    pdf.restoreState()

    
    pill_x = MARGIN + 70
    rounded_rect(pdf, pill_x, badge_y, 110, 30, r=15, fill=dbc)
    pdf.saveState()
    pdf.setFont("Bold", 14)
    pdf.setFillColor(dc)
    pdf.drawCentredString(pill_x + 55, badge_y - 20, d)
    pdf.restoreState()

    
    tag_x = pill_x + 120
    rounded_rect(pdf, tag_x, badge_y, 180, 30, r=6, fill=C["teal_light"])
    pdf.saveState()
    pdf.setFont("Normal", 10)
    pdf.setFillColor(C["teal"])
    pdf.drawCentredString(tag_x + 90, badge_y - 20, deal_type)
    pdf.restoreState()

    return badge_y - 48    # y ready for first section


#* 2-COLUMN MINI STATS (for location/risk)

def two_col_stat(pdf, left_label, left_val, right_label, right_val,
                 lv_color, rv_color, y):
    needed = 54
    y = check_y(pdf, y, needed)
    half = CONTENT_W // 2 - 8

    for i, (lbl, val, col) in enumerate([
        (left_label,  left_val,  lv_color),
        (right_label, right_val, rv_color),
    ]):
        bx = MARGIN + i * (half + 16)
        rounded_rect(pdf, bx, y, half, 46, r=6,
                     fill=C["white"], stroke=C["border"], line_w=0.6)
        pdf.saveState()
        pdf.setFont("Normal", 9)
        pdf.setFillColor(C["muted"])
        pdf.drawCentredString(bx + half // 2, y - 16, lbl)
        pdf.setFont("Bold", 18)
        pdf.setFillColor(col)
        pdf.drawCentredString(bx + half // 2, y - 36, val)
        pdf.restoreState()

    return y - 58


#* footer

def draw_footer(pdf, y):
    y = check_y(pdf, y, 36)
    pdf.saveState()
    pdf.setStrokeColor(C["border"])
    pdf.setLineWidth(0.5)
    pdf.line(MARGIN, y, MARGIN + CONTENT_W, y)
    pdf.setFont("Normal", 8)
    pdf.setFillColor(C["muted"])
    pdf.drawCentredString(PAGE_W / 2, y - 16,
                          "Generated by Property Analysis Tool  •  For informational purposes only")
    pdf.restoreState()


#* main

def generate_property_report(results):

    PDF_DIR.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = PDF_DIR / f"Property_Report_{timestamp}.pdf"

    pdf = canvas.Canvas(str(file_path), pagesize=(PAGE_W, PAGE_H))
    pdf.setTitle("Property Analysis Report")

    # page background
    _draw_page_bg(pdf)

    # header band + decision badges
    y = draw_header(pdf, results['decision'], results['score'], results['deal_type'])
    y -= 10


    # ── FINANCIAL METRICS ────────────────────────────────────────────
    y = section_header(pdf, "Financial Metrics", C["section_fin"], y)

    card_top = y
    y = open_card(pdf, y)
    metrics = [
        ("Property Price",         f"₹{results['price']:,.0f}"),
        ("Monthly Cashflow",       f"₹{results['cashflow']:,.0f}"),
        ("Annual Cashflow",        f"₹{results['annual_cashflow']:,.0f}"),
        ("Net Annual (After Tax)", f"₹{results['net_annual_cashflow']:,.0f}"),
        ("Real ROI",               f"{results['real_roi']:.2f}%"),
        ("Rental Yield",           f"{results['rental_yield']:.2f}%"),
        ("Loan-to-Value (LTV)",    f"{results['ltv']:.1f}%"),
    ]
    for label, value in metrics:
        y = metric_row(pdf, label, value, y, C["section_fin"])
    draw_card_bg(pdf, card_top, y, C["section_fin"])
    y -= 18


    # ── 5-YEAR PROJECTIONS ───────────────────────────────────────────
    y = section_header(pdf, "5-Year Projections", C["section_prj"], y)

    card_top = y
    y = open_card(pdf, y)
    projections = [
        ("Estimated Property Value", f"₹{results['future_value']:,.0f}"),
        ("Estimated Monthly Rent",   f"₹{results['future_rent']:,.0f}"),
    ]
    for label, value in projections:
        y = metric_row(pdf, label, value, y, C["section_prj"])
    draw_card_bg(pdf, card_top, y, C["section_prj"])
    y -= 18


    # ── LOCATION & RISK (two-column stat cards) ──────────────────────
    y = section_header(pdf, "Location & Risk Overview", C["section_loc"], y)
    y = two_col_stat(
        pdf,
        "Location Score",  f"{results['location_score']}/10",
        "Risk Exposure",   f"{results['risk_score']}/10",
        C["section_loc"],  C["section_rsk"],
        y,
    )
    # risk label badge under the stats
    y = check_y(pdf, y, 28)
    rounded_rect(pdf, MARGIN + CONTENT_W // 2 + 8, y + 2, 180, 22,
                 r=11, fill=C["sell_bg"])
    pdf.saveState()
    pdf.setFont("Normal", 10)
    pdf.setFillColor(C["section_rsk"])
    pdf.drawCentredString(MARGIN + CONTENT_W // 2 + 8 + 90, y - 12, results['risk_label'])
    pdf.restoreState()
    y -= 24


    # ── MAJOR RISKS ──────────────────────────────────────────────────
    y -= 8
    y = section_header(pdf, "Major Risk Factors", C["section_rsk"], y)

    card_top = y + 6
    y -= 8
    for r in results['risk_reasons']:
        y = bullet_item(pdf, r, y, C["section_rsk"])
        y -= 4
    draw_card_bg(pdf, card_top, y, C["section_rsk"])
    y -= 18


    # ── KEY INSIGHTS ─────────────────────────────────────────────────
    y = section_header(pdf, "Key Insights", C["section_ins"], y)

    card_top = y + 6
    y -= 8
    for insight in results['insight']:
        y = bullet_item(pdf, insight, y, C["section_ins"])
        y -= 4
    draw_card_bg(pdf, card_top, y, C["section_ins"])
    y -= 24


    # ── FOOTER ───────────────────────────────────────────────────────
    draw_footer(pdf, y)

    pdf.save()
    return file_path

