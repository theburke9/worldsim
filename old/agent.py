from actions.action import Action
from actions.think import ActionThink

class Agent:
    def __init__(self, name: str, age: int, gender: str, position: tuple[int], energy = 100):
        self.name = name
        self.age = age
        self.gender = gender
        self.position = position
        self.current_action = None
        self.energy = energy
        self.memories = []
        self.plan = []

    def update(self, world, tick):
        if self.current_action is None or self.current_action.is_done():
            if not self.plan or len(self.plan) == 0:
                self.plan.append(ActionThink(1))
            self.current_action = self.plan.pop(0)
            self.current_action.start(self, world, tick)
        else:
            self.current_action.update(self, world, tick)

    def add_action(self, action: Action):
        self.plan.append(action)

    def add_actions(self, actions: list[Action]):
        self.plan.extend(actions)

    def add_memories(self, memories: list[str]):
        self.memories.extend(memories)  

    def update_position(self, newPosition: tuple[int]) -> None:
        self.position = newPosition          

    def __str__(self):
        return f"Agent({self.name}, {self.position})"
