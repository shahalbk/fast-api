from fastapi import FastAPI

app = FastAPI()

#define a root endpoint

@app.get("/")
def read_root():
    return {"message": "Hello, World"}

#define another endpoint with a parameter,querry parameter is name
@app.get("/hello/{name}") 
def say_hello(name: str):
    return {"message":f"hello, {name}"}#its for gettijng json  format.

#to run the server, use uvicorn main:app --reload