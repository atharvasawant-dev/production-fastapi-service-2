"""Work Items REST endpoints."""

import logging
from fastapi import APIRouter, HTTPException

from src.models.work_item import WorkItem, WorkItemCreate
from src.services.work_items_service import WorkItemsService

logger = logging.getLogger(__name__)
router = APIRouter(tags=['work-items'])
service = WorkItemsService()

@router.get('/work-items', response_model=list[WorkItem])
def list_work_items() -> list[WorkItem]:
    return service.list_items()

@router.post('/work-items', response_model=WorkItem, status_code=201)
def create_work_item(payload: WorkItemCreate) -> WorkItem:
    try:
        return service.create_item(payload)
    except Exception as e:
        logger.exception('Failed to create work item')
        raise HTTPException(status_code=500, detail=str(e))

@router.get('/work-items/{item_id}', response_model=WorkItem)
def get_work_item(item_id: int) -> WorkItem:
    try:
        return service.get_item(item_id)
    except KeyError:
        raise HTTPException(status_code=404, detail='Not found')

@router.delete('/work-items/{item_id}', status_code=204)
def delete_work_item(item_id: int) -> None:
    try:
        service.delete_item(item_id)
        return None
    except KeyError:
        raise HTTPException(status_code=404, detail='Not found')
