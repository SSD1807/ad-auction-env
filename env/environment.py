import random

class AdAuctionEnv:
    def __init__(self):
        self.reset()

    def reset(self):
        self.budget = 1000
        self.timestep = 0
        
        # simulate ad performance
        self.ctr = random.uniform(0.03, 0.07)          # click-through rate
        self.conv_rate = random.uniform(0.01, 0.03)    # conversion rate
        
        return self._get_obs()

    def _get_obs(self):
        return {
            "budget": round(self.budget, 2),
            "ctr": round(self.ctr, 4),
            "conv_rate": round(self.conv_rate, 4),
            "timestep": self.timestep
        }

    def step(self, action):
        bid = action.get("bid", 1.0)

        # simulate competitor (harder over time)
        competitor_bid = random.uniform(0.5, 3.0) * (1 + self.timestep * 0.05)

        win = bid > competitor_bid

        if win:
            price_paid = competitor_bid  # second-price auction
            
            impressions = 100
            clicks = int(self.ctr * impressions)
            conversions = int(clicks * self.conv_rate)

            revenue = conversions * 50
            cost = price_paid * clicks
        else:
            revenue = 0
            cost = 0

        # ===== IMPROVED REWARD =====
        roas = revenue / (cost + 1e-6)
        reward = roas

        # penalty if no win
        if not win:
            reward -= 0.1

        # penalty for overbidding
        if bid > competitor_bid + 1:
            reward -= 0.2

        # budget efficiency bonus
        if cost > 0 and self.budget > 0:
            reward += 0.05

        # penalty if budget exhausted early
        if self.budget < 100:
            reward -= 0.3

        # ===== UPDATE STATE =====
        self.budget -= cost
        self.timestep += 1

        done = self.budget <= 0 or self.timestep >= 20

        return self._get_obs(), reward, done, {
            "win": win,
            "competitor_bid": round(competitor_bid, 2)
        }