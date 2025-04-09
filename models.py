import os

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import func, String, DateTime, Integer
from dotenv import load_dotenv
from datetime import datetime

load_dotenv() # laod envs

DATABASE_URL = os.getenv("DEV_DATABASE_URL")

class Base(DeclarativeBase):
    pass


class Ro(Base):
    __tablename__ = 'ro'
    __table_args__ = {'schema': 'spreed'}
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    cpf: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    age: Mapped[int] = mapped_column(Integer, nullable=True)
    date_year: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    gender: Mapped[str] = mapped_column(String, nullable=True)
    uf: Mapped[str] = mapped_column(String(2), nullable=True)
    cep: Mapped[str] = mapped_column(String, nullable=True)
    phone_base: Mapped[str] = mapped_column(String, nullable=True)
    dd_one: Mapped[str] = mapped_column(String(3), nullable=True)
    phone_one: Mapped[str] = mapped_column(String, nullable=True)
    have_whatsapp_one: Mapped[str] = mapped_column(String, nullable=True)
    dd_two: Mapped[str] = mapped_column(String(3), nullable=True)
    phone_two: Mapped[str] = mapped_column(String, nullable=True)
    have_whatsapp_two: Mapped[str] = mapped_column(String, nullable=True)
    email: Mapped[str] = mapped_column(String, nullable=True)
    email_two: Mapped[str] = mapped_column(String, nullable=True)
    email_three: Mapped[str] = mapped_column(String, nullable=True)
    create_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, server_default=func.now())

    def __repr__(self):
        return f"<Ro cpf={self.cpf} uf={self.uf}>"
