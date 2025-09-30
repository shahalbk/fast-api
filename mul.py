from fastapi import FastAPI

obj = FastAPI()

@obj.get("/")
def welcome():
    return {"message": "welcome to the math API"}

@obj.get("/multiply/{number}")
def multiply(number:int):
    return {"number":5*number}

@obj.get("/square/{number}")
def square(number:int):
    return {"square is ":number*number}

