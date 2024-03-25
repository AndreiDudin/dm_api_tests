from typing import Optional, Dict, List
from pydantic import BaseModel, StrictStr, Extra, Field


class GeneralError(BaseModel):
    class Config:
        extra = Extra.forbid

    message: Optional[StrictStr] = Field(None, description='Client message')
