import hashlib
import json
import uuid
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.models.event import EventStore


class EventService:

    def append_event(self, db: Session, tenant_id: str, aggregate_id: str, event_type: str, payload: dict):
        # 1️⃣ Get latest version
        last_event = (
            db.query(EventStore)
            .filter(EventStore.aggregate_id == aggregate_id)
            .order_by(EventStore.version.desc())
            .first()
        )

        next_version = 1 if not last_event else last_event.version + 1
        previous_hash = last_event.hash if last_event else ""

        payload_str = json.dumps(payload, sort_keys=True)

        computed_hash = hashlib.sha256(
            (previous_hash + payload_str).encode()
        ).hexdigest()

        new_event = EventStore(
            id=uuid.uuid4(),
            tenant_id=tenant_id,
            aggregate_id=aggregate_id,
            event_type=event_type,
            payload=payload_str,
            version=next_version,
            previous_hash=previous_hash,
            hash=computed_hash
        )

        db.add(new_event)

        try:
            db.commit()
        except IntegrityError:
            db.rollback()
            raise Exception("Version conflict detected")

        return new_event
