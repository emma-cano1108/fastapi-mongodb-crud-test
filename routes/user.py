from fastapi import APIRouter, Response, status #Módulo para crear rutas (URL's) por aparte (APIRouter)
from config.db import conn
from schemas.user import userEntity, usersEntity
from models.user import User #Importa el modelo de los datos de usuario que deben ser ingresados
from passlib.hash import sha256_crypt
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT

user = APIRouter()

@user.get('/users', response_model=list[User], tags=['Users']) #Al visitar la url /users, estará entrando al módulo user, Método get para consultar registros
def find_all_user():
    return usersEntity(conn.users.user.find())

@user.post('/users', response_model=User, tags=['Users']) #Método post para crear registros
def create_user(user: User):
    new_user = dict(user) #Convertir el usuario en un diccionario para poder procesarlo
    del new_user['id']
    new_user["password"] = sha256_crypt.encrypt(new_user["password"]) #Encriptar contraseña
    id = conn.users.user.insert_one(new_user).inserted_id #Crea el documento de usuario y almacena el id generado en una variable
    user = conn.users.user.find_one({'_id': id})
    return userEntity(user) #Retorna el usuario recién creado teniendo en cuenta el schema userEntity

@user.get('/users/{id}', response_model=User, tags=['Users'])
def find_user(id: str):
    return userEntity(conn.users.user.find_one({"_id": ObjectId(id)}))


@user.put('/users/{id}', response_model=User, tags=['Users']) #Método put para actualizar registros
def update_user(id: str, user: User):
    conn.users.user.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(user)})
    return userEntity(conn.users.user.find_one({"_id": ObjectId(id)}))

@user.delete('/users/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=['Users']) #Método delete para eliminar registros
def delete_user(id: str):
    userEntity(conn.users.user.find_one_and_delete({"_id": ObjectId(id)}))
    return Response(status_code=HTTP_204_NO_CONTENT) #Retornar una respuesta de FastAPI con el código de estado 204 proveído por Starlette
#Estado 204: Se llevó a cabo correctamente la instrucción pero no es necesario / no hay información para mostrar o usar
