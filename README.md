# Ad Auction OpenEnv

## 🔗 Live Demo
👉 https://shreeyandas-ad-auction-env.hf.space

## Overview
This project simulates a real-world ad auction system similar to Meta Ads.

## Features
- Second-price auction mechanism
- Dynamic competitor bidding
- Budget constraints
- Reward based on ROAS
- Dynamic difficulty: competitor bids increase     over time

## Tasks
1. Easy: Basic bidding strategy
2. Medium: Budget optimization
3. Hard: Dynamic competition handling

## API Endpoints
- /reset
- /step
- /state
- /tasks
- /grader

## Run
pip install -r requirements.txt
uvicorn api.main:app --reload

## Docker
docker build -t ad-auction-env .
docker run -p 7860:7860 ad-auction-env

## 🧪 Example API Call

### POST /step

#### Request:
```json
{
  "bid": 2.5
}

{
  "reward": 1.23,
  "done": false,
  "info": {
    "win": true,
    "competitor_bid": 2.1
  }
}
---

### ⚠️ Important formatting tip
Make sure:
- triple backticks ``` are correct
- json block is properly closed

---

# ✅ STEP 5 — Push README update

```bash
git add README.md
git commit -m "Added API example"
git push