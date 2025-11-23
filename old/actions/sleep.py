from actions.action import Action, ActionState
from utils import get_date_from_ticks

class ActionSleep(Action):
    def __init__(self, ticks):
        super().__init__("SLEEP")
        self.ticks = ticks
        self.actual_ticks = 0

    def start(self, agent, world, tick):
        super().start(agent, world, tick)
        print(f"[{get_date_from_ticks(tick)}] 💤 {agent.name} starts to sleep")

    def update(self, agent, world, tick):
        if (self.state != ActionState.RUNNING):
            return
        
        if self.actual_ticks >= self.ticks:
            print(f"[{get_date_from_ticks(tick)}] 💤 {agent.name} wakes up")
            self.state = ActionState.DONE
            return
        
        agent.energy += 5

        if agent.energy > 100:
            agent.energy = 100

        self.actual_ticks += 1