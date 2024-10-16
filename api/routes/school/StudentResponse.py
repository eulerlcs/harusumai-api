from datetime import date
from typing import Union
from pydantic import BaseModel


class StudentResponse(BaseModel):
    id: int
    name: str
    birthday: Union[date, None] = None
    main_teacher_id: int
