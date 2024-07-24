from typing import List

# Serialize a single accident report
def individual_serial(accident_report: dict) -> dict:
    return {
        "id": str(accident_report.get("_id")) if "_id" in accident_report else None,
        "client_name": accident_report.get("client_name", ""),
        "contact_number": accident_report.get("contact_number", ""),
        "accident_description": accident_report.get("accident_description", ""),
        "street_name": accident_report.get("street_name", ""),
        "surburb_name": accident_report.get("surburb_name", ""),
        "city_name": accident_report.get("city_name", ""),
        "time": accident_report.get("time", ""),
        "images": accident_report.get("images", []),
        "police_station_address": accident_report.get("police_station_address", ""),
        "ar_number": accident_report.get("ar_number", "")
    }

# Serialize a list of accident reports
def list_serial(accident_reports: List[dict]) -> List[dict]:
    return [individual_serial(report) for report in accident_reports]
