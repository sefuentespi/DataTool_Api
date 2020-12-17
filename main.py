from fastapi import FastAPI
from pydantic import BaseModel
from model.client_model import ClientIn, ClientOut
from db.client_db import Client, get_client, update_client
from model.product_model import ProductIn, ProductOut
from db.product_db import Product, get_product, update_product
from fastapi.middleware.cors import CORSMiddleware

DataTool = FastAPI()

origins = [
    "http://localhost.tiangolo.com", "https://localhost.tiangolo.com",
    "http://localhost", "http://localhost:8080","https://datatool-front.herokuapp.com/"
]
DataTool.add_middleware(
    CORSMiddleware, allow_origins=origins,
    allow_credentials=True, allow_methods=["*"], allow_headers=["*"],
)

@DataTool.get("/clients/{client_id}")
async def client_get(client_id: int):
    client_in = get_client(client_id)
    if client_in == None:
        return None
    client_out = ClientOut(**client_in.dict())
    return client_out

@DataTool.put("/clients")
async def client_update(client: ClientIn):
    client_in = get_client(client.id)
    if client_in != None:
        client_in.name = client.name
        update_client(client_in)
        client_out = ClientOut(**client_in.dict())
        return client_out
    return None

@DataTool.get("/products/{product_id}")
async def product_get(product_id: int):
    product_in = get_product(product_id)
    if product_in == None:
        return None
    product_out = ProductOut(**product_in.dict())
    return product_out

@DataTool.put("/products")
async def product_update(product: ProductIn):
    product_in = get_product(product.id)
    if product_in == None:
        return None
    else:
        product_in.price = product.price
    update_product(product_in)
    product_out = ProductOut(**product_in.dict())
    return product_out