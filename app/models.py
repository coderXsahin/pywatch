from sqlalchemy import Column, Integer, String, Text
from app.database import Base


class IncidentModel(Base):
    __tablename__ = "incidents"

    id = Column(Integer, primary_key=True, index=True)
    message = Column(String(255), nullable=False)
    count = Column(Integer, nullable=False)
    severity = Column(String(20), nullable=False)
    status = Column(String(20), nullable=False)
    root_cause = Column(Text, nullable=False)
    recommendation = Column(Text, nullable=False)