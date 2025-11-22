from action_state import ActionState

class Action:
    name: str
    state: ActionState

    def __init__(self, name, initial_state: ActionState = ActionState.IDLE):
        self.name = name
        self.state = initial_state

    def start(self) -> None:
        pass

    def update(self) -> None:
        pass

    def isDone(self) -> bool:
        return self.state == ActionState.DONE
    