import os
from datetime import date, datetime
from sqlalchemy import create_engine, Integer, String, DateTime, func
from sqlalchemy.orm import DeclarativeBase, declarative_base, Mapped, mapped_column


__db_host = os.getenv("DB_HOST", "localhost")
__db_port = int(os.getenv("DB_PORT", 5432))
__db_username = os.getenv("DB_USERNAME", "euler")
__db_password = os.getenv("DB_PASSWORD", "12345678")
__db_database = os.getenv("DB_DATABASE", "vectordb")
__mode = os.getenv("MODE", "dev")

url = f"postgresql+psycopg://{__db_username}:{__db_password}@{__db_host}:{__db_port}/{__db_database}"
engine = create_engine(url, echo=(__mode == "dev"))


class DbBase(DeclarativeBase):
    id: Mapped[int] = mapped_column(
        Integer, comment="id", primary_key=True, sort_order=-10
    )

    create_id: Mapped[datetime] = mapped_column(
        String, comment="作成者", server_default=""
    )
    create_date: Mapped[datetime] = mapped_column(
        DateTime, comment="作成年月日", server_default=func.current_timestamp()
    )
    update_id: Mapped[str] = mapped_column(String, comment="更新者", server_default="")
    update_date: Mapped[datetime] = mapped_column(
        DateTime, comment="更新年月日", server_default=func.current_timestamp()
    )
