# pdf_export.py
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from paths import FONTS_DIR, PDF_DIR
from datetime import datetime


# FONT REGISTRATION

pdfmetrics.registerFont(TTFont("Normal", str(FONTS_DIR / "DejaVuSans.ttf")))
pdfmetrics.registerFont(TTFont("Bold", str(FONTS_DIR / "DejaVuSans-Bold.ttf")))



# THEME

THEME = {
    "title": colors.black,
    "section": colors.darkblue,
    "label": colors.black,
    "value": colors.HexColor("#0F766E"),
    "decision_buy": colors.green,
    "decision_sell": colors.red,
    "muted": colors.grey,
}



# HELPERS

def h_line(pdf, y):
    pdf.setStrokeColor(colors.black)
    pdf.setLineWidth(1)
    pdf.line(40, y, 555, y)


def section_title(pdf, text, y):
    pdf.setFont("Bold", 16)
    pdf.setFillColor(THEME["section"])
    pdf.drawString(40, y, text)
    h_line(pdf, y - 6)
    return y - 30


def label_value(pdf, label, value, y):
    pdf.setFont("Normal", 12)
    pdf.setFillColor(THEME["label"])
    pdf.drawString(50, y, label)

    pdf.setFillColor(THEME["value"])
    pdf.drawRightString(520, y, value)
    return y - 22



#! MAIN PDF FUNCTION

def generate_property_report(
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
    risk_score,
    risk_label,
    reasons,
    decision,
    score,
    deal_type,
    insights

    ):


    PDF_DIR.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = PDF_DIR / f"Property_Report_{timestamp}.pdf"

    pdf = canvas.Canvas(str(file_path))
    pdf.setTitle("Property Analysis Report")

    y = 800

    
    #! TITLE
    
    pdf.setFont("Bold", 22)
    pdf.setFillColor(THEME["title"])
    pdf.drawCentredString(300, y, "PROPERTY ANALYSIS REPORT")
    h_line(pdf, y - 10)

    y -= 50

    
    #! DECISION SUMMARY
    
    pdf.setFont("Bold", 14)
   
    
    pdf.drawString(40, y, f"Decision: {decision.upper()}")

    pdf.setFillColor(THEME["label"])
    y -= 25
    pdf.drawString(40, y, f"Investment Score: {score}/10")
    y -= 30
    pdf.drawString(40, y, f"Deal Type: {deal_type}")

    y -= 30
    h_line(pdf, y)

    y -= 40

    
    #! FINANCIAL METRICS
    
    y = section_title(pdf, "Financial Metrics", y)

    metrics = [
        ("Property Price", f"₹{price:,.0f}"),
        ("Monthly Cashflow", f"₹{cashflow:,.0f}"),
        ("Annual Cashflow", f"₹{annual_cashflow:,.0f}"),
        ("Net Annual (After Tax)", f"₹{net_annual_cashflow:,.0f}"),
        ("Real ROI", f"{real_roi:.2f}%"),
        ("Rental Yield", f"{rental_yield:.2f}%"),
        ("Loan-to-Value (LTV)", f"{ltv:.1f}%"),
    ]

    for label, value in metrics:
        y = label_value(pdf, label, value, y)

    y -= 10

    
    #! 5-YEAR PROJECTIONS
    
    y = section_title(pdf, "5-Year Projections", y)

    projections = [
        ("Estimated Property Value", f"₹{future_value:,.0f}"),
        ("Estimated Monthly Rent", f"₹{future_rent:,.0f}"),
    ]

    for label, value in projections:
        y = label_value(pdf, label, value, y)

    y -= 10

    
    #! LOCATION & RISK
    
    y = section_title(pdf, "Location & Risk Overview", y)

    risk_data = [
        ("Location Score", f"{location_score}/10"),
        ("Risk Exposure", f"{risk_score}/10 ({risk_label})"),
    ]

    for label, value in risk_data:
        y = label_value(pdf, label, value, y)

    y -= 10

    
    #! MAJOR RISKS
    
    y = section_title(pdf, "Major Risk Factors", y)

    pdf.setFont("Normal", 12)
    pdf.setFillColor(THEME["label"])
    for r in reasons:
        pdf.drawString(55, y, f"- {r}")
        y -= 18

    y -= 10

    
    #! KEY INSIGHTS
    
    y = section_title(pdf, "Key Insights", y)
    pdf.setFont("Normal", 12)
    for insight in insights:
        pdf.drawString(55, y, f"- {insight}")
        y -= 25

    y -= 30
    h_line(pdf, y)

    pdf.setFont("Normal", 10)
    pdf.setFillColor(THEME["muted"])
    pdf.drawCentredString(300, y - 20, "End of Report")

    pdf.save()
