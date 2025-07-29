from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.user import user

app = FastAPI() #Crear el módulo principal de la aplicación

# Permitir CORS para localhost:5173
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user) #Incluir la ruta externa en el proyecto principal

