from fastapi import Depends, FastAPI, Request, Body, Path, Query, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.encoders import jsonable_encoder
from middlewares.error_handler import ErrorHandler
from pydantic import BaseModel, Field 
from typing import Optional, List
from jwt_manager import create_token, validate_token
from fastapi.security import HTTPBearer
from config.database import Session, engine, Base
from models.user import User as UserModel

# Instacia de mi aplicacion
app =  FastAPI()
app.title = 'MovieApi'
app.version = '0.0.1'

app.add_middleware(ErrorHandler)

#motor
Base.metadata.create_all(bind= engine)

####### Models ###
class User(BaseModel):
    id: Optional[int] = None
    name:str
    laste_name: str
    mail : str
    direcction : str
    number : str
    is_actie : bool


############################### Querys #############################333
@app.get('/home', tags=['Home'])
def getMessage():
    return 'Hello People'
      
########## USERS ##########
@app.post('/User', tags=['User'] )
def createUser(user : User) -> dict :
    db = Session()
    new_user = UserModel(**user.model_dump())
    db.add(new_user)
    db.commit()
    return JSONResponse(status_code=201, content={ 'sms' : 'success'})

@app.get('/User', tags=['User'], response_model=list[User], status_code=200)
def getUsers()->List[User]:
    db = Session()
    result = db.query(UserModel).all()  
    return JSONResponse(status_code= 200, content=jsonable_encoder(result))

@app.get('/User/{id}', tags=['User'], response_model= User )
def getUserById(id: int = Path(ge =1 , le=200))-> User:
    db = Session()
    result  = db.query(UserModel).filter(UserModel.id == id).first()
    if not result:
        return JSONResponse(status_code=404, content= {'sms': 'not found'})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@app.get('/User/', tags=['User'], response_model=List[User])
def isActiveUser(is_active: bool = Query())-> List[User]:
    db =Session()
    result = db.query(UserModel).filter(UserModel.is_actie == is_active).all()
    if not result:
        return JSONResponse(status_code= 404, content={'sms': 'not found'})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@app.put('/UpdateUser/{id}', tags=['User'], response_model=dict, status_code=200 )
def updateuser(id:int, user: User)-> dict:
    db = Session()
    result = db.query(UserModel).filter(UserModel.id == id).first()
    
    if not result:
        return JSONResponse(status_code= 404, content='user notFound')
    result.name = user.name
    result.laste_name = user.laste_name
    result.mail = user.mail
    result.direcction = user.direcction
    result.number = user.number
    result.is_actie = user.is_actie
    db.commit()
    return JSONResponse(status_code=200, content={'sms': 'edit user susscess'})
        
# delete
@app.delete('/UserDelete/{id}', tags=['User'] )
def deleteUserById(id: int):
    db = Session()
    result = db.query(UserModel).filter(UserModel.id == id).first()
    
    if result:
        db.delete(result)
        db.commit()
        return JSONResponse(status_code= 201, content={'sms': 'delete success'})
    
    return JSONResponse(status_code=404, content={'sms': 'user not found'})
    