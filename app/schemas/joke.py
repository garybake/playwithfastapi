from typing import Optional

from pydantic import BaseModel


class JokeResponse(BaseModel):
    id: Optional[int]
    the_joke: Optional[str]
    the_punchline: Optional[str]
