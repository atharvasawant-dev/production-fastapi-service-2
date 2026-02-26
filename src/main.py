"""FastAPI application entry point."""

import logging
from fastapi import FastAPI
from src.routes.health import router as health_router

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

app = FastAPI(title='Work Items API', version='1.0.0')

app.include_router(health_router)

try:
    from src.routes.work_items import router as work_items_router
    app.include_router(work_items_router, prefix='/v1')
except Exception:
    pass

try:
    from src.routes.dashboard import router as dashboard_router
    app.include_router(dashboard_router)
    from src.routes.api_metrics import router as metrics_router
    app.include_router(metrics_router, prefix='/api')
except Exception:
    pass

@app.on_event('startup')
def on_startup() -> None:
    logger.info('Application startup complete')
