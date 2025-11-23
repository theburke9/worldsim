from abc import ABC, abstractmethod
from actions.action_state import ActionState

class Action(ABC):
    name: str
    startup_tick: int
    state: ActionState
    remaining_ticks: int
    agent: object

    def __init__(self, agent: object, name, remaining_ticks: int, initial_state: ActionState = ActionState.IDLE):
        self.name = name
        self.agent = agent
        self.startup_tick = 0
        self.state = initial_state
        self.remaining_ticks = remaining_ticks

    def start(self, startup_tick: int) -> None:
        self.start = ActionState.RUNNING
        self.startup_tick = startup_tick

    def update(self, current_tick: int) -> None:
        pass

    def isDone(self) -> bool:
        return self.state == ActionState.DONE
    
    def isRunning(self) -> bool:
        return self.state == ActionState.RUNNING
    
    def hasRemainingTicks(self) -> bool:
        return self.remaining_ticks > 0
    