from llm.api import BaseApi
from actions.action import Action
from utils.prompt import load_prompt

class Agent:
    name: str
    age: int
    energy: int
    health: int
    hunger_level: int
    memories: list[str]
    plan: list[object]
    brain: BaseApi
    current_action: Action | None
    initial_position: tuple[int, int]

    # constructor
    def __init__(self, name: str, age: int, energy: int, health: int, hunger_level: int, brain: BaseApi, initial_position: tuple[int, int], initial_memory: list[str] = [], initial_plan: list[Action] = []) -> None:
        self.name = name
        self.age = age
        self.energy = energy
        self.health = health
        self.hunger_level = hunger_level
        self.memories = initial_memory
        self.plan = initial_plan
        self.brain = brain
        self.current_action = None
        self.initial_position = initial_position

    # state
    def update(self, current_tick: int) -> None:
        pass

    def pickAction(self) -> None:
        """
        This is a real naive implementation.
        I think we can make a better function.
        """
        self.current_action = Action("TO DO: IMPLEMENT REAL ACTION")

    def think(self, prompt: str) -> str | None:
        return self.brain.generate(prompt)
    
    def getState(self, prompt_path: str, current_tick: int) -> str:
        from utils.time import tick_to_time
        return load_prompt(prompt_path, self.name, self.age, tick_to_time(current_tick), ";".join(self.memories))

    def isBusy(self) -> bool:
        if self.current_action is None or self.current_action.isDone():
            return False
        return True