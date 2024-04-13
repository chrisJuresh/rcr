from ninja_jwt.controller import NinjaJWTDefaultController
from ninja_extra import NinjaExtraAPI
from ninja import Swagger

swagger = Swagger(settings={"persistAuthorization": True})
api = NinjaExtraAPI(docs=swagger)
api.register_controllers(NinjaJWTDefaultController)