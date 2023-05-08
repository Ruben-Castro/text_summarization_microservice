import logging
from typing import List, Optional

from app.models.pydantic import SummaryPayloadSchema
from app.models.tortoise import TextSummary

log = logging.getLogger("uvicorn")


async def post(payload: SummaryPayloadSchema) -> int:
    summary = TextSummary(url=payload.url, summary="dummy summary")

    await summary.save()
    return summary.id


async def get(id: int) -> Optional[dict]:
    summary = await TextSummary.filter(id=id).first().values()
    log.info(f"Summary= {summary}")
    if summary:
        return summary
    return None


async def get_all() -> List:
    summaries = await TextSummary.all().values()
    return summaries


async def delete(id: int) -> int:
    summary = await TextSummary.filter(id=id).first().delete()
    return summary


async def put(id: int, payload: SummaryPayloadSchema) -> Optional[dict]:
    summary = await TextSummary.filter(id=id).update(
        url=payload.url, summary=payload.summary
    )
    if summary:
        update_summary = await TextSummary.filter(id=id).first().values()
        return update_summary
    return None
