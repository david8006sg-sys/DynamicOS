from sqlalchemy import Column, String, Integer, DateTime, Text
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER
from datetime import datetime
import uuid
from app.db import Base


class EventStore(Base):
    __tablename__ = "event_store"

    id = Column(UNIQUEIDENTIFIER, primary_key=True, default=uuid.uuid4)
    tenant_id = Column(UNIQUEIDENTIFIER, nullable=False)
    aggregate_id = Column(UNIQUEIDENTIFIER, nullable=False)
    event_type = Column(String(100), nullable=False)
    payload = Column(Text, nullable=False)
    version = Column(Integer, nullable=False)
    previous_hash = Column(String(64))
    hash = Column(String(64), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
