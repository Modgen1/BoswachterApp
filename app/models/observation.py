from sqlmodel import Field, SQLModel

# FIXME: update the models here to what is in the requirements

class ObservationBase(SQLModel):
    """
    This is the base class for Observation entities containing all fields the
    user can set.
    """
    name: str = Field()

class Observation(ObservationBase, table=True):
    """
    This is the table representation for the Observation entity, it includes
    all fields from the base class and our auto increment ID.
    """
    id: int | None = Field(default=None, primary_key=True)

class ObservationCreate(ObservationBase):
    """
    Model defining the data required to create an Observation. Currently this
    adds nothing to the base class.
    """
    pass

class ObservationUpdate(SQLModel):
    """
    Model defining data required for our PATCH endpoint. All fields are
    optional here since we only require to send in fields the user wants
    to change.
    """
    name: str | None = None