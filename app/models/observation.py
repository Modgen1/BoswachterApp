from sqlmodel import Field, SQLModel

class ObservationBase(SQLModel):
    name: str = Field()

class Observation(ObservationBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

class ObservationCreate(ObservationBase):
    pass

class ObservationUpdate(SQLModel):
    name: str | None = None