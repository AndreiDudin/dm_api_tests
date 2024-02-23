from pydantic import BaseModel, StrictStr, Field
from typing import Optional


class ChangePasswordModel(BaseModel):
    login: StrictStr
    token: StrictStr
    old_password: Optional[StrictStr] = Field(alias="oldPassword"), None
    new_password: Optional[StrictStr] = Field(alias="newPassword"), None
