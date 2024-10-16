from fastapi import APIRouter
from .TeacherReqeust import TeacherReqeust
from .TeacherResponse import TeacherResponse
from api.routes.school.StudentReqeust import StudentReqeust
from api.routes.school.StudentResponse import StudentResponse
from service.school.SchoolService import SchoolService

router = APIRouter()


@router.post("/student/new", response_model=StudentResponse)
def create_teacher(request: StudentReqeust) -> StudentResponse:
    service = SchoolService()
    response = service.create_student(request)

    return response


@router.post("/teacher/new", response_model=TeacherResponse)
def create_teacher(request: TeacherReqeust) -> TeacherResponse:
    service = SchoolService()
    response = service.create_teacher(request)

    return response


@router.post("/teacher/name", response_model=dict)
def update_teacher_name(request: TeacherReqeust) -> dict:
    service = SchoolService()
    ret = service.update_teacher_name(request.name)
    response = {"count": ret}

    return response


@router.get("/teacher/students", response_model=list[StudentResponse])
def select_students_by_techer_id(teacher_id: int) -> list[StudentResponse]:
    service = SchoolService()
    response = service.select_students_by_techer_id(teacher_id)

    return response
