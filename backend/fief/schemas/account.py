from typing import Optional

from pydantic import BaseModel, root_validator

from fief.db.types import DatabaseType
from fief.errors import APIErrorCode
from fief.schemas.generics import UUIDSchema


class AccountCreate(BaseModel):
    name: str
    database_type: Optional[DatabaseType]
    database_host: Optional[str]
    database_port: Optional[int]
    database_username: Optional[str]
    database_password: Optional[str]
    database_name: Optional[str]

    @root_validator
    def validate_all_database_settings(cls, values):
        database_settings = [
            values.get("database_type"),
            values.get("database_host"),
            values.get("database_port"),
            values.get("database_username"),
            values.get("database_password"),
            values.get("database_name"),
        ]
        if any(database_settings) and not all(database_settings):
            raise ValueError(APIErrorCode.ACCOUNT_CREATE_MISSING_DATABASE_SETTINGS)
        return values


class BaseAccount(UUIDSchema):
    name: str
    domain: str
    database_type: Optional[DatabaseType]
    database_host: Optional[str]
    database_port: Optional[int]
    database_username: Optional[str]
    database_password: Optional[str]
    database_name: Optional[str]


class Account(BaseAccount):
    pass


class AccountRead(BaseAccount):
    pass
