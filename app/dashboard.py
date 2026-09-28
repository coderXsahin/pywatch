import json
import urllib.request
from types import SimpleNamespace
import streamlit as st
from app.ai_analyzer import analyze_incident
API_URL = "http://127.0.0.1:8001"
def get_statistics():
    url = f"{API_URL}/statistics"
    with urllib.request.urlopen(url) as response:
        return json.loads(response.read().decode("utf-8"))
def get_incidents():
    url = f"{API_URL}/incidents"
    with urllib.request.urlopen(url) as response:
        return json.loads(response.read().decode("utf-8"))
st.set_page_config(
    page_title="PyWatch Dashboard",
    page_icon="PyWatch",
    layout="wide"
)
st.title("PyWatch")
st.subheader("Intelligent Application Monitoring & Incident Analyzer")
if st.button("Refresh Dashboard"):
    st.rerun()
statistics = get_statistics()
col1, col2, col3, col4 = st.columns(4)
col1.metric(
    "Total Incidents",
    statistics["total_incidents"]
)
col2.metric(
    "Open Incidents",
    statistics["open_incidents"]
)
col3.metric(
    "Critical Incidents",
    statistics["critical_incidents"]
)
col4.metric(
    "High Severity",
    statistics["high_incidents"]
)
st.divider()
st.subheader("Incident Overview")
incident_data = get_incidents()
incidents = incident_data["incidents"]
rows = []
for incident in incidents:
    severity = incident["severity"]
    status = incident["status"]
    if severity == "CRITICAL":
        severity_display = "[CRITICAL]"
    elif severity == "HIGH":
        severity_display = "[HIGH]"
    else:
        severity_display = severity
    if status == "OPEN":
        status_display = "[OPEN]"
    else:
        status_display = "[CLOSED]"
    rows.append({
        "ID": incident["id"],
        "Message": incident["message"],
        "Count": incident["count"],
        "Severity": severity_display,
        "Status": status_display,
        "Root Cause": incident["root_cause"]
    })
st.dataframe(
    rows,
    use_container_width=True,
    hide_index=True
)
st.divider()
st.subheader("Incident Details")
incident_options = {
    f"#{incident['id']} - {incident['message']}": incident
    for incident in incidents
}
selected_name = st.selectbox(
    "Select an incident",
    list(incident_options.keys())
)
selected_incident = incident_options[selected_name]
st.write(
    "Message:",
    selected_incident["message"]
)
st.write(
    "Severity:",
    selected_incident["severity"]
)
st.write(
    "Status:",
    selected_incident["status"]
)
st.write(
    "Occurrences:",
    selected_incident["count"]
)
st.write(
    "Root Cause:",
    selected_incident["root_cause"]
)
st.write(
    "Recommendation:",
    selected_incident["recommendation"]
)
st.divider()
st.subheader("AI Incident Analysis")

st.success("AI Engine Status: Connected")

if st.button("Analyze Incident with Gemini"):
    incident_object = SimpleNamespace(
        message=selected_incident["message"],
        count=selected_incident["count"],
        severity=selected_incident["severity"],
        status=selected_incident["status"],
        root_cause=selected_incident["root_cause"],
        recommendation=selected_incident["recommendation"]
    )
    with st.spinner("Gemini is analyzing the incident..."):
        ai_result = analyze_incident(incident_object)
    if ai_result["api_key_configured"]:
        st.write("### AI Analysis")
        st.write(ai_result["analysis"])
    else:
        st.warning(
            "Gemini API key is not configured."
        )
