from scheduler import Scheduler
from map import Map
from zone import Zone
from agent import Agent

if __name__ == "__main__":
    # map
    world_map = Map(20, 20)

    # zones
    home = Zone("home", 0, 0, 5, 5)
    park = Zone("park", 8, 8 , 9, 9)
    world_map.add_zone(home)
    world_map.add_zone(park)

    # agent
    agent = Agent("joe", 25, "male", (0, 0), 40)

    # scheduler
    scheduler = Scheduler(world_map, [agent])
    scheduler.run(500)