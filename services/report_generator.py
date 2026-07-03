from datetime import datetime
from typing import Dict


def generate_report(result: Dict) -> str:
    """
    Generate a formatted financial analysis report.
    Returns the report as a string.
    """

    company = result.get("company", {})
    ratios = result.get("ratios", {})
    score = result.get("financial_health", {})
    recommendation = result.get("investment", {})
    red_flags = result.get("red_flags", [])
    swot = result.get("swot", {})
    ai_analysis = result.get("ai_analysis", "")

    report = []

    report.append("=" * 70)
    report.append("FinSight AI - Equity Research Report")
    report.append("=" * 70)
    report.append(f"Generated: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}")
    report.append("")

    # -----------------------------------------------------
    # Company
    # -----------------------------------------------------

    report.append("COMPANY INFORMATION")
    report.append("-" * 70)

    for key, value in company.items():
        report.append(f"{key}: {value}")

    report.append("")

    # -----------------------------------------------------
    # Financial Health
    # -----------------------------------------------------

    report.append("FINANCIAL HEALTH")
    report.append("-" * 70)

    for key, value in score.items():
        report.append(f"{key}: {value}")

    report.append("")

    # -----------------------------------------------------
    # Ratios
    # -----------------------------------------------------

    report.append("FINANCIAL RATIOS")
    report.append("-" * 70)

    for key, value in ratios.items():
        report.append(f"{key}: {value}")

    report.append("")

    # -----------------------------------------------------
    # Investment Recommendation
    # -----------------------------------------------------

    report.append("INVESTMENT RECOMMENDATION")
    report.append("-" * 70)

    for key, value in recommendation.items():
        report.append(f"{key}: {value}")

    report.append("")

    # -----------------------------------------------------
    # SWOT
    # -----------------------------------------------------

    report.append("SWOT ANALYSIS")
    report.append("-" * 70)

    for section in [
        "strengths",
        "weaknesses",
        "opportunities",
        "threats",
    ]:

        report.append(section.upper())

        for item in swot.get(section, []):
            report.append(f"• {item}")

        report.append("")

    # -----------------------------------------------------
    # Red Flags
    # -----------------------------------------------------

    report.append("RED FLAGS")
    report.append("-" * 70)

    if red_flags:
        for flag in red_flags:
            report.append(f"• {flag}")
    else:
        report.append("No major financial red flags detected.")

    report.append("")

    # -----------------------------------------------------
    # AI Analysis
    # -----------------------------------------------------

    report.append("AI ANALYSIS")
    report.append("-" * 70)

    report.append(str(ai_analysis))

    report.append("")
    report.append("=" * 70)
    report.append("End of Report")
    report.append("=" * 70)

    return "\n".join(report)