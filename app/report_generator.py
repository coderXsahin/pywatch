import json
def generate_report(incidents):
    report = []
    for incident in incidents:
        report.append({
            "message": incident.message,
            "count": incident.count,
            "severity": incident.severity,
            "status": incident.status,
            "root_cause": incident.root_cause,
            "recommendation": incident.recommendation
        })
    return report
def save_report(report, file_path):
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(report, file, indent=4)
def load_report(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)
def get_report_statistics(report):
    statistics = {
        "total_incidents": len(report),
        "open_incidents": 0,
        "critical_incidents": 0,
        "high_incidents": 0
    }
    for incident in report:
        if incident["status"] == "OPEN":
            statistics["open_incidents"] += 1
        if incident["severity"] == "CRITICAL":
            statistics["critical_incidents"] += 1
        if incident["severity"] == "HIGH":
            statistics["high_incidents"] += 1
    return statistics
def build_report_summary(report):
    statistics = get_report_statistics(report)
    return {
        "statistics": statistics,
        "incidents": report
    }
