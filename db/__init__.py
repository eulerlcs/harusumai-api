from . import DbBase
from .MStudent import MStudent
from .MTeacher import MTeacher

from functools import wraps
from typing import Any, Callable
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, scoped_session, sessionmaker, Session


#### ref: https://github.com/take0a/fastapi-sample
#### ref: https://zenn.dev/robon/articles/c943cc4740bffb
#### ref: https://sqripts.com/2022/06/16/20408/


ScopedSession = scoped_session(
    sessionmaker(bind=DbBase.engine, future=True),
)


def entrypoint(func: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(func)
    def _entry_point(*args: Any, **keywords: Any) -> Any:
        session: Session = ScopedSession()
        try:
            result = func(*args, **keywords)
        except Exception:
            session.rollback()
            raise
        else:
            session.commit()
        finally:
            ScopedSession.remove()
        return result

    return _entry_point
