from fastapi import FastAPI
app = FastAPI(
    title="PyWatch API",
    description="Application monitoring and incident analysis API",
    version="1.0.0"
)
@app.get("/")
def home():
    return {
        "application": "PyWatch",
        "status": "running"
    }
@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }
@app.get("/incidents")
def get_incidents():
    from app.incident_service import IncidentService

    service = IncidentService()
    incidents = service.get_saved_incidents()

    return {
        "total_incidents": service.repository.count_incidents(),
        "incidents": [
            {
                "id": incident.id,
                "message": incident.message,
                "count": incident.count,
                "severity": incident.severity,
                "status": incident.status,
                "root_cause": incident.root_cause,
                "recommendation": incident.recommendation,
                "created_at": incident.created_at,
                "closed_at": incident.closed_at
            }
            for incident in incidents
        ]
    }
@app.get("/statistics")
def get_statistics():
    from app.incident_service import IncidentService

    service = IncidentService()
    incidents = service.get_open_incidents()
    total_incidents = service.repository.count_incidents()

    open_incidents = len(incidents)
    
    critical_incidents = len(service.get_critical_incidents())
    high_incidents = len(service.get_high_incidents())

    return {
        "total_incidents": total_incidents,
        "open_incidents": open_incidents,
        "critical_incidents": critical_incidents,
        "high_incidents": high_incidents
    }
@app.get("/incidents/high")
def get_high_incidents():
    from app.incident_service import IncidentService

    service = IncidentService()
    incidents = service.get_high_incidents()

    return {
        "total_high_incidents": len(incidents),
        "incidents": [
            {
                "id": incident.id,
                "message": incident.message,
                "count": incident.count,
                "severity": incident.severity,
                "status": incident.status,
                "root_cause": incident.root_cause,
                "recommendation": incident.recommendation
            }
            for incident in incidents
        ]
    }
@app.get("/incidents/critical")
def get_critical_incidents():
    from app.incident_service import IncidentService

    service = IncidentService()
    incidents = service.get_critical_incidents()

    return {
        "total_critical_incidents": len(incidents),
        "incidents": [
            {
                "id": incident.id,
                "message": incident.message,
                "count": incident.count,
                "severity": incident.severity,
                "status": incident.status,
                "root_cause": incident.root_cause,
                "recommendation": incident.recommendation
            }
            for incident in incidents
        ]
    }
@app.get("/monitor/status")
def monitor_status():
    return {
        "monitor": "PyWatch Monitor",
        "status": "active",
        "interval_seconds": 5
    }
@app.post("/monitor/check")
def run_monitor_check():
    from app.monitor import Monitor

    monitor = Monitor()
    incidents = monitor.check()

    critical_count = sum(
        1 for incident in incidents
        if incident.severity == "CRITICAL"
    )

    high_count = sum(
        1 for incident in incidents
        if incident.severity == "HIGH"
    )

    return {
        "total_incidents": len(incidents),
        "critical_incidents": critical_count,
        "high_incidents": high_count,
        "incidents": [incident.to_dict() for incident in incidents]
    }
@app.get("/monitor/summary")
def monitor_summary():
    from app.monitor import Monitor

    monitor = Monitor()
    incidents = monitor.check()

    critical_count = sum(
        1 for incident in incidents
        if incident.severity == "CRITICAL"
    )

    high_count = sum(
        1 for incident in incidents
        if incident.severity == "HIGH"
    )

    return {
        "monitor_status": "active",
        "total_open_incidents": len(incidents),
        "critical_incidents": critical_count,
        "high_incidents": high_count
    }

@app.put("/incidents/{incident_id}/close")
def close_incident(incident_id: int):
    from app.incident_repository import IncidentRepository

    repository = IncidentRepository()
    incident = repository.close_incident(incident_id)

    if incident is None:
        return {
            "status": "error",
            "message": "Incident not found"
        }

    return {
        "status": "success",
        "message": "Incident closed successfully",
        "incident": {
            "id": incident.id,
            "message": incident.message,
            "severity": incident.severity,
            "status": incident.status
        }
    }
