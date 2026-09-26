from app.root_cause import analyze_root_cause
from app.recommendation import get_recommendation
class Incident:
    def __init__(self, message, count, severity="HIGH", status="OPEN"):
        self.message = message
        self.count = count
        self.severity = severity
        self.status = status
        self.root_cause = analyze_root_cause(message)
        self.recommendation = get_recommendation(message)
    def summary(self):
        return (
            f"{self.severity} incident: "
            f"{self.message} occurred {self.count} times. "
            f"Status: {self.status}. "
            f"Probable root cause: {self.root_cause}. "
            f"Recommended action: {self.recommendation}"
        )
    def to_dict(self):
        return {
            "message": self.message,
            "count": self.count,
            "severity": self.severity,
            "status": self.status,
            "root_cause": self.root_cause,
            "recommendation": self.recommendation
        }
    def __repr__(self):
        return (
            f"Incident(message='{self.message}', "
            f"count={self.count}, "
            f"severity='{self.severity}', "
            f"status='{self.status}')"
        )
