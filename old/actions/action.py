from enum import Enum

class ActionState(Enum):
    IDLE = 1
    RUNNING = 2
    PAUSE = 3
    DONE = 4

class Action:
    def __init__(self, name: str, interruptible=True):
        self.name = name
        self.state = ActionState.IDLE
        self.interruptible = interruptible

    def start(self, agent, world, tick):
        self.state = ActionState.RUNNING

    def update(self, agent, world, tick):
        pass

    def pause(self):
        if self.interruptible and self.state == ActionState.RUNNING:
            self.state = ActionState.PAUSE
            print(f"⏸️ {self.name} paused")

    def resume(self):
        if self.state == ActionState.PAUSE:
            self.state = ActionState.RUNNING
            print(f"▶️ {self.name} resumed")

    def is_done(self):
        return self.state == ActionState.DONE