from fastapi import FastAPI
from routes.user import user

app = FastAPI() #Crear el módulo principal de la aplicación

app.include_router(user) #Incluir la ruta externa en el proyecto principal

