from ninja_extra import NinjaExtraAPI
from login.urls import router as login_router
from ninja_jwt.controller import NinjaJWTDefaultController

api = NinjaExtraAPI()

api.register_controllers(NinjaJWTDefaultController)

api.add_router("/",login_router,tags=["Login"])