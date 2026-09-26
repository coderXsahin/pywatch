from datetime import datetime
from app import incident
from app.database import SessionLocal
from app.models import IncidentModel


class IncidentRepository:

    def save_incident(self, incident):
        session = SessionLocal()

        try:
            existing = session.query(IncidentModel).filter_by(
                message=incident.message,
                count=incident.count,
                severity=incident.severity,
                status=incident.status
            ).first()

            if existing:
                return existing

            db_incident = IncidentModel(
            message=incident.message,
            count=incident.count,
            severity=incident.severity,
            status=incident.status,
            root_cause=incident.root_cause,
            recommendation=incident.recommendation,
            created_at=datetime.now(),
            closed_at=None
            )

            session.add(db_incident)
            session.commit()
            session.refresh(db_incident)

            return db_incident

        finally:
            session.close()

    def get_all_incidents(self):
        session = SessionLocal()

        try:
            return session.query(IncidentModel).all()

        finally:
            session.close()

    def count_incidents(self):
        session = SessionLocal()

        try:
            return session.query(IncidentModel).count()

        finally:
            session.close()

    def get_open_incidents(self):
        session = SessionLocal()

        try:
            return session.query(IncidentModel).filter_by(
                status="OPEN"
            ).all()

        finally:
            session.close()

    def get_critical_incidents(self):
        session = SessionLocal()

        try:
            return session.query(IncidentModel).filter_by(
                severity="CRITICAL"
            ).all()

        finally:
            session.close()

    def get_high_incidents(self):
        session = SessionLocal()

        try:
            return session.query(IncidentModel).filter_by(
                severity="HIGH"
            ).all()

        finally:
            session.close()

    def close_incident(self, incident_id):
        session = SessionLocal()

        try:
            incident = session.query(IncidentModel).filter_by(
                id=incident_id
            ).first()

            if incident is None:
                return None

            incident.status = "CLOSED"
            incident.closed_at = datetime.now()

            session.commit()
            session.refresh(incident)

            return incident

        finally:
            session.close()