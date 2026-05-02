from pydantic import BaseModel
from uuid import UUID
from typing import Dict, Any

class EventCreate(BaseModel):
    aggregate_id: UUID
    event_type: str
    payload: Dict[str, Any]
