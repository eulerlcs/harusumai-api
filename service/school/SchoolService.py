from db import ScopedSession, entrypoint, MTeacher, MStudent
import sqlalchemy
from sqlalchemy.orm import Session
from api.routes.school.StudentReqeust import StudentReqeust
from api.routes.school.StudentResponse import StudentResponse
from api.routes.school.TeacherReqeust import TeacherReqeust
from api.routes.school.TeacherResponse import TeacherResponse


class SchoolService:

    @entrypoint
    def create_student(self, request: StudentReqeust) -> StudentResponse:
        session: Session = ScopedSession()
        with session.begin_nested():
            item = MStudent(
                name=request.name,
                birthday=request.birthday,
                main_teacher_id=request.main_teacher_id,
            )
            session.add(item)
            session.flush()

            response = StudentResponse(
                id=item.id,
                name=item.name,
                birthday=item.birthday,
                main_teacher_id=item.main_teacher_id,
            )
            return response

    @entrypoint
    def create_teacher(self, request: TeacherReqeust) -> TeacherResponse:
        session: Session = ScopedSession()
        with session.begin_nested():
            item = MTeacher(name=request.name, birthday=request.birthday)
            session.add(item)
            session.flush()

            response = TeacherResponse(
                id=item.id, name=item.name, birthday=item.birthday
            )
            return response

    @entrypoint
    def update_teacher_name(self, name: str) -> int:
        session: Session = ScopedSession()
        with session.begin_nested():
            query = sqlalchemy.text(f"update {MTeacher.__tablename__} set name = :name")
            result = session.execute(query, {"name": name})

            return result.rowcount

    def select_students_by_techer_id(self, teacher_id: int) -> list[StudentResponse]:
        session: Session = ScopedSession()
        with session.begin_nested():
            query = sqlalchemy.text(
                f"""
select 
    s.id, s.name, s.birthday, s.main_teacher_id 
from 
    {MStudent.__tablename__} s inner join {MTeacher.__tablename__} t 
    on s.main_teacher_id = t.id
where
    s.main_teacher_id = :main_teacher_id
"""
            )

            results = (
                session.execute(query, {"main_teacher_id": teacher_id}).mappings().all()
            )

            response = []
            for result in results:
                item = StudentResponse(
                    id=result["id"],
                    name=result["name"],
                    birthday=result["birthday"],
                    main_teacher_id=result["main_teacher_id"],
                )

                response.append(item)

            return response
