from datetime import date
from sqlalchemy import String, Date, Integer
from sqlalchemy.orm import Mapped, mapped_column
from . import DbBase


class MStudent(DbBase.DbBase):
    __tablename__ = "m_student"
    __table_args__ = {"comment": "学生マスタ"}

    name: Mapped[str] = mapped_column(String(64), comment="名前", nullable=False)
    birthday: Mapped[date] = mapped_column(Date, comment="生年月日")
    main_teacher_id: Mapped[int] = mapped_column(Integer, comment="main_teacher_id")


MStudent().metadata.create_all(DbBase.engine)
