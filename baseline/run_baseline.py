from env.environment import AdAuctionEnv
from graders.graders import grade_roas

def run_baseline():
    env = AdAuctionEnv()
    obs = env.reset()

    total_reward = 0
    done = False

    while not done:
        # smarter strategy
        if obs["ctr"] > 0.06:
            bid = 2.5
        elif obs["ctr"] > 0.045:
            bid = 1.8
        else:
            bid = 1.0

        action = {"bid": bid}

        obs, reward, done, info = env.step(action)
        total_reward += reward

    score = grade_roas(total_reward)

    print("Total Reward:", round(total_reward, 3))
    print("Final Score (0-1):", score)


if __name__ == "__main__":
    run_baseline()