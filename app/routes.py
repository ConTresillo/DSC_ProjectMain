from fastapi import APIRouter

router = APIRouter()

@router.post("/slots/{slot_id}/book")
def book_slot(slot_id: int):
    return {
        "slot_id": slot_id,
        "action": "BOOK",
        "status": "received"
    }

@router.post("/slots/{slot_id}/verify")
def verify_slot(slot_id: int):
    return {
        "slot_id": slot_id,
        "action": "VERIFY",
        "status": "received"
    }

@router.post("/slots/{slot_id}/decline")
def decline_slot(slot_id: int):
    return {
        "slot_id": slot_id,
        "action": "DECLINE",
        "status": "received"
    }