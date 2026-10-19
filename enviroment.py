from __future__ import annotations
import random

class Enviroment:
    def __init__(self):
        self.steps_left = 10

    def get_observation(self) -> list[float]:   # return the observations the enviroment "made"
        return [0.0, 0.0, 0.0]

    def get_actions(self) -> list[int]: # return the possible actions in this enviroment
        return [0, 1]

    def is_done(self) -> bool:  # check if the game is over
        return self.steps_left == 0

    def action(self, action: int) -> float: 
        if self.is_done():
            raise Exception("Game/Episode is over")

        self.steps_left -= 1        # handeling the action
        return random.random()      # returning the reward