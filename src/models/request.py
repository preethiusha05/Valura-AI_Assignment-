from pydantic import BaseModel
from typing import List, Dict, Any

class QueryRequest(BaseModel):
    query: str
    context: Dict[str, Any] = {}
    history: List[Dict[str, Any]] = []