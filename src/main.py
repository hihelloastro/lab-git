# 교재용 코드
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union

app = FastAPI(
    title="FastAPI — Hello World code",
    description="This is the Hello World of FastAPI.",
    version="1.0.0",
)

class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None

@app.get("/hello")
def hello_world():
    return "Hello World!"

@app.get("/get_test/{input_val}")
def get_test1(input_val):
    return {"valeus": input_val}

# http://127.0.0.1:8000/get_test2/100?q=안녕
@app.get ("/get_test2/{input_val}")
def get_test2(input_val: int, q: str):
    return {"item_id": input_val, "q": q}

'''
{
    "name": "Item1",
    "description": "This is an item.",
    "price": 10.5,
    "tax": 0.5
}
'''
@app.post('/post_test')
def post_test(item: Item):
    return item

# 실행
# Talend API Tester 확인
# uvicorn main:app --reload
