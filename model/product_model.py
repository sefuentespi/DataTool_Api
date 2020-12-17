from pydantic import BaseModel

class ProductIn(BaseModel):
    id: int
    price: int

class ProductOut(BaseModel):
    id: int
    name: str
    price: int
    stock: int