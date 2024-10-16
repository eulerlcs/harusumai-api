from datetime import date
from sqlalchemy import String, Date
from sqlalchemy.orm import Mapped, mapped_column
from . import DbBase


class MTeacher(DbBase.DbBase):
    __tablename__ = "m_teacher"
    __table_args__ = {"comment": "先生マスタ"}

    name: Mapped[str] = mapped_column(String(64), comment="名前", nullable=False)
    birthday: Mapped[date] = mapped_column(Date, comment="生年月日")


MTeacher().metadata.create_all(DbBase.engine)
