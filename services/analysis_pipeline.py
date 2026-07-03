from services.pdf_reader import extract_text
from services.page_locator import locate_financial_pages
from services.page_inspector import inspect_page
from services.table_extractor import extract_tables
from services.company_identifier import identify_company

from services.financial_parser import (
    extract_financial_data,
    extract_financial_data_from_tables,
)

from services.field_mapper import map_fields
from services.ratio_calculator import calculate_ratios
from services.financial_scorer import calculate_financial_score
from services.red_flag_detector import detect_red_flags
from services.investment_engine import generate_investment_recommendation
from services.openrouter import generate_financial_analysis

from services.swot_generator import generate_swot
from services.trend_analyzer import analyze_trends
from services.chart_generator import generate_charts
from services.report_generator import generate_report
from services.excel_export import export_to_excel

import os


def analyze_report(pdf_path: str):
    """
    Complete FinSight AI Financial Analysis Pipeline
    """

    # ======================================================
    # STEP 1 - Extract PDF Text
    # ======================================================

    extracted_text = extract_text(pdf_path)

    # ======================================================
    # STEP 2 - Identify Company
    # ======================================================

    company_info = identify_company(extracted_text)

    # ======================================================
    # STEP 3 - Locate Financial Statements
    # ======================================================

    located_pages = locate_financial_pages(pdf_path)

    # ======================================================
    # STEP 4 - Inspect Pages
    # ======================================================

    inspected_pages = {}

    for section, pages in located_pages.items():

        inspected_pages[section] = []

        for page in pages:

            inspected_pages[section].append(

                inspect_page(
                    pdf_path,
                    page["page"]
                )

            )

    # ======================================================
    # STEP 5 - Extract Tables
    # ======================================================

    extracted_tables = []

    for section, pages in located_pages.items():

        for page in pages:

            tables = extract_tables(
                pdf_path,
                page["page"]
            )

            extracted_tables.extend(tables)

    # ======================================================
    # STEP 6 - Parse Financial Tables
    # ======================================================

    table_data = extract_financial_data_from_tables(
        extracted_tables
    )

    # ======================================================
    # STEP 7 - Regex Extraction Backup
    # ======================================================

    regex_data = extract_financial_data(
        extracted_text
    )

    # ======================================================
    # STEP 8 - Merge Financial Data
    # ======================================================

    financial_data = regex_data.copy()

    financial_data.update(

        {
            key: value
            for key, value in table_data.items()
            if value is not None
        }

    )

    # ======================================================
    # STEP 9 - Standardize Fields
    # ======================================================

    standardized_data = map_fields(
        financial_data
    )

    # ======================================================
    # STEP 10 - Calculate Ratios
    # ======================================================

    ratios = calculate_ratios(
        standardized_data
    )

        # ======================================================
    # STEP 11 - Financial Health Score
    # ======================================================

    financial_score = calculate_financial_score(
        standardized_data,
        ratios
    )

    # ======================================================
    # STEP 12 - Detect Red Flags
    # ======================================================

    red_flags = detect_red_flags(
        standardized_data,
        ratios
    )

    # ======================================================
    # STEP 13 - Investment Recommendation
    # ======================================================

    recommendation = generate_investment_recommendation(
        financial_score,
        red_flags,
        ratios
    )

    # ======================================================
    # STEP 14 - SWOT Analysis
    # ======================================================

    swot = generate_swot(
        standardized_data,
        ratios,
        financial_score,
        red_flags,
        recommendation
    )

    # ======================================================
    # STEP 15 - Trend Analysis
    # ======================================================

    financial_history = [
        standardized_data
    ]

    trends = analyze_trends(
        financial_history
    )

    # ======================================================
    # STEP 16 - Chart Data
    # ======================================================

    charts = generate_charts(
        standardized_data,
        ratios
    )

    # ======================================================
    # STEP 17 - AI Financial Analysis
    # ======================================================

    try:

        ai_report = generate_financial_analysis(
            standardized_data,
            ratios
        )

    except Exception as e:

        ai_report = f"AI Analysis unavailable: {str(e)}"

        # ======================================================
    # STEP 18 - Build Result Dictionary
    # ======================================================

    result = {

        "company": company_info,

        "financial_data": standardized_data,

        "ratios": ratios,

        "financial_health": financial_score,

        "red_flags": red_flags,

        "investment": recommendation,

        "swot": swot,

        "trends": trends,

        "charts": charts,

        "ai_analysis": ai_report,

        "table_extraction": {

            "tables_found": len(extracted_tables),

            "fields_extracted": len(table_data)

        },

        "pipeline_status": "Success"

    }

    # ======================================================
    # STEP 19 - Generate Text Report
    # ======================================================

    try:

        report = generate_report(result)

        result["report"] = report

    except Exception as e:

        result["report"] = f"Report generation failed: {str(e)}"

    # ======================================================
    # STEP 20 - Export Excel
    # ======================================================

    try:

        os.makedirs("exports", exist_ok=True)

        company_name = (
            company_info.get("company_name")
            or company_info.get("Company Name")
            or "Company"
        )

        safe_name = (
            str(company_name)
            .replace(" ", "_")
            .replace("/", "_")
            .replace("\\", "_")
        )

        excel_path = os.path.join(
            "exports",
            f"{safe_name}_Analysis.xlsx"
        )

        export_to_excel(
            result,
            excel_path
        )

        result["excel_file"] = excel_path

    except Exception as e:

        result["excel_file"] = f"Excel export failed: {str(e)}"

    # ======================================================
    # STEP 21 - Return Complete Result
    # ======================================================

    return result    