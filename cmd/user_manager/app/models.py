from datetime import datetime
from typing import Optional

from app.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import TIMESTAMP, ForeignKey


class Users(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str]
    is_verified: Mapped[bool] = mapped_column(default=False)
    verification_token: Mapped[str]
    verification_token_expires_at: Mapped[datetime] = mapped_column(TIMESTAMP)
    username: Mapped[str] = mapped_column(unique=True)
    password_hash: Mapped[str]
    fullname: Mapped[Optional[str]]
    role_id: Mapped[int] = mapped_column(ForeignKey("roles.id"))

    # role: Mapped["Roles"] = relationship(back_populates="users")

    def __str__(self):
        return f"Username: {self.username}, emal: {self.email}"


class Roles(Base):
    __tablename__ = "roles"

    id: Mapped[int] = mapped_column(primary_key=True)
    role_name: Mapped[str] = mapped_column(unique=True)
    description: Mapped[Optional[str]]

    def __str__(self):
        return f"{self.role_name}; {self.description}"


class OAuthAcc(Base):
    __tablename__ = "oauth_acc"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    provider: Mapped[str]
    provider_user_id: Mapped[str]
    access_token: Mapped[str]
    refresh_token: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(TIMESTAMP)
    expires_at: Mapped[datetime] = mapped_column(TIMESTAMP)
    updated_at: Mapped[datetime] = mapped_column(TIMESTAMP)

    # user: Mapped["Users"] = relationship(back_populates="oauth_acc")


class RefreshTokens(Base):
    __tablename__ = "refresh_tokens"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    refresh_token: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(TIMESTAMP)
    expires_at: Mapped[datetime] = mapped_column(TIMESTAMP)
    revoked: Mapped[bool]

    # user: Mapped["Users"] = relationship(back_populates="refresh_tokens")

    def __str__(self):
        return f"{self.refresh_token}; User_id: {self.user_id}"

