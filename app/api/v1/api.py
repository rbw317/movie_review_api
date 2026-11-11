import logging

from fastapi import APIRouter, Query

logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/search")
async def search(text: str = Query(..., min_length=1, description="Text to search for")):
    logger.info("Search requested: text=%r", text)

    results = []  

    logger.info("Search returned %d results", len(results))
    return {"query": text, "results": results}