
from typing import List, Dict
from app.config import settings

def apply_voice_limits(data: List[Dict], limit: int) -> List[Dict]:

    if not data:
        return []

    sample = data[0]

    # Prioritize recent items if timestamp exists
    if "created_at" in sample:
        data = sorted(
            data,
            key=lambda x: x.get("created_at", ""),
            reverse=True
        )
    # Validate limit
    if limit is None or limit < 1:
        limit = settings.MAX_RESULTS
    effective_limit = min(limit, settings.MAX_RESULTS)

    return data[:effective_limit]
