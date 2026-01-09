from fastapi import FastAPI

app = FastAPI(title="Autonomous Flight Booking Agent")

@app.get("/")
def root():
    return {"status": "Flight Agent running"}
