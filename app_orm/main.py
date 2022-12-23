from fastapi import FastAPI
from . import models
from .database_pg_local import engine
from .routers import post, user, auth, vote
from .config import settings



#crea in automatico tabella da modello Base
#a seguito dell'utilizzo di alembic questa parte non mi serve
# piu perche ho l'elenco delle revision già pronte
#models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)







