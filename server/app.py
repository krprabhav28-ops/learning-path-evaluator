from fastapi import FastAPI
from environment import LearningPathEvaluator

app = FastAPI()
env = LearningPathEvaluator()

@app.get("/")
def home():
    return {"message": "API running 🚀"}

@app.post("/reset")
def reset():
    env.current_task = "easy"   # IMPORTANT
    message = env.reset()
    return {"message": message}

@app.post("/step")
def step(action: dict):
    result = env.step(action)   # FIXED
    return result

@app.get("/state")
def state():
    return env.state()
