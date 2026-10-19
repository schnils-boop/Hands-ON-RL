from __future__ import annotations
from enviroment import Enviroment
import random

class Agent: 
    def __init__(self):
        self.total_reward = 0.0

    def step(self, env: Enviroment):

        # get enviroment feedback
        current_obs = env.get_observation()
        actions = env.get_actions()

        # choose action at random (usually uses obs to choose action)
        action = random.choice(actions)

        # execute action and get reward
        reward = env.action(action)
        self.total_reward += reward

