
from pydantic import BaseModel
from typing import Dict, List, Optional

class Metadata(BaseModel):
    total_results: int
    returned_results: int
    data_freshness: str

class DataResponse(BaseModel):
    data_type: str
    # data: List[Any]
    summary: Optional[Dict] = None
    data: List[Dict]
    metadata: Metadata
