from fastapi import APIRouter, Request
from sse_starlette.sse import EventSourceResponse
import json
import asyncio

from pydantic import BaseModel
from typing import List, Dict, Any

from src.guards.safety import check_safety
from src.classifier.intent_classifier import classify_intent
from src.router.dispatcher import route_request

router = APIRouter()

# -------------------------------
# Request model (for testing)
# -------------------------------
class QueryRequest(BaseModel):
    query: str
    context: Dict[str, Any] = {}
    history: List[Dict[str, Any]] = []


# -------------------------------
# SSE Streaming Endpoint (MAIN)
# -------------------------------
@router.post("/query")
async def query_endpoint(request: Request):
    body = await request.json()
    user_query = body.get("query", "")
    user_context = body.get("context", {})
    history = body.get("history", [])

    async def event_stream():
        # 1. Safety
        safety = check_safety(user_query)
        if safety["blocked"]:
            yield {"event": "error", "data": json.dumps(safety)}
            return

        yield {"event": "status", "data": "safety_passed"}

        # 2. Classification
        classification = classify_intent(user_query, history)
        yield {
            "event": "classification",
            "data": json.dumps(classification)
        }

        # 3. Routing
        result = route_request(classification, user_context)

        # 4. Stream result
        text = json.dumps(result)
        for i in range(0, len(text), 50):
            chunk = text[i:i+50]
            yield {"event": "data", "data": chunk}
            await asyncio.sleep(0.05)

        yield {"event": "end", "data": "done"}

    return EventSourceResponse(event_stream())


# -------------------------------
# TEST Endpoint (Swagger friendly)
# -------------------------------
@router.post("/query-test")
async def query_test(request: QueryRequest):

    safety = check_safety(request.query)
    if safety["blocked"]:
        return {"error": safety}

    classification = classify_intent(request.query, request.history)

    result = route_request(classification, request.context)

    return result