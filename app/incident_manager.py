from app.incident import Incident
class IncidentManager:
    def __init__(self):
        self.incidents = []
    def add_incident(self, incident):
        self.incidents.append(incident)
    def get_open_incidents(self):
        return [
            incident
            for incident in self.incidents
            if incident.status == "OPEN"
        ]
    def close_incident(self, incident):
        incident.status = "CLOSED"
