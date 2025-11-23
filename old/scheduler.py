from map import Map
from agent import Agent

class Scheduler:
    def __init__(self, map: Map, agents: list[Agent]):
        self.map = map
        self.agents = agents
        self.tick = 0

    def run(self, ticks: int):
        for _ in range(ticks):
            self.tick += 1

            for agent in self.agents:
                agent.update(self.map, self.tick)