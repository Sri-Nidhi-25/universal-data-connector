import logging
from fastapi import HTTPException, APIRouter, Query
from app.connectors.crm_connector import CRMConnector
from app.connectors.support_connector import SupportConnector
from app.connectors.analytics_connector import AnalyticsConnector
from app.services.business_rules import apply_voice_limits
from app.services.voice_optimizer import summarize_if_large
from app.services.data_identifier import identify_data_type
from app.models.common import DataResponse, Metadata
import time
from datetime import datetime
router = APIRouter(tags=["Data"])
logger = logging.getLogger(__name__)

@router.get("/data/{source}", response_model=DataResponse)
def get_data(source: str, limit: int = Query(10, ge=1),
    optimize: bool = Query(True)):
    
    start_time = time.perf_counter()
    logger.info(f"Received request for source: {source} with limit: {limit}")

    connector_map = {
        "crm": CRMConnector(),
        "support": SupportConnector(),
        "analytics": AnalyticsConnector(),
    }

    connector = connector_map.get(source)
    if not connector:
        logger.warning(f"Invalid data source requested: {source}")
        raise HTTPException(status_code=404, detail="Invalid data source")

    try:
        raw_data = connector.fetch()
        total = len(raw_data)
        logger.debug(f"Total records fetched: {total}")
        summary = summarize_if_large(raw_data) if optimize else None
        filtered = apply_voice_limits(raw_data, limit=limit)

        data_type = identify_data_type(raw_data)

        metadata = Metadata(
            total_results=total,
            returned_results=len(filtered),
            data_freshness=f"Data as of {datetime.utcnow().isoformat()}",
        )
        response = DataResponse(
                data_type=data_type,
                data=filtered,
                summary=summary,
                metadata=metadata
            )
        duration = time.perf_counter() - start_time
        logger.info(f"Request processed successfully in {duration:.4f} seconds")

        return response
    
    except Exception as e:
        # logger.error(f"Error processing request: {str(e)}")
        logger.exception("Error processing request")
        raise HTTPException(status_code=500, detail="Internal server error")
