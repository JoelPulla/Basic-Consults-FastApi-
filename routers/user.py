from fastapi import APIRouter
from fastapi import  Path, Query
from fastapi.responses import  JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import Optional, List
from config.database import Session
from models.user import User as UserModel
from services.user_service import UserService 
from schemas.user_schema import User 


user_router =APIRouter()



########## USERS ##########
@user_router.get('/User/{id}', tags=['User'], response_model= User )
def getUser(id: int = Path(ge =1 , le=200))-> User:
    db = Session()
    result  = UserService(db).get_user(id)
    if not result:
        return JSONResponse(status_code=404, content= {'sms': 'not found'})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@user_router.get('/User', tags=['User'], response_model=list[User], status_code=200)
def getAllUsers()->List[User]:
    db = Session()
    result = UserService(db).get_users()     
    return JSONResponse(status_code= 200, content=jsonable_encoder(result))


@user_router.get('/User/', tags=['User'], response_model=List[User])
def isActiveUser(is_active: bool = Query())-> List[User]:
    db =Session()
    result = UserService(db).get_users_by_status(is_active)
    if not result:
        return JSONResponse(status_code= 404, content={'sms': 'not found'})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@user_router.post('/User', tags=['User'] )
def createUser(user : User) -> dict :
    db = Session()
    UserService(db).create_user(user)
    return JSONResponse(status_code=201, content={ 'sms' : 'success'})

@user_router.put('/UpdateUser/{id}', tags=['User'], response_model=dict, status_code=200 )
def updateuser(id:int, user: User)-> dict:
    db = Session()
    result = UserService(db).update_User(id) 
    if not result:
        return JSONResponse(status_code= 404, content='user notFound')
    UserService(db).update_User(id, user)
    return JSONResponse(status_code=200, content={'sms': 'edit user susscess'})
        
# delete
@user_router.delete('/UserDelete/{id}', tags=['User'] )
def deleteUserById(id: int):
    db = Session()
    result = UserModel = db.query(UserModel).filter(UserModel.id == id).first()
    
    if not result:
        return JSONResponse(status_code=404, content={'sms': 'user not found'})
    
    UserService(db).delete_user(id)    
    return JSONResponse(status_code= 201, content={'sms': 'delete success'})
    
    
    