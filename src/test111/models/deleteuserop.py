"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from test111.types import BaseModel
from test111.utils import FieldMetadata, PathParamMetadata
from typing_extensions import Annotated, TypedDict


class DeleteUserRequestTypedDict(TypedDict):
    username: str
    r"""The name that needs to be deleted"""


class DeleteUserRequest(BaseModel):
    username: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The name that needs to be deleted"""
