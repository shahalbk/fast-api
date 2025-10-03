from fastapi import FastAPI,Request
app = FastAPI()

items = []


@app.post("/additems")
async def add_item(request:Request):
    data = await request.json()
    item = data.get("item")
    items.append(item)
    return {"message":f"successfully added {item}"}


@app.get("/getitems")
def get_items():
    return {"items":items}