from __future__ import annotations
from enviroment import Enviroment
from agent import Agent

def main():
    env = Enviroment()
    agent = Agent()

    while not env.is_done():
        agent.step(env)

    print(f"total reward achieved after 10 iterations: {agent.total_reward}")

if __name__ == "__main__":
    main()
