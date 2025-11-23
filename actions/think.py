from action import Action
from utils.time import tick_to_time
from llm.api import BaseApi

class ThinkAction(Action):
    def __init__(self, remaining: str):
        super().__init__("THINK", remaining)

    def start(self, agent_name: str, startup_tick: int) -> None:
        super().__init__(startup_tick)
        print(f"[{tick_to_time(startup_tick)}] 💭 {agent_name} starts to think")

    def update(self, current_tick: int):
        if not self.isRunning():
            return
        
        if self.hasRemainingTicks():
            self.remaining_ticks -= 1
            return
        
        brain_response = self.agent.think("")

        if brain_response is None:
            pass
