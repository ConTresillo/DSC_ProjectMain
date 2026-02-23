from fastapi import APIRouter

router = APIRouter()

# Minimal in-memory storage
last_action = {
    1: None,
    2: None
}

@router.post("/slots/{slot_id}/book")
def book_slot(slot_id: int):
    last_action[slot_id] = "BOOK"
    return {
        "slot_id": slot_id,
        "action": "BOOK"
    }

@router.post("/slots/{slot_id}/verify")
def verify_slot(slot_id: int):
    last_action[slot_id] = "VERIFY"
    return {
        "slot_id": slot_id,
        "action": "VERIFY"
    }

@router.post("/slots/{slot_id}/decline")
def decline_slot(slot_id: int):
    last_action[slot_id] = "DECLINE"
    return {
        "slot_id": slot_id,
        "action": "DECLINE"
    }

# This is what ESP32 will poll
@router.get("/slots/{slot_id}")
def get_slot(slot_id: int):
    return {
        "slot_id": slot_id,
        "last_action": last_action.get(slot_id)
    }