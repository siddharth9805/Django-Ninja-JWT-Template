from ninja import Router
from ninja_jwt.authentication import AsyncJWTAuth
from .schemas import UserSchema, TokenSchema, UserProfileSchema,UserLoginSchema
from .models import User,UserProfile
from django.http import HttpResponse
from ninja_jwt.tokens import RefreshToken,AccessToken

router = Router()

@router.post('/login',response=TokenSchema)
def login(request,payload:UserLoginSchema):
    user = User.objects.filter(username=payload.username).first()
    
    if not user:
        return HttpResponse("No such user", 404)
    if not user.check_password(payload.password):
        return HttpResponse("check password", 401)
    
    refresh_token = RefreshToken.for_user(user)
    access_token = refresh_token.access_token

    return HttpResponse(access_token,200)

@router.post('/userView', auth=AsyncJWTAuth)
def userView(request,payload:TokenSchema):
    token=payload.token
    token_data=AccessToken(token)
    user_id=token_data["username"]

    if not token_data:
        return HttpResponse("No Token", 404)
    
    user=User.objects.filter(username=user_id).first()
    userdetail= UserProfile.objects.filter(username=user.username).first()

    if userdetail is None:
        data={"username":user.username, "role_name":user.get_role_name()}
        seralized = UserProfileSchema(**data)
        userdetail=UserProfile.objects.create(**seralized.dict())
        userdetail.save()
    else:
        userdetail.role_name=user.get_role_name()
        userdetail.save()
    
    return HttpResponse(userdetail.username,200)