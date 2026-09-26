from app.log_parser import parse_log_file
from app.log_analyzer import create_incident_manager
from app.incident_repository import IncidentRepository


class IncidentService:

    def __init__(self):
        self.repository = IncidentRepository()

    def analyze_log_file(self, file_path, threshold=3, save=True):
        logs = parse_log_file(file_path)
        manager = create_incident_manager(logs, threshold)

        if save:
            for incident in manager.get_open_incidents():
                self.repository.save_incident(incident)

        return manager

    def get_saved_incidents(self):
        return self.repository.get_all_incidents()

    def get_open_incidents(self):
        return self.repository.get_open_incidents()

    def get_critical_incidents(self):
        return self.repository.get_critical_incidents()

    def get_high_incidents(self):
        return self.repository.get_high_incidents()

    def close_incident(self, incident_id):
        return self.repository.close_incident(incident_id)