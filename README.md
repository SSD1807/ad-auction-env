# Ad Auction OpenEnv

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