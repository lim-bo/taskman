from typing import Optional

from database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import TIMESTAMP, ForeignKey


class Users:
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str]
    is_verified: Mapped[bool] = mapped_column(default=False)
    verification_token: Mapped[str]
    verification_token_expires_at: Mapped[TIMESTAMP]
    username: Mapped[str] = mapped_column(unique=True)
    password_hash: Mapped[str]
    fullname: Mapped[Optional[str]]
    role_id: Mapped[int] = mapped_column(ForeignKey("roles.id"))

    # role: Mapped["Roles"] = relationship(back_populates="users")

    def __str__(self):
        return f"Username: {self.username}, emal: {self.email}"


class Roles:
    __tablename__ = "roles"

    id: Mapped[int] = mapped_column(primary_key=True)
    role_name: Mapped[str] = mapped_column(unique=True)
    description: Mapped[Optional[str]]

    def __str__(self):
        return f"{self.role_name}; {self.description}"


class OAuthAcc:
    __tablename__ = "oauth_acc"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    provider: Mapped[str]
    provider_user_id: Mapped[str]
    access_token: Mapped[str]
    refresh_token: Mapped[str]
    created_at: Mapped[TIMESTAMP]
    expires_at: Mapped[TIMESTAMP]
    updated_at: Mapped[TIMESTAMP]


class RefreshTokens:
    __tablename__ = "refresh_tokens"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    refresh_token: Mapped[str]
    created_at: Mapped[TIMESTAMP]
    expires_at: Mapped[TIMESTAMP]
    revoked: Mapped[bool]

    def __str__(self):
        return f"{self.refresh_token}; User_id: {self.user_id}"
