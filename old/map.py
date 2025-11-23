import numpy as np
from path_finder import astar

class Map:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.zones = []
        self.layers = {
            "collisions": np.zeros((height, width), dtype=np.uint8)
        }

    def is_walkable(self, x: int, y: int):
        return (
            0 <= x < self.width 
            and 0 <= y < self.height 
            and self.layers["collisions"][y][x] == 0
        )
    
    def add_zone(self, zone):
        self.zones.append(zone)

    def get_zone_at(self, x: int, y: int):
        for zone in self.zones:
            if zone.contains(x, y):
                return zone.label

        return "Unknown"
    
    def get_pos_at(self, zone_name: str):
        for zone in self.zones:
            if zone.label.lower() == zone_name.lower():
                return (zone.x1, zone.x2, zone.y1, zone.y2)
        return None

if __name__ == "__main__":
    m = Map(10, 10)
    print("map created\n", m.layers["collisions"])