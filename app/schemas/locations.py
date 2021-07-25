from pydantic import BaseModel


class LocationKeyResponse(BaseModel):
    key: str
