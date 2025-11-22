from enum import Enum

class ActionState(Enum):
    IDLE = 1
    RUNNING = 2
    PAUSE = 3
    DONE = 4