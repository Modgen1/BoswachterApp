from fastapi import HTTPException, Query, APIRouter
from app.models.observation import *
from sqlmodel import select, Session
from app.dependencies.database import engine
from typing import Annotated

router = APIRouter(
    prefix="/observations",
    tags=["observations"],
)

@router.get("/")
def get_observations(
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100,
) -> list[Observation]:
    with Session(engine) as session:
        observations = session.exec(select(Observation).offset(offset).limit(limit)).all()
        return observations

@router.get("/{id}")
async def get_observation(id: int) -> Observation:
    with Session(engine) as session:
        observation = session.get(Observation, id)
        if not observation:
            raise HTTPException(status_code=404, detail="Observation not found")
        return observation

@router.delete("/{id}", status_code=204)
def delete_observation(id: int):
    with Session(engine) as session:
        observation = session.get(Observation, id)
        if not observation:
            raise HTTPException(status_code=404, detail="Observation not found")
        session.delete(observation)
        session.commit()

@router.patch("/{id}")
def patch_observation(id: int, observation: ObservationUpdate):
    with Session(engine) as session:
        db_observation = session.get(Observation, id)
        if not db_observation:
            raise HTTPException(status_code=404, detail="Observation not found")
        db_observation.sqlmodel_update(observation.model_dump(exclude_unset=True))
        session.add(db_observation)
        session.commit()
        session.refresh(db_observation)
        return db_observation
    
@router.put("/{id}")
def put_observation(id: int, observation: Observation:
    with Session(engine) as session:
        db_observation = session.get(Observation, id)
        if not db_observation:
            raise HTTPException(status_code=404, detail="Observation not found")
        db_observation.sqlmodel_update(observation.model_dump())
        session.add(db_observation)
        session.commit()
        session.refresh(db_observation)
        return db_observation

@router.post("/", status_code=201)
def post_observation(observation: ObservationCreate) -> Observation:
    with Session(engine) as session:
        db_observation = Observation.model_validate(observation)
        session.add(db_observation)
        session.commit()
        session.refresh(db_observation)
        return db_observation