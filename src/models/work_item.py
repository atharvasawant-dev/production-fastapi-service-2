"""Domain models for Work Items."""

from datetime import datetime
from pydantic import BaseModel, Field

class WorkItemCreate(BaseModel):
    title: str = Field(min_length=3, max_length=200)
    description: str = Field(default='', max_length=2000)

class WorkItem(WorkItemCreate):
    id: int
    created_at: datetime
