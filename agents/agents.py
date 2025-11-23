from llm.api import BaseApi
from actions.action import Action

class Agent:
    name: str
    age: int
    memories: list[str]
    plan: list[object]
    brain: BaseApi
    current_action: Action | None
    initial_position: tuple[int, int]

    # constructor
    def __init__(self, name: str, age: int, brain: BaseApi, initial_position: tuple[int, int], initial_memory: list[str] = [], initial_plan: list[Action] = []) -> None:
        assert(age > 0)
        assert(isinstance(initial_position, tuple))
        assert(isinstance(initial_memory, list))
        assert(isinstance(initial_plan, list))
        assert(isinstance(brain, BaseApi))
        self.name = name
        self.age = age
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

    def isBusy(self) -> bool:
        if self.current_action is None or self.current_action.isDone():
            return False
        return True