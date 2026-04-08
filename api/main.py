from fastapi import FastAPI
from env.environment import AdAuctionEnv
from tasks.tasks import get_tasks
from graders.graders import grade_roas

app = FastAPI()

env = AdAuctionEnv()

@app.get("/")
def home():
    return {"message": "Ad Auction OpenEnv Running"}

@app.get("/reset")
def reset():
    return env.reset()

@app.post("/step")
def step(action: dict):
    obs, reward, done, info = env.step(action)
    return {
        "observation": obs,
        "reward": reward,
        "done": done,
        "info": info
    }

@app.get("/state")
def state():
    return env._get_obs()

@app.get("/tasks")
def tasks():
    return get_tasks()

@app.get("/grader")
def grader(score: float):
    return {"graded_score": grade_roas(score)}