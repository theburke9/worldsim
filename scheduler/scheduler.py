from world.world import World

class Scheduler:
    ticks: int = 0
    
    def __init__(self, world: World):
        self.world = world
        self.current_tick = 0

    def run(self, n_ticks: int = 500) -> None:
        for _ in range(n_ticks):
            self.world.update(self.current_tick)

        self.current_tick += 1