# PyWatch — Intelligent Application Monitoring & Incident Analyzer



PyWatch is a Python-based application monitoring and incident-analysis platform designed to help support engineers detect recurring application failures, classify incidents, identify probable root causes, and generate troubleshooting recommendations.



It combines log analysis, REST APIs, PostgreSQL persistence, automated monitoring, a Streamlit dashboard, and Gemini-powered AI incident analysis.



## Architecture



```text

Application

&#x20;    â†“

Application Logs

&#x20;    â†“

Log Parser

&#x20;    â†“

Incident Detection

&#x20;    â†“

Severity Classification

&#x20;    â†“

Root Cause + Recommendation

&#x20;    â†“

PostgreSQL

&#x20;    â†“

FastAPI

&#x20;    â†“

Streamlit Dashboard

&#x20;    â†“

Gemini AI Analysis

```



## Key Features



\* Application log parsing

\* Recurring incident detection

\* Incident severity classification

\* Probable root-cause generation

\* Troubleshooting recommendations

\* PostgreSQL persistence using SQLAlchemy

\* Incident deduplication

\* OPEN â†’ CLOSED â†’ OPEN incident lifecycle

\* FastAPI REST APIs

\* Monitoring and health-check endpoints

\* Streamlit monitoring dashboard

\* Gemini-powered AI incident analysis

\* Automated regression testing with Pytest

\* Docker and Docker Compose support



## Technology Stack



| Area             | Technology             |

| ---------------- | ---------------------- |

| Language         | Python                 |

| Backend API      | FastAPI                |

| Database         | PostgreSQL             |

| ORM              | SQLAlchemy             |

| Validation       | Pydantic               |

| AI               | Google Gemini API      |

| Dashboard        | Streamlit              |

| Testing          | Pytest                 |

| Containerization | Docker, Docker Compose |

| Version Control  | Git, GitHub            |



## Project Structure



```text

pywatch/

â”‚

â”œâ”€â”€ app/

â”‚   â”œâ”€â”€ ai\_analyzer.py

â”‚   â”œâ”€â”€ api.py

â”‚   â”œâ”€â”€ dashboard.py

â”‚   â”œâ”€â”€ database.py

â”‚   â”œâ”€â”€ incident.py

â”‚   â”œâ”€â”€ incident\_manager.py

â”‚   â”œâ”€â”€ incident\_repository.py

â”‚   â”œâ”€â”€ incident\_service.py

â”‚   â”œâ”€â”€ log\_analyzer.py

â”‚   â”œâ”€â”€ log\_parser.py

â”‚   â”œâ”€â”€ main.py

â”‚   â”œâ”€â”€ models.py

â”‚   â”œâ”€â”€ monitor.py

â”‚   â”œâ”€â”€ recommendation.py

â”‚   â”œâ”€â”€ report\_generator.py

â”‚   â”œâ”€â”€ root\_cause.py

â”‚   â””â”€â”€ scheduler.py

â”‚

â”œâ”€â”€ logs/

â”œâ”€â”€ reports/

â”œâ”€â”€ tests/

â”œâ”€â”€ .gitignore

â”œâ”€â”€ docker-compose.yml

â”œâ”€â”€ Dockerfile

â”œâ”€â”€ requirements.txt

â””â”€â”€ README.md

```



## Incident Lifecycle



PyWatch avoids creating duplicate records when an already-known incident occurs again.



```text

New incident

&#x20;    â†“

Check existing incident

&#x20;    â†“

Existing CLOSED incident?

&#x20;    â†“

Yes â†’ Reopen existing incident

&#x20;    â†“

OPEN

```



This allows recurring failures to be tracked without unnecessarily creating duplicate incident records.



## API Endpoints



| Endpoint                         | Method | Purpose                          |

| -------------------------------- | ------ | -------------------------------- |

| `/`                              | GET    | API information                  |

| `/health`                        | GET    | Application health check         |

| `/incidents`                     | GET    | Retrieve incidents               |

| `/statistics`                    | GET    | Incident statistics              |

| `/incidents/high`                | GET    | Retrieve HIGH severity incidents |

| `/incidents/critical`            | GET    | Retrieve CRITICAL incidents      |

| `/monitor/status`                | GET    | Monitoring status                |

| `/monitor/check`                 | POST   | Run a monitoring check           |

| `/monitor/summary`               | GET    | Monitoring summary               |

| `/incidents/{incident\_id}/close` | PUT    | Close an incident                |



Interactive API documentation is available through FastAPI Swagger UI at:



```text

http://127.0.0.1:8001/docs

```



## Local Setup



### 1. Clone the repository



```bash

git clone https://github.com/coderXsahin/pywatch.git

cd pywatch

```



### 2. Create a virtual environment



Windows PowerShell:



```powershell

python -m venv .venv

.venv\\Scripts\\Activate.ps1

```



### 3. Install dependencies



```powershell

pip install -r requirements.txt

```



### 4. Configure environment variables



Create a `.env` file:



```env

GEMINI\_API\_KEY=your\_gemini\_api\_key

DATABASE\_URL=your\_database\_connection\_string

POSTGRES\_PASSWORD=your\_postgres\_password

```



Do not commit `.env` to GitHub.



## Running with Docker



Start the application and PostgreSQL:



```powershell

docker compose up -d --build

```



Check services:



```powershell

docker compose ps

```



The API is exposed on:



```text

http://127.0.0.1:8001

```



Health check:



```text

http://127.0.0.1:8001/health

```



Swagger documentation:



```text

http://127.0.0.1:8001/docs

```



## Running the Dashboard



With the Docker API running:



```powershell

python -m streamlit run app\\dashboard.py

```



The dashboard is available at:



```text

http://localhost:8501

```



The dashboard displays:



\* Total incidents

\* Open incidents

\* Critical incidents

\* High-severity incidents

\* Incident details

\* Root-cause information

\* Troubleshooting recommendations

\* Gemini AI incident analysis



## Running Tests



Run the automated test suite:



```powershell

python -m pytest -q

```



Current test result:



```text

6 passed

```



## Example Incident



Example detected incident:



```text

Message:

Database connection failed



Severity:

CRITICAL



Occurrences:

3



Status:

OPEN

```



PyWatch generates a probable root cause and troubleshooting recommendation and can send the incident context to Gemini for additional technical analysis.



## AI Incident Analysis



Gemini is used as an AI-assisted support layer.



For a detected incident, PyWatch provides Gemini with:



\* Incident message

\* Number of occurrences

\* Severity

\* Current status

\* Probable root cause

\* Existing recommendation



The AI response provides:



1\. Incident summary

2\. Possible technical causes

3\. Recommended troubleshooting steps

4\. Preventive actions



The AI output is intended as troubleshooting assistance rather than a definitive production root-cause determination.



## Screenshots



### Monitoring Dashboard



The Streamlit dashboard provides an overview of incidents, severity, status, root causes, and AI-assisted analysis.



### FastAPI Swagger Documentation



The FastAPI Swagger interface provides interactive access to the PyWatch REST API.



## Engineering Highlights



\* Designed a modular Python application with separated monitoring, analysis, persistence, API, and presentation layers.

\* Implemented database-backed incident persistence using SQLAlchemy.

\* Added incident deduplication and lifecycle handling for recurring failures.

\* Built REST APIs for monitoring and incident management.

\* Integrated an external generative-AI service for support-oriented incident analysis.

\* Containerized the API and PostgreSQL environment using Docker Compose.

\* Added automated regression tests using Pytest.



## Future Improvements



Potential extensions include:



\* Authentication and role-based access control

\* Incident history/event tracking

\* Configurable alert thresholds

\* Metrics and alerting integrations

\* Database migrations with Alembic

\* More advanced anomaly detection

\* CI/CD automation

\* Production observability integrations



## Author



\*\*Sahin Khatoon\*\*



PyWatch was developed as a portfolio project demonstrating Python application development, application support engineering, troubleshooting, REST API development, database integration, AI-assisted analysis, testing, and containerization.




