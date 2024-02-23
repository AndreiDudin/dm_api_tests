from pydantic import BaseModel, StrictStr, Field
from typing import Optional


class LoginCredentialsModel(BaseModel):
    login: StrictStr
    password: Optional[StrictStr] = None
    remember_me: Optional[StrictStr] = Field(alias="rememberMe"), None
