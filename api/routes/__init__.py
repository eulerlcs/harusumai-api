from fastapi import APIRouter
from .school.SchoolApi import router as hello_router


router = APIRouter()

router.include_router(router=hello_router, prefix="/school")
