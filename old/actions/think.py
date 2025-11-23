from llm import deepseek
from prompt_loader import load_prompt
from actions.action import Action, ActionState
from utils import get_date_from_ticks, get_memory, get_thought, strip_markdown_blocks, strip_think_blocks, get_plan

class ActionThink(Action):
    def __init__(self, duration: int):
        super().__init__("THINK")
        self.remaining = duration

    def start(self, agent, world, tick):
        super().start(agent, world, tick)
        print(f"[{get_date_from_ticks(tick)}] 💭 {agent.name} starts to think...")

    def update(self, agent, world, tick):
        if self.state != ActionState.RUNNING:
            return
        
        if self.remaining > 0:
            self.remaining -= 1
        else:
            print(f"{agent.name}, {world.get_zone_at(*agent.position)}, {agent.position}, {agent.age}, {get_date_from_ticks(tick)}, {";".join(agent.memories)}, {agent.energy}")

            prompt = load_prompt(
                "prompts/think_v1.txt",
                agent.name,
                world.get_zone_at(*agent.position),
                agent.age,
                get_date_from_ticks(tick),
                ";".join(agent.memories),
                agent.energy
            )

            raw = deepseek.generate_online(prompt, 120, True)
            clean = strip_think_blocks(raw)
            clean = strip_markdown_blocks(clean)
            clean = clean.replace("\n", "")
            
            # update agent's plan and memory
            thought = get_thought(clean)
            plan = get_plan(clean)
            memory = get_memory(clean)

            agent.add_actions(plan)
            agent.add_memories(memory)

            print(f"[{get_date_from_ticks(tick)}] 💭 {agent.name} thinks: {thought}")
            self.state = ActionState.DONE
