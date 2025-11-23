import re
import json

from actions.action import Action

from datetime import datetime, timedelta

def strip_think_blocks(text: str) -> str:
    return re.sub(r"(?s)<think>.*?</think>", "", text).strip()

def strip_markdown_blocks(text: str) -> str:
    return re.sub(r"```(?:json)?|```", "", text).strip()

def hydrate_action(action: dict) -> Action|None:
    from actions.goto import ActionGoTo
    from actions.sleep import ActionSleep
    action_name: str = action.get('name', None)
    action_params: dict = action.get('params', None)

    if action_name is None:
        return None
    
    if action_name == "SLEEP":
        sleep_duration = action_params.get('duration', None)
        return ActionSleep(sleep_duration if sleep_duration is not None else 60)
    
    if action_name == "GOTO":
        target_location = action_params.get('target', None)

        if target_location is None:
            return None
        
        # Todo
        return ActionGoTo(target_location)

    return None

def get_plan(response: str) -> list[Action]:
    try:
        data: dict = json.loads(response)
        raw_actions: list = data.get('plan', [])
        actions: list[Action] = []

        for raw_action in raw_actions:
            action = hydrate_action(raw_action)
            actions.append(action)

        return actions
    except Exception as e:
        print("(get_plan) unable to parse JSON:", e)
        return []
    
def get_memory(response: str) -> list[Action]:
    try:
        data: dict = json.loads(response)
        memory: list[str] = data.get('memory_update', [])
        return memory
    except Exception as e:
        print("(get_memory) unable to parse JSON:", e)
        return []
    
def get_thought(response: str) -> list[Action]:
    try:
        data: dict = json.loads(response)
        thought: list[str] = data.get('thought', [])
        return thought
    except Exception as e:
        print("(get_thought) unable to parse JSON:", e)
        return []
    
def get_date_from_ticks(ticks: int) -> str:
    start_date = datetime(2025, 1, 1, 0, 0)
    minutes_per_tick = 10
    delta = timedelta(minutes=ticks * minutes_per_tick)
    new_date = start_date + delta
    return new_date.strftime("%Y-%m-%d %H:%M")