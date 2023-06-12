from ninja import NinjaAPI
from login.urls import router as login_router
from ninja_jwt.controller import NinjaJWTDefaultController

api = NinjaAPI()

api.register_controllers(NinjaJWTDefaultController)

api.add_router("/",login_router,tags=["Login"] )