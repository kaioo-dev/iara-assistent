from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes.user import router as user_router
from app.core.config import settings


app = FastAPI(title=settings.APP_TITLE, version=settings.APP_VERSION)

# Configurar CORS
origins = [
    "http://localhost:3000",  # URL do seu frontend
    "https://meusite.com",     # Outros sites permitidos
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Permitir apenas as URLs listadas
    allow_credentials=True,
    allow_methods=["*"],     # Permitir todos os métodos
    allow_headers=["*"],     # Permitir todos os cabeçalhos
)


# user router
app.include_router(user_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to my FastAPI app!"}
