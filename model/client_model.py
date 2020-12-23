from pydantic import BaseModel

class ClientIn(BaseModel):
    id: int
    name: str

class ClientOut(BaseModel):
    id: int
    name: str
    client_isActive: bool

class ClientInCreate(BaseModel):
    id: int
    name: str
    client_isActive: bool