from actions.action import Action, ActionState
from path_finder import astar
from utils import get_date_from_ticks

class ActionGoTo(Action):
    def __init__(self, target_location):
        super().__init__("GOTO")
        self.target_location = target_location
        self.target_position = None
        self.path = []

    def start(self, agent, world, tick):
        super().start(agent, world, tick)
        
        self.target_position = world.get_pos_at(self.target_location)
        
        print(f"[{get_date_from_ticks(tick)}] 🚶 {agent.name} goes to {self.target_location}")
        
        self.path = astar(world, agent.position, self.target_position)

    def update(self, agent, world, tick):
        if (self.state != ActionState.RUNNING):
            return
        
        if not self.path:
            print(f"[{get_date_from_ticks(tick)}] 📍 {agent.name} arrived at {world.get_zone_at(self.target_position[0], self.target_position[1])}")
            self.state = ActionState.DONE
            return

        next_pos = self.path.pop(0)
        agent.update_position(next_pos)