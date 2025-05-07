from sqlalchemy import Column, Integer, String, ForeignKey, Float, Text, Enum
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.expression import text
from ..database import Base
import datetime
import enum


class SenderEnum(str, enum.Enum):
    USER = "user"
    BOT = "bot"


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=True)
    phone_number: Mapped[str] = mapped_column(String(50), unique=True)
    phone_number_id: Mapped[str] = mapped_column(String(50), unique=True)
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=True)
    created_at: Mapped[datetime.datetime] = mapped_column(
        default=lambda: datetime.datetime.now(datetime.timezone.utc)
    )
    chat_sessions = relationship("ChatSesion", back_populates="user")


class ChatSession(Base):
    __tablename__ = "chat_sessions"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    created_at: Mapped[datetime.datetime] = mapped_column(
        default=lambda: datetime.datetime.now(datetime.timezone.utc)
    )
    finished_at: Mapped[datetime.datetime] = mapped_column()

    user = relationship("User", back_populates="chat_sesions")
    mensajes = relationship("ChatMessage", back_populates="session")


class ChatMessage(Base):
    __tablename__ = "chat_messages"

    id: Mapped[int] = mapped_column(primary_key=True, nullable=True)
    session_id: Mapped[int] = mapped_column(ForeignKey("chat_sessions.id"))
    message: Mapped[str] = mapped_column(Text)
    sender: Mapped[SenderEnum] = mapped_column(Enum(SenderEnum), nullable=False)
    created_at: Mapped[datetime.datetime] = mapped_column(
        default=lambda: datetime.datetime.now(datetime.timezone.utc)
    )

    sesion = relationship("ChatSession", back_populates="messages")
