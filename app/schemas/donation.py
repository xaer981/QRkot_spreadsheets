from datetime import datetime
from typing import Optional

from pydantic import BaseModel, PositiveInt, ConfigDict


class DonationCreate(BaseModel):
    full_amount: PositiveInt
    comment: Optional[str]


class DonationRead(DonationCreate):
    id: int
    create_date: datetime

    model_config = ConfigDict(from_attributes=True)


class DonationDB(DonationRead):
    user_id: int
    invested_amount: int
    fully_invested: bool
    close_date: Optional[datetime]
