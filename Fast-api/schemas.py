from pydantic import BaseModel

class ElectronicsCreate(BaseModel):
    name: str
    category: str
    brand: str
    price: str
    stock :int


class ElectronicsResponse(ElectronicsCreate):
    id : int

    model_config = {
        "from_attributes": True

    }