from ninja_extra import NinjaExtraAPI
from login.urls import router as login_router

api = NinjaExtraAPI(csrf=True)

api.add_router("/",login_router,tags=["Login"])