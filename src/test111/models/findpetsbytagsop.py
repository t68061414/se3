"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from test111.types import BaseModel
from test111.utils import FieldMetadata, QueryParamMetadata
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class FindPetsByTagsRequestTypedDict(TypedDict):
    tags: NotRequired[List[str]]
    r"""Tags to filter by"""


class FindPetsByTagsRequest(BaseModel):
    tags: Annotated[
        Optional[List[str]],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Tags to filter by"""
