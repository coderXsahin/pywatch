import time
from datetime import datetime

from app import incident
from app.incident_service import IncidentService


class Monitor:
    def __init__(self, log_file="logs/application.log", interval=5):
        self.log_file = log_file
        self.interval = interval
        self.service = IncidentService()

    def check(self):
        print(f"Check time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        manager = self.service.analyze_log_file(self.log_file)

        incidents = manager.get_open_incidents()

        print("=== Monitoring Check ===")
        print(f"Open incidents: {len(incidents)}")

        critical_count = sum(
    1       for incident in incidents
            if incident.severity == "CRITICAL"
        )

        high_count = sum(
        1       for incident in incidents
                if incident.severity == "HIGH"
        )

        print(f"Critical incidents: {critical_count}")
        print(f"High incidents: {high_count}")

        for incident in incidents:
            print(incident.summary())

        return incidents
if __name__ == "__main__":
    monitor = Monitor(interval=5)

    while True:
        monitor.check()
        time.sleep(monitor.interval)