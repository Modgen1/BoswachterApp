from fastapi import HTTPException, Query, APIRouter
from app.models.observation import Observation
from sqlmodel import select
from app.dependencies.database import SessionDep
from typing import Annotated

router = APIRouter(
    prefix="/observations",
    tags=["observations"],
)

@router.get("/")
def get_observations(
    session: SessionDep,
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100,
) -> list[Observation]:
    observations = session.exec(select(Observation).offset(offset).limit(limit)).all()
    return observations

@router.get("/{id}")
async def get_observation(id: int, session: SessionDep) -> Observation:
    observation = session.get(Observation, id)
    if not observation:
        raise HTTPException(status_code=404, detail="Observation not found")
    return observation

@router.delete("/{id}")
def delete_observation(id: int, session: SessionDep):
    observation = session.get(Observation, id)
    if not observation:
        raise HTTPException(status_code=404, detail="Observation not found")
    session.delete(observation)
    session.commit()
    return {"ok": True}

# @router.put("/{id}")
# def put_observation(id: int):
#     return {}

@router.post("/")
def post_observation(observation: Observation, session: SessionDep) -> Observation:
    session.add(observation)
    session.commit()
    session.refresh(observation)
    return observation