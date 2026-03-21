from datetime import datetime

from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserUpdate(BaseModel):
    email: EmailStr | None = None


class UserResponse(BaseModel):
    id: str
    email: EmailStr
    is_active: bool
    is_superuser: bool
    created_at: datetime

    model_config = {"from_attributes": True}
    # from_attributes=True lets Pydantic read from ORM objects
    # without it: UserResponse(**user.__dict__) would fail
    # with it:    UserResponse.model_validate(user) works perfectly


