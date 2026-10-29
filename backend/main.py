from fastapi import FastAPI

app = FastAPI(title="AI Travel Planner")


@app.get("/")
def home():
    return {"message": "AI Travel Planner backend is running"}