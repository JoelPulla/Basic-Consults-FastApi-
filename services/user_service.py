from models.user import User as UserModel
from schemas.user_schema  import User


class UserService():
    
    def __init__(self, db) -> None:
        self.db = db
        
    def get_users(self):
        result = self.db.query(UserModel).all()
        return result
    
    def get_user(self, id):
        result  = self.db.query(UserModel).filter(UserModel.id == id).first()
        return result
    
    def get_users_by_status(self, is_active):
        result = self.db.query(UserModel).filter(UserModel.is_actie == is_active).all()
        return result
    
    def create_user(self, user: User):
        new_user = UserModel( **user.model_dump())
        self.db.add(new_user)
        self.db.commit()
        return
    
    def update_User(self, id, data: User):
        result = self.db.query(UserModel).filter(UserModel.id == id).first()
        result.name = data.name
        result.laste_name = data.laste_name
        result.mail = data.mail
        result.direcction = data.direcction
        result.number = data.number
        result.is_actie = data.is_actie
        self.db.commit()
        return
    
    def delete_user(self, id):
        self.db.query(UserModel).filter(UserModel.is_actie == id).delete()
        self .db.commit()
        return