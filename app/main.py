from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"msg": "root works"}

@app.get("/test")
def test():
    return {"msg": "test works"}
