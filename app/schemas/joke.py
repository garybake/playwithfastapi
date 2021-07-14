from typing import Optional

from pydantic import BaseModel


class JokeResponse(BaseModel):
    id: Optional[int]
    type: Optional[str]
    setup: Optional[str]
    punchline: Optional[str]
    status: str
