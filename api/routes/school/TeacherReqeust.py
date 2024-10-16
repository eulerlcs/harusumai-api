from datetime import date
from typing import Union
from pydantic import BaseModel


class TeacherReqeust(BaseModel):
    name: str
    birthday: Union[date, None] = None
