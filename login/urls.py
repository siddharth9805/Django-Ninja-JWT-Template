from ninja import Router
from .schemas import TokenSchema, UserProfileSchema,UserLoginSchema
from .models import User,UserProfile
from django.http import HttpResponse
from ninja_jwt.tokens import RefreshToken
from ninja_jwt.authentication import JWTAuth

router = Router()

@router.post('/login',response=TokenSchema)
def login(request,payload:UserLoginSchema):
    user = User.objects.filter(username=payload.username).first()
    
    if not user:
        return HttpResponse("No such user", 404)
    if user.password != payload.password:
        return HttpResponse("check password", 401)
    
    refresh_token = RefreshToken.for_user(user)
    access_token = refresh_token.access_token
    
    user.access_token=access_token.__str__()
    user.save()

    token={"token":access_token.__str__()}

    return token

@router.post('/userView',response=UserProfileSchema,auth=JWTAuth())
def userView(request,payload:TokenSchema):
    token=payload.token

    user = User.objects.filter(access_token=token).first()
    if not user:
        return HttpResponse("No such user", 404)
    
    userdetail= UserProfile.objects.filter(username=user.username).first()

    if userdetail is None:
        data={"username":user.username, "role_name":user.get_role_name()}
        seralized = UserProfileSchema(**data)
        userdetail=UserProfile.objects.create(**seralized.dict())
        userdetail.save()
    else:
        userdetail.role_name=user.get_role_name()
        userdetail.save()
    
    return userdetail