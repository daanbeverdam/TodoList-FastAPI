from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class TodoItem(BaseModel):
    id: int
    title: str
    description: Optional[str]
    done: Optional[bool]
    created_at: Optional[datetime] = datetime.now()
    updated_at: Optional[datetime] = datetime.now()


class TodoItemIn(BaseModel):
    title: str = Field(..., min_length=1)
    done: Optional[bool]
    description: Optional[str]


class TodoItemUpdate(BaseModel):
    title: Optional[str]
    done: Optional[bool]
    description: Optional[str]