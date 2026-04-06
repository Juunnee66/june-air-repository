from fastapi import FastAPI

app = FastAPI()

# python decorator : 함수를 꾸며주는, 함수에 추가기능을 부여하는 문법

# get 요청이 들어오면 root handler 함수 실행
@app.get("/")
def root_handler():
    return {"ping": "pong"}

# GET /hello : hello 경로에서 get 요청을 보내면 함수가 실행됨
@app.get("/hello") 
def hello_handler():
    return {"message" : "Hello from FastAPI!"}

users = [
    {"id":1, "name": "Alex", "job":"student"},
    {"id":2, "name": "Bob", "job":"sw engineer"},
    {"id":3, "name": "Chris", "job":"barista"}
]


# 전체 사용자 목록 조회 API : GET /users
@app.get("/users")
def get_users_handler():
    return users


# 이 코드는 user_id 보다 밑에두면 안됨 -> /users/부분이 같기 때문에!
@app.get("/users/search")
def search_user_handler():
    return {"msg":"searching..."}


# 단일 사용자 데이터 조회 API
# GET /users/{user_id}
@app.get("/users/{user_id}")
def get_user_handler(user_id: int): #타입힌트로 걸러주기
    for user in users:
        if user["id"] == user_id:
            return user


