def userEntity(item) -> dict: #Establecer que se retornará un diccionario (un solo usuario)
    return {
        "id": str(item['_id']),
        "name": item['name'],
        "email": item['email'],
        "password": item['password']
    }


def usersEntity(entity) -> list:
    return [userEntity(item) for item in entity] #Se ingresa una lista, y por cada elemento que contenga esa lista, se le pasará a userEntity