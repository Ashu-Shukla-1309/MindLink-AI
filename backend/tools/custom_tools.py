import time

def lookup_order(order_id: str):
    time.sleep(0.1)
    return {
        "order_id": order_id,
        "status": "Delivered",
        "delivered_at": "2025-11-15T10:23:00Z",
        "notes": "Left at front door"
    }
