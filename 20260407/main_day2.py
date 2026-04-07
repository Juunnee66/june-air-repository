from fastapi import FastAPI, Path, Query
from request import UserCreateRequest
from response import UserResponse


app = FastAPI()

# python decorator : 함수를 꾸며주는, 함수에 추가기능을 부여하는 문법

# get 요청이 들어오면 root handler 함수 실행
@app.get("/")
def root_handler():
    return {"ping": "pong"}

# GET /hello : hello 경로에서 get 요청을 보내면 함수가 실행됨
@app.get("/hello") 
def hello_handler():
    return {"msg" : "Hello from FastAPI!"}

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


# 사용자 정보검색 API
# GET /users/search?name=alex
# GET /users/search?job=student
@app.get("/users/search?name=alex")
def search_user_handler(
    name: str | None = Query(None),
    job: str | None = Query(None),
):
    if name is None and job is None:
        return {"msg":"조회에 사용할 QueryParam이 필요합니다."}
    
    for user in users:
        if name and job:
            if user["name"] == name and user["job"] == job:
                return user
            else:
                return None
        else:
            if user["name"] == name:
                return user
            if user["job"] == job:
                return user


# 단일 사용자 데이터 조회 API
# GET /users/{user_id}
@app.get("/users/{user_id}")
def get_user_handler(

    user_id: int = Path(..., ge=1), # ge = greater than or equal to 
):
    for user in users:
        if user["id"] == user_id:
            return user
        

# 회원 추가 API
# POST /users
@app.post("/users", response_model=UserResponse)
def create_user_handler(
    #1) 사용자 데이터를 넘겨 받는다 + 데이터 유효성 검사(형식)
    body: UserCreateRequest # 클래스를 만나면 requestbody 라고 생각함
):

    #2) 사용자 데이터를 저장한다
    new_user = {
        "id": len(users) +1,
        "name": body.name,
        "job": body.job,
        "password": "password"
    }
    users.append(new_user)

    #3) 응답을 반환한다
    return new_user

