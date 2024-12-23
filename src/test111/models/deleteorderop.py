"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import pydantic
from test111.types import BaseModel
from test111.utils import FieldMetadata, PathParamMetadata
from typing_extensions import Annotated, TypedDict


class DeleteOrderRequestTypedDict(TypedDict):
    order_id: int
    r"""ID of the order that needs to be deleted"""


class DeleteOrderRequest(BaseModel):
    order_id: Annotated[
        int,
        pydantic.Field(alias="orderId"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""ID of the order that needs to be deleted"""
