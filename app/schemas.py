from pydantic import BaseModel
from typing import Optional

class TicketPreferenceCreate(BaseModel):
    source_city: str
    destination_city: str
    max_price: float
    travel_date: str
    time_limit: Optional[str] = None
