from datetime import datetime
from enum import Enum
from typing import List, Optional, ClassVar, Any
from pydantic import BaseModel, StrictStr, Field, Extra


class UserRole(Enum):
    guest = 'Guest'
    player = 'Player'
    administrator = 'Administrator'
    nanny_moderator = 'NannyModerator'
    regular_moderator = 'RegularModerator'
    senior_moderator = 'SeniorModerator'


class Rating(BaseModel):
    class Config:
        extra = Extra.forbid

    enabled: Optional[bool] = Field(None, description='Rating participation flag')
    quality: Optional[int] = Field(None, description='Quality rating')
    quantity: Optional[int] = Field(None, description='Quantity rating')


class User(BaseModel):
    class Config:
        extra = Extra.forbid

    login: Optional[StrictStr] = Field(None, description='Login')
    roles: Optional[List[UserRole]] = Field(None, description='Roles')
    medium_picture_url: Optional[StrictStr] = Field(
        None, alias='mediumPictureUrl', description='Profile picture URL M-size'
    )
    small_picture_url: Optional[StrictStr] = Field(
        None, alias='smallPictureUrl', description='Profile picture URL S-size'
    )
    status: Optional[StrictStr] = Field(None, description='User defined status')
    rating: Optional[Rating] = None
    online: Optional[datetime] = Field(None, description='Last seen online moment')
    name: Optional[StrictStr] = Field(None, description='User real name')
    location: Optional[StrictStr] = Field(None, description='User real location')
    registration: Optional[datetime] = Field(
        None, description='User registration moment'
    )


class UserEnvelope(BaseModel):
    class Config:
        extra = Extra.forbid

    resource: Optional[User] = None
    metadata: Optional[Any] = Field(None, description='Additional metadata')

# class UserRole(Enum):
#     GUEST = "Guest"
#     PLAYER = "Player"
#     ADMINISTRATOR = "Administrator"
#     NANNY_MODERATOR = "NannyModerator"
#     REGULAR_MODERATOR = "RegularModerator"
#     SENIOR_MODERATOR = "SeniorModerator"
#
#
# class Rating(BaseModel):
#     enabled: Optional[bool]
#     quality: Optional[int]
#     quantity: Optional[int]
#
#
# class User(BaseModel):
#     login: Optional[StrictStr] = Field(None, description="Login")
#     roles: Optional[List[UserRole]]
#     medium_picture_url: Optional[StrictStr] = Field(None, alias="mediumPictureUrl")
#     small_picture_url: Optional[StrictStr] = Field(None, alias="smallPictureUrl")
#     status: Optional[StrictStr] = None
#     rating: Optional[Rating] = None
#     online: Optional[datetime] = None
#     name: Optional[StrictStr] = None
#     location: Optional[StrictStr] = None
#     registration: Optional[datetime] = None
#
#
# class ParseMode(Enum):
#     COMMON = "Common"
#     INFO = "Info"
#     POST = "Post"
#     CHAT = "Chat "
#
#
# class Info(BaseModel):
#     value: Optional[StrictStr] = None
#     parseMode: ParseMode
#
#
# class ColorSchema(Enum):
#     COMMON = "Guest"
#     INFO = "Info"
#     POST = "Post"
#     CHAT = "Chat "
#
#
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
#
#
# # class UserDetailsModel(BaseModel):
# #     login: StrictStr
# #     roles: List[Roles]
# #     medium_picture_url: Optional[StrictStr] = Field(alias="mediumPictureUrl"), None
# #     small_picture_url: Optional[StrictStr] = Field(alias="smallPictureUrl"), None
# #     status: Optional[StrictStr] = None
# #     rating: Rating
# #     online: Optional[datetime] = None
# #     name: Optional[StrictStr] = None
# #     location: Optional[StrictStr] = None
# #     registration: Optional[datetime] = None
# #     icq: Optional[StrictStr] = None
# #     skype: Optional[StrictStr] = None
# #     original_picture_url: Optional[StrictStr] = Field(alias="originalPictureUrl"), None
# #     info: Info
# #     settings: Optional[Settings] = None
#
#
# # class UserDetailsEnvelopeModel(BaseModel):
# #     resource: UserDetailsModel
# #     metadata: Optional[str] = None
#
#
# class UserEnvelopeModel(BaseModel):
#     resource: User
#     metadata: Optional[str] = None
