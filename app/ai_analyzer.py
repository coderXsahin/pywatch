import os
from dotenv import load_dotenv
from google import genai

load_dotenv()


def build_incident_prompt(incident):
    return f"""
You are an application support engineer.

Analyze the following production incident:

Incident:
{incident.message}

Occurrences:
{incident.count}

Severity:
{incident.severity}

Current status:
{incident.status}

Probable root cause:
{incident.root_cause}

Existing recommendation:
{incident.recommendation}

Provide:
1. A concise incident summary
2. Possible technical causes
3. Recommended troubleshooting steps
4. Preventive actions
"""


def analyze_incident(incident):
    prompt = build_incident_prompt(incident)

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key or api_key == "YOUR_GEMINI_KEY":
        return {
            "incident": incident.message,
            "analysis": "Gemini API key is not configured.",
            "api_key_configured": False,
            "prompt": prompt
        }

    try:
        client = genai.Client(api_key=api_key)

        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=prompt
        )

        return {
            "incident": incident.message,
            "analysis": response.text,
            "api_key_configured": True,
            "prompt": prompt
        }

    except Exception as error:
        return {
            "incident": incident.message,
            "analysis": "AI analysis temporarily unavailable.",
            "api_key_configured": True,
            "error": str(error),
            "prompt": prompt
        }