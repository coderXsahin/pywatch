from app.incident_service import IncidentService


def test_get_high_incidents():
    service = IncidentService()

    incidents = service.get_high_incidents()

    assert len(incidents) >= 1

    for incident in incidents:
        assert incident.severity == "HIGH"

    assert any(
        incident.message == "Payment service unavailable"
        for incident in incidents
    )

def test_get_critical_incidents():
    service = IncidentService()

    incidents = service.get_critical_incidents()

    assert len(incidents) >= 1

    for incident in incidents:
        assert incident.severity == "CRITICAL"

    assert any(
        incident.message == "Database connection failed"
        for incident in incidents
    )

def test_get_open_incidents():
    service = IncidentService()

    incidents = service.get_open_incidents()

    for incident in incidents:
        assert incident.status == "OPEN"

def test_total_incidents():
    service = IncidentService()

    incidents = service.get_saved_incidents()

    assert len(incidents) >= 2

    messages = [incident.message for incident in incidents]

    assert "Payment service unavailable" in messages
    assert "Database connection failed" in messages

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

    count = service.repository.count_incidents()

    assert count >= 2