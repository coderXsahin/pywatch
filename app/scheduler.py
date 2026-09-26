import time
from app.monitor import Monitor


class Scheduler:

    def __init__(self, interval=5):
        self.interval = interval
        self.monitor = Monitor()

    def start(self):
        print("PyWatch scheduler started")

        while True:
            incidents = self.monitor.check()

            print(
                f"Monitoring check completed. "
                f"Incidents found: {len(incidents)}"
            )

            time.sleep(self.interval)