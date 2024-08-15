from fastapi import APIRouter


home_router = APIRouter()

##### MESSAGE DEFAULT HOME #####
@home_router.get('/home', tags=['Home'])
def getMessage():
    return 'Hello People'

