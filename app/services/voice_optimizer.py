from collections import Counter
from typing import List, Dict, Optional

# def summarize_if_large(data: List[Dict]) -> List[Dict]:
#     if len(data) > 10:
#         return [{"summary": f"{len(data)} records found. Showing first 10."}]
#     return data
# def summarize_if_large(data: List[Dict]) -> List[Dict]:
#     if not data:
#         return []

#     sample = data[0]

#     # If analytics/time-series data
#     if "revenue" in sample:
#         total_revenue = sum(item.get("revenue", 0) for item in data)
#         return [{
#             "summary": f"Total revenue is {total_revenue} across {len(data)} records."
#         }]

#     if len(data) > 10:
#         return [{
#             "summary": f"{len(data)} records found. Showing top 10 most relevant results."
#         }]

#     return data


def summarize_if_large(data: List[Dict]) -> Optional[Dict]:

    if not data:
        return None

    sample = data[0]

    # ---------------------------
    # 1️⃣ Support Ticket Summary
    # ---------------------------
    if "ticket_id" in sample and "status" in sample:
        status_counts = Counter(item["status"] for item in data)
        priority_counts = Counter(item["priority"] for item in data)

        return {
            "total_tickets": len(data),
            "open_tickets": status_counts.get("open", 0),
            "closed_tickets": status_counts.get("closed", 0),
            "high_priority": priority_counts.get("high", 0),
        }

    # ---------------------------
    # 2️⃣ Analytics Summary
    # ---------------------------
    if "value" in sample and "metric" in sample:
        total_value = sum(item.get("value", 0) for item in data)
        avg_value = total_value / len(data)

        latest = sorted(
            data,
            key=lambda x: x.get("date", ""),
            reverse=True
        )[0]

        return {
            "metric": latest.get("metric"),
            "latest_value": latest.get("value"),
            "average_value": round(avg_value, 2),
            "data_points": len(data)
            }

    # ---------------------------
    # 3️⃣ CRM Summary
    # ---------------------------
    if "customer_id" in sample and "status" in sample:
        status_counts = Counter(item["status"] for item in data)

        return {
            "total_customers": len(data),
            "active": status_counts.get("active", 0),
            "inactive": status_counts.get("inactive", 0),
            }

    # Default behavior
    return None
