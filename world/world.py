import numpy as np
from world.zone import Zone
from llm.api import BaseApi
from agents.agents import Agent

class World:
    """
    # World class
    This class represents the whole map.
    It contains **agents**, **zones** and **rules**.
    """
    width: int
    height: int
    zones: list[Zone]
    agents: list[Agent]
    rules: list[object]
    layers: dict[str, np.ndarray[tuple[np.uint8, np.uint8]]]
    generator: BaseApi

    MIN_WIDTH: int = 10
    MIN_HEIGHT: int = 10
    DEFAULT_ZONE: str = "outside"
        
    # constructor
    def __init__(self, width: int, height: int, zones: list[Zone] = [], agents: list[Agent] = [], rules: list[object] = []) -> None:
        assert(isinstance(width, int) and width >= self.MIN_WIDTH)
        assert(isinstance(height, int) and height >= self.MIN_HEIGHT)
        assert(isinstance(zones, list))
        assert(isinstance(agents, list))
        assert(isinstance(rules, list))
        self.width = width
        self.height = height
        self.zones = zones
        self.agents = agents
        self.rules = rules
        self.layers = { "collisions": np.zeros((height, width), dtype=np.uint8) }

    # state
    def update(self, current_tick: int) -> None:
        for agent in self.agents:
            if agent.isBusy():
                agent.update(current_tick)
            else:
                agent.pickAction()

    # map
    def is_tile_walkable(self, x: int, y: int) -> bool:
        assert("collisions" in self.layers.keys())
        assert(x >= 0 and x < self.width)
        assert(y >= 0 and y < self.height)
        return not self.layers["collisions"][y][x]

    # zones
    def get_zone_position_at(self, zone_name: str) -> tuple[int, int, int, int] | None:
        for zone in self.zones:
            if zone.name == zone_name.strip().lower():
                return (zone.start_zone, zone.end_zone)
        return None
    
    def get_zone_name_at(self, x: int, y: int) -> str:
        for zone in self.zones:
            if zone.has(x, y):
                return zone.name
        return self.DEFAULT_ZONE