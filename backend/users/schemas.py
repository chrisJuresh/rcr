from ninja import Schema

class UserRegisterSchema(Schema):
    username: str
    password: str