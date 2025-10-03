from fastapi import FastAPI,Request

app = FastAPI()

l = []


@app.post("/post")
async def addcontact(request:Request):
    data = await request.json()
#dict.get(key)
    phone = data.get('phone')
    email = data.get('email')
    d = {"phone":phone,"email":email}
    l.append(d)
    return {"message":f"{d} added successful."}

@app.get("/result")
def display():
    return {"contact": l}




