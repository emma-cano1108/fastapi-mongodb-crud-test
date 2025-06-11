from typing import Union
from pydantic import BaseModel


class User(BaseModel): #Establece el modelo o formato en que se debe pasar un usuario
    id: Union[str, None] = None #Establece que no es necesario pasar el id, pero los demás si
    name: str
    email: str
    password: str