"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import pydantic
from test111.types import BaseModel
from test111.utils import FieldMetadata, HeaderMetadata, PathParamMetadata
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class DeletePetRequestTypedDict(TypedDict):
    pet_id: int
    r"""Pet id to delete"""
    api_key: NotRequired[str]


class DeletePetRequest(BaseModel):
    pet_id: Annotated[
        int,
        pydantic.Field(alias="petId"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""Pet id to delete"""

    api_key: Annotated[
        Optional[str],
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = None
