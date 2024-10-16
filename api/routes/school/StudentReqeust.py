from datetime import date
from typing import Union
from pydantic import BaseModel


class StudentReqeust(BaseModel):
    name: str
    birthday: Union[date, None] = None
    main_teacher_id: int
