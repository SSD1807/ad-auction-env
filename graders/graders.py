def grade_roas(total_reward):
    """
    Converts total reward (ROAS) into a normalized score (0 to 1)
    """

    if total_reward >= 2.5:
        return 1.0
    elif total_reward >= 1.5:
        return 0.8
    elif total_reward >= 1.0:
        return 0.6
    elif total_reward >= 0.5:
        return 0.4
    else:
        return 0.2