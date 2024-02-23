from datetime import datetime
from enum import Enum
from typing import List, Optional, ClassVar
from pydantic import BaseModel, StrictStr, Field


class ParseMode(Enum):
    COMMON = "Common"
    INFO = "Info"
    POST = "Post"
    CHAT = "Chat "


class Info(BaseModel):
    value: Optional[StrictStr] = None
    parseMode: ParseMode


class ColorSchema(Enum):
    COMMON = "Guest"
    INFO = "Info"
    POST = "Post"
    CHAT = "Chat "


# class Paging(BaseModel):
#     posts_per_page: ClassVar[int] = Field(None, alias="postsPerPage")
#     comments_per_page: ClassVar[int] = Field(None, alias="commentsPerPage")
#     topics_per_page: ClassVar[int] = Field(None, alias="topicsPerPage")
#     messages_per_page: ClassVar[int] = Field(None, alias="messagesPerPage")
#     entities_per_page: ClassVar[int] = Field(None, alias="entitiesPerPage")
#
#
# class Settings(BaseModel):
#     color_schema: Optional[ColorSchema] = Field(None, alias="colorSchema")
#     nanny_greetings_message: Optional[StrictStr] = Field(None, alias="nannyGreetingsMessage")
#     paging = Optional[Paging]


class Roles(Enum):
    GUEST = "Guest"
    PLAYER = "Player"
    ADMINISTRATOR = "Administrator"
    NANNY_MODERATOR = "NannyModerator"
    REGULAR_MODERATOR = "RegularModerator"
    SENIOR_MODERATOR = "SeniorModerator"


class Rating(BaseModel):
    enabled: bool
    quality: int
    quantity: int


# class UserDetailsModel(BaseModel):
#     login: StrictStr
#     roles: List[Roles]
#     medium_picture_url: Optional[StrictStr] = Field(alias="mediumPictureUrl"), None
#     small_picture_url: Optional[StrictStr] = Field(alias="smallPictureUrl"), None
#     status: Optional[StrictStr] = None
#     rating: Rating
#     online: Optional[datetime] = None
#     name: Optional[StrictStr] = None
#     location: Optional[StrictStr] = None
#     registration: Optional[datetime] = None
#     icq: Optional[StrictStr] = None
#     skype: Optional[StrictStr] = None
#     original_picture_url: Optional[StrictStr] = Field(alias="originalPictureUrl"), None
#     info: Info
#     settings: Optional[Settings] = None


# class UserDetailsEnvelopeModel(BaseModel):
#     resource: UserDetailsModel
#     metadata: Optional[str] = None


class User(BaseModel):
    login: StrictStr
    roles: List[Roles]
    medium_picture_url: Optional[StrictStr] = Field(alias="mediumPictureUrl"), None
    small_picture_url: Optional[StrictStr] = Field(alias="smallPictureUrl"), None
    status: Optional[StrictStr] = None
    rating: Rating
    online: Optional[datetime] = None
    name: Optional[StrictStr] = None
    location: Optional[StrictStr] = None
    registration: Optional[datetime] = None


class UserEnvelopeModel(BaseModel):
    resource: User
    metadata: Optional[str] = None
