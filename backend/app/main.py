from fastapi import FastAPI
from  app.routes import query,upload

app = FastAPI()

app.include_router(query.router)
app.include_router(upload.router)
