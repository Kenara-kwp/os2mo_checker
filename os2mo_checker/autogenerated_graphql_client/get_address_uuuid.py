from datetime import datetime
from typing import List, Optional
from uuid import UUID

from pydantic import Field

from .base_model import BaseModel


class GetAddressUuuid(BaseModel):
    addresses: "GetAddressUuuidAddresses"


class GetAddressUuuidAddresses(BaseModel):
    objects: List["GetAddressUuuidAddressesObjects"]


class GetAddressUuuidAddressesObjects(BaseModel):
    current: Optional["GetAddressUuuidAddressesObjectsCurrent"]


class GetAddressUuuidAddressesObjectsCurrent(BaseModel):
    uuid: UUID
    ituser_response: Optional["GetAddressUuuidAddressesObjectsCurrentItuserResponse"]


class GetAddressUuuidAddressesObjectsCurrentItuserResponse(BaseModel):
    current: Optional["GetAddressUuuidAddressesObjectsCurrentItuserResponseCurrent"]


class GetAddressUuuidAddressesObjectsCurrentItuserResponseCurrent(BaseModel):
    user_key: str
    uuid: UUID
    validity: "GetAddressUuuidAddressesObjectsCurrentItuserResponseCurrentValidity"


class GetAddressUuuidAddressesObjectsCurrentItuserResponseCurrentValidity(BaseModel):
    from_: datetime = Field(alias="from")
    to: Optional[datetime]


GetAddressUuuid.update_forward_refs()
GetAddressUuuidAddresses.update_forward_refs()
GetAddressUuuidAddressesObjects.update_forward_refs()
GetAddressUuuidAddressesObjectsCurrent.update_forward_refs()
GetAddressUuuidAddressesObjectsCurrentItuserResponse.update_forward_refs()
GetAddressUuuidAddressesObjectsCurrentItuserResponseCurrent.update_forward_refs()
GetAddressUuuidAddressesObjectsCurrentItuserResponseCurrentValidity.update_forward_refs()
