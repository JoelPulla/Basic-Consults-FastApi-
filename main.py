from fastapi import FastAPI
from middlewares.error_handler import ErrorHandler
from config.database import engine, Base
from routers.user import user_router
from routers.home import home_router
from routers.movie import movie_router

##### INSTANCE MY APP #####
app =  FastAPI()
app.title = 'MovieApi'
app.version = '0.0.1'

app.add_middleware(ErrorHandler)

##### ROUTERS #####
app.include_router(home_router)
app.include_router(movie_router)
app.include_router(user_router)

### Motor ###
Base.metadata.create_all(bind= engine)

