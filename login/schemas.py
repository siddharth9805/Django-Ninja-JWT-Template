from ninja import ModelSchema
from login.models import User, UserProfile
from ninja import Schema

class UserSchema(ModelSchema):
    class Config:
        model=User
        model_fields = ['password','username','role','last_login']

class UserProfileSchema(ModelSchema):
    class Config:
        model=UserProfile
        model_fields = ['role_name','username']

class TokenSchema(Schema):
    token:str

class UserLoginSchema(Schema):
    username:str
    password:str