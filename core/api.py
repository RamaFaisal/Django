from ninja import NinjaAPI, Router
from ninja.schema import Schema

api = NinjaAPI()
router = Router()

class HelloResponse(Schema):
    msg: str

@router.get("/hello", response=HelloResponse)
def hello(request):
    return {"msg": "Hello World"}

api.add_router("", router)
