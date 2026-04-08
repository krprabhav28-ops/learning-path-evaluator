from fastapi import FastAPI
from environment import LearningPathEvaluator

app = FastAPI()
env = LearningPathEvaluator()

@app.post("/reset")
def reset():
    message = env.reset()
    return{"message": message}

@app.post("/step")
def step(action: dict):
    result = env.step(action)
    return result

@app.get("/state")
def state():
    return env.state()
