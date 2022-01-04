from typing import Optional, Set
from pydantic import BaseModel

class Place(BaseModel):
    name: str
    description: Optional[str] = None
    
