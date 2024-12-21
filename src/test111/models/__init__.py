"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .apierror import APIError
from .apierrorinvalidinput import APIErrorInvalidInput, APIErrorInvalidInputData
from .apierrornotfound import APIErrorNotFound, APIErrorNotFoundData
from .apierrorunauthorized import APIErrorUnauthorized, APIErrorUnauthorizedData
from .apiresponse import APIResponse, APIResponseTypedDict
from .category import Category, CategoryTypedDict
from .deleteorderop import DeleteOrderRequest, DeleteOrderRequestTypedDict
from .deletepetop import DeletePetRequest, DeletePetRequestTypedDict
from .deleteuserop import DeleteUserRequest, DeleteUserRequestTypedDict
from .findpetsbystatusop import (
    FindPetsByStatusRequest,
    FindPetsByStatusRequestTypedDict,
    QueryParamStatus,
)
from .findpetsbytagsop import FindPetsByTagsRequest, FindPetsByTagsRequestTypedDict
from .getorderbyidop import GetOrderByIDRequest, GetOrderByIDRequestTypedDict
from .getpetbyidop import GetPetByIDRequest, GetPetByIDRequestTypedDict
from .getuserbynameop import GetUserByNameRequest, GetUserByNameRequestTypedDict
from .loginuserop import (
    LoginUserRequest,
    LoginUserRequestTypedDict,
    LoginUserResponse,
    LoginUserResponseTypedDict,
)
from .order import Order, OrderStatus, OrderTypedDict
from .pet import Pet, PetTypedDict, Status
from .security import Security, SecurityTypedDict
from .tag import Tag, TagTypedDict
from .updateuserop import UpdateUserRequest, UpdateUserRequestTypedDict
from .uploadfileop import UploadFileRequest, UploadFileRequestTypedDict
from .user import User, UserTypedDict

__all__ = [
    "APIError",
    "APIErrorInvalidInput",
    "APIErrorInvalidInputData",
    "APIErrorNotFound",
    "APIErrorNotFoundData",
    "APIErrorUnauthorized",
    "APIErrorUnauthorizedData",
    "APIResponse",
    "APIResponseTypedDict",
    "Category",
    "CategoryTypedDict",
    "DeleteOrderRequest",
    "DeleteOrderRequestTypedDict",
    "DeletePetRequest",
    "DeletePetRequestTypedDict",
    "DeleteUserRequest",
    "DeleteUserRequestTypedDict",
    "FindPetsByStatusRequest",
    "FindPetsByStatusRequestTypedDict",
    "FindPetsByTagsRequest",
    "FindPetsByTagsRequestTypedDict",
    "GetOrderByIDRequest",
    "GetOrderByIDRequestTypedDict",
    "GetPetByIDRequest",
    "GetPetByIDRequestTypedDict",
    "GetUserByNameRequest",
    "GetUserByNameRequestTypedDict",
    "LoginUserRequest",
    "LoginUserRequestTypedDict",
    "LoginUserResponse",
    "LoginUserResponseTypedDict",
    "Order",
    "OrderStatus",
    "OrderTypedDict",
    "Pet",
    "PetTypedDict",
    "QueryParamStatus",
    "Security",
    "SecurityTypedDict",
    "Status",
    "Tag",
    "TagTypedDict",
    "UpdateUserRequest",
    "UpdateUserRequestTypedDict",
    "UploadFileRequest",
    "UploadFileRequestTypedDict",
    "User",
    "UserTypedDict",
]