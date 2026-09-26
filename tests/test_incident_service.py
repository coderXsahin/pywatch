from app.incident_service import IncidentService


def test_get_high_incidents():
    service = IncidentService()

    incidents = service.get_high_incidents()

    assert len(incidents) == 1
    assert incidents[0].id == 4
    assert incidents[0].message == "Payment service unavailable"
    assert incidents[0].severity == "HIGH"

def test_get_critical_incidents():
    service = IncidentService()

    incidents = service.get_critical_incidents()

    assert len(incidents) == 1
    assert incidents[0].id == 5
    assert incidents[0].message == "Database connection failed"
    assert incidents[0].severity == "CRITICAL"

def test_get_open_incidents():
    service = IncidentService()

    incidents = service.get_open_incidents()

    for incident in incidents:
        assert incident.status == "OPEN"

def test_total_incidents():
    service = IncidentService()

    incidents = service.get_saved_incidents()

    assert len(incidents) == 2
    assert incidents[0].message == "Payment service unavailable"
    assert incidents[1].message == "Database connection failed"

def test_analyze_log_file():
    service = IncidentService()

    manager = service.analyze_log_file(
    "logs/application.log",
    threshold=3,
    save=False
    )

    incidents = manager.get_open_incidents()

    assert len(incidents) >= 1

def test_repository_count():
    service = IncidentService()

    assert service.repository.count_incidents() == 2