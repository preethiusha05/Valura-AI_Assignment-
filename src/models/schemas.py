from pydantic import BaseModel
from typing import List, Dict, Optional


class ClassificationResult(BaseModel):
    intent: str
    agent: str
    entities: Dict[str, Optional[str]]
    safety_verdict: str