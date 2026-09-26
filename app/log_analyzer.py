from app.incident import Incident
def count_log_levels(logs):
    counts = {
        "INFO": 0,
        "WARNING": 0,
        "ERROR": 0
    }
    for log in logs:
        level = log["level"]
        if level in counts:
            counts[level] += 1
    return counts
def find_errors(logs):
    errors = []
    for log in logs:
        if log["level"] == "ERROR":
            errors.append(log)
    return errors
def find_repeated_errors(logs):
    error_counts = {}
    for log in logs:
        if log["level"] == "ERROR":
            message = log["message"]
            if message not in error_counts:
                error_counts[message] = 0
            error_counts[message] += 1
    return error_counts
def determine_severity(message):
    if message == "Database connection failed":
        return "CRITICAL"
    if message == "Payment service unavailable":
        return "HIGH"
    return "MEDIUM"
def detect_incidents(logs, threshold=3):
    error_counts = find_repeated_errors(logs)
    incidents = []
    for message, count in error_counts.items():
        if count >= threshold:
            severity = determine_severity(message)
            incident = Incident(
                message=message,
                count=count,
                severity=severity
            )
            incidents.append(incident)
    return incidents
def create_incident_manager(logs, threshold=3):
    from app.incident_manager import IncidentManager
    manager = IncidentManager()
    incidents = detect_incidents(logs, threshold)
    for incident in incidents:
        manager.add_incident(incident)
    return manager
