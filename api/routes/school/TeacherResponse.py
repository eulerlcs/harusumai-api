from datetime import date
from typing import Union
from pydantic import BaseModel


class TeacherResponse(BaseModel):
    id: int
    name: str
    birthday: Union[date, None] = None
