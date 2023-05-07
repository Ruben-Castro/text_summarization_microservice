import logging

from typing import Optional
from app.models.pydantic import SummaryPayloadSchema
from app.models.tortoise import TextSummary

log = logging.getLogger("uvicorn")

async def post(payload:SummaryPayloadSchema) -> int:
    summary = TextSummary(
        url=payload.url,
        summary="dummy summary"
    )

    await summary.save()
    return summary.id

async def get(id:int) -> Optional[dict]:
    summary = await TextSummary.filter(id= id).first().values()
    log.info(f"Summary= {summary}")
    if summary:
        return summary
    return None 