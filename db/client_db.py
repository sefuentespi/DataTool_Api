from typing import Dict
from pydantic import BaseModel

class Client(BaseModel):
    id: int
    name: str
    client_isActive: bool

database_client = Dict[int, Client]

database_client = {1:Client(**{"id":1,
                               "name": "Alpina",
                               "client_isActive": True }),
                   2:Client(**{"id":2,
                               "name": "Postobon",
                               "client_isActive": False }),                      
                  }    

def get_client(id: int):
    if id in database_client.keys():
        return database_client[id]
    else:
        return None

def update_client(client: Client):
    database_client[client.id] = client
    return client

def create_client(client: Client):
    if client.id in database_client.keys():
        return "User already exists"
    else:
        new = {client.id: client}
        database_client.update(new)
        return new
