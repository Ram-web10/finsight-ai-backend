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
import traceback


def analyze_report(pdf_path: str):
    """
    Complete FinSight AI Analysis Pipeline
    """

    print("=" * 70)
    print("FinSight AI Analysis Started")
    print(f"PDF Path: {pdf_path}")
    print("=" * 70)

    try:

        # ======================================================
        # STEP 1 - Extract PDF Text
        # ======================================================

        print("\n[STEP 1] Extracting PDF Text...")

        extracted_text = extract_text(pdf_path)

        print("✓ STEP 1 Completed")

        # ======================================================
        # STEP 2 - Identify Company
        # ======================================================

        print("\n[STEP 2] Identifying Company...")

        company_info = identify_company(extracted_text)

        print("✓ STEP 2 Completed")
        print(company_info)

        # ======================================================
        # STEP 3 - Locate Financial Pages
        # ======================================================

        print("\n[STEP 3] Locating Financial Statements...")

        located_pages = locate_financial_pages(pdf_path)

        print("✓ STEP 3 Completed")
        print(located_pages)

        # ======================================================
        # STEP 4 - Inspect Pages
        # ======================================================

        print("\n[STEP 4] Inspecting Pages...")

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

        print("✓ STEP 4 Completed")

        # ======================================================
        # STEP 5 - Extract Tables
        # ======================================================

        print("\n[STEP 5] Extracting Tables...")

        extracted_tables = []

        for section, pages in located_pages.items():

            for page in pages:

                tables = extract_tables(
                    pdf_path,
                    page["page"]
                )

                extracted_tables.extend(tables)

        print(f"✓ STEP 5 Completed")
        print(f"Tables Extracted: {len(extracted_tables)}")

        # ======================================================
        # STEP 6 - Parse Financial Tables
        # ======================================================

        print("\n[STEP 6] Parsing Financial Tables...")

        table_data = extract_financial_data_from_tables(
            extracted_tables
        )

        print("✓ STEP 6 Completed")

        # ======================================================
        # STEP 7 - Regex Backup Extraction
        # ======================================================

        print("\n[STEP 7] Regex Financial Extraction...")

        regex_data = extract_financial_data(
            extracted_text
        )

        print("✓ STEP 7 Completed")

        # ======================================================
        # STEP 8 - Merge Data
        # ======================================================

        print("\n[STEP 8] Merging Financial Data...")

        financial_data = regex_data.copy()

        financial_data.update({

            key: value

            for key, value in table_data.items()

            if value is not None

        })

        print("✓ STEP 8 Completed")

                # ======================================================
        # STEP 9 - Standardize Fields
        # ======================================================

        print("\n[STEP 9] Standardizing Financial Fields...")

        standardized_data = map_fields(
            financial_data
        )

        print("✓ STEP 9 Completed")

        # ======================================================
        # STEP 10 - Calculate Ratios
        # ======================================================

        print("\n[STEP 10] Calculating Financial Ratios...")

        ratios = calculate_ratios(
            standardized_data
        )

        print("✓ STEP 10 Completed")
        print(ratios)

        # ======================================================
        # STEP 11 - Financial Health Score
        # ======================================================

        print("\n[STEP 11] Calculating Financial Score...")

        financial_score = calculate_financial_score(
            standardized_data,
            ratios
        )

        print("✓ STEP 11 Completed")
        print(financial_score)

        # ======================================================
        # STEP 12 - Detect Red Flags
        # ======================================================

        print("\n[STEP 12] Detecting Red Flags...")

        red_flags = detect_red_flags(
            standardized_data,
            ratios
        )

        print("✓ STEP 12 Completed")
        print(red_flags)

        # ======================================================
        # STEP 13 - Investment Recommendation
        # ======================================================

        print("\n[STEP 13] Generating Investment Recommendation...")

        recommendation = generate_investment_recommendation(
            financial_score,
            red_flags,
            ratios
        )

        print("✓ STEP 13 Completed")
        print(recommendation)

        # ======================================================
        # STEP 14 - SWOT Analysis
        # ======================================================

        print("\n[STEP 14] Building SWOT Analysis...")

        swot = generate_swot(
            standardized_data,
            ratios,
            financial_score,
            red_flags,
            recommendation
        )

        print("✓ STEP 14 Completed")

        # ======================================================
        # STEP 15 - Trend Analysis
        # ======================================================

        print("\n[STEP 15] Analyzing Trends...")

        financial_history = [
            standardized_data
        ]

        trends = analyze_trends(
            financial_history
        )

        print("✓ STEP 15 Completed")

        # ======================================================
        # STEP 16 - Generate Charts
        # ======================================================

        print("\n[STEP 16] Generating Charts...")

        charts = generate_charts(
            standardized_data,
            ratios
        )

        print("✓ STEP 16 Completed")

        # ======================================================
        # STEP 17 - AI Financial Analysis
        # ======================================================

        print("\n[STEP 17] Calling AI Model...")

        try:

            ai_report = generate_financial_analysis(
                standardized_data,
                ratios
            )

            print("✓ AI Analysis Completed")

        except Exception as ai_error:

            print("❌ AI Analysis Failed")
            print(ai_error)

            ai_report = (
                "AI analysis unavailable.\n\n"
                f"Reason: {str(ai_error)}"
            )

                    # ======================================================
        # STEP 18 - Build Result Dictionary
        # ======================================================

        print("\n[STEP 18] Building Result Dictionary...")

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

        print("✓ STEP 18 Completed")

        # ======================================================
        # STEP 19 - Generate Report
        # ======================================================

        print("\n[STEP 19] Generating Report...")

        try:

            report = generate_report(result)

            result["report"] = report

            print("✓ Report Generated")

        except Exception as report_error:

            print("❌ Report Generation Failed")

            print(report_error)

            result["report"] = str(report_error)

        # ======================================================
        # STEP 20 - Export Excel
        # ======================================================

        print("\n[STEP 20] Exporting Excel...")

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

            print("✓ Excel Exported")

        except Exception as excel_error:

            print("❌ Excel Export Failed")

            print(excel_error)

            result["excel_file"] = str(excel_error)

        # ======================================================
        # STEP 21 - Finished
        # ======================================================

        print("\n" + "=" * 70)
        print("🎉 FinSight AI Analysis Completed Successfully")
        print("=" * 70)

        return result

    except Exception as e:

        print("\n" + "=" * 70)
        print("❌ PIPELINE FAILED")
        print("=" * 70)

        traceback.print_exc()

        return {
            "pipeline_status": "Failed",
            "error": str(e),
            "traceback": traceback.format_exc()
        }