from typing import Dict
from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    price: int
    stock: int

database_product = Dict[int, Product]

database_product = {1:Product(**{"id":1,
                                 "name": "gaseosa",
                                 "price": 2000,
                                 "stock": 2}),
                    2:Product(**{"id":2,
                                 "name": "quesillo",
                                 "price": 4000,
                                 "stock":  4}),                      
                  }    

def get_product(id: int):
    if id in database_product.keys():
        return database_product[id]
    else:
        return None

def update_product(product: Product):
    database_product[product.id] = product
    return product