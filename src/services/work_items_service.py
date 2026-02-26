"""Business logic for Work Items (in-memory repository)."""

import logging
from datetime import datetime
from typing import Dict, List

from src.models.work_item import WorkItem, WorkItemCreate

logger = logging.getLogger(__name__)

class WorkItemsService:
    def __init__(self) -> None:
        self._db: Dict[int, WorkItem] = {}
        self._seq = 0

    def list_items(self) -> List[WorkItem]:
        return sorted(self._db.values(), key=lambda x: x.id)

    def create_item(self, payload: WorkItemCreate) -> WorkItem:
        self._seq += 1
        item = WorkItem(id=self._seq, created_at=datetime.utcnow(), **payload.model_dump())
        self._db[item.id] = item
        logger.info('Created work_item id=%s title=%s', item.id, item.title)
        return item

    def get_item(self, item_id: int) -> WorkItem:
        if item_id not in self._db:
            raise KeyError('work_item_not_found')
        return self._db[item_id]

    def delete_item(self, item_id: int) -> None:
        if item_id not in self._db:
            raise KeyError('work_item_not_found')
        del self._db[item_id]
        logger.info('Deleted work_item id=%s', item_id)
