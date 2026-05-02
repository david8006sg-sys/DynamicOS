from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID
from app.db import get_db
from app.services.event_service import EventService
from app.schemas.event import EventCreate

router = APIRouter()

@router.post("/events")
def create_event(event: EventCreate, db: Session = Depends(get_db)):
    service = EventService()

    # ⚠️ V1: hardcoded tenant for now (will replace with JWT later)
    tenant_id = "00000000-0000-0000-0000-000000000001"

    try:
        new_event = service.append_event(
            db=db,
            tenant_id=tenant_id,
            aggregate_id=event.aggregate_id,
            event_type=event.event_type,
            payload=event.payload
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

    return {
        "event_id": str(new_event.id),
        "version": new_event.version
    }
