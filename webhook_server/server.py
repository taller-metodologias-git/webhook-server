from fastapi import Body, FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/payload/")
def print_payload(event=Body()):
    print("data received", event)
