import os
from dotenv import load_dotenv
from world.world import World
from world.zone import Zone
from agent.agent import Agent
from llm.deepseek import DeepSeekAPI

def main(API_KEY: str) -> None:
    generator = DeepSeekAPI("https://api.deepseek.com", "deepseek-reasoner", "You are an agent living in a nice little village.", API_KEY)
    homeZone = Zone("Park", (0, 0), (2, 2))
    john = Agent("john", 20, generator, (0,0))
    myWorld = World(10, 10, [homeZone], [john])
    print(myWorld.is_tile_walkable(1, 1))
    print(myWorld.get_zone_name_at(3, 2))

if __name__ == "__main__":
    load_dotenv()
    api_key = os.getenv("SECRET_API_KEY")

    if api_key is None:
        print("You have to provide an API KEY")
        print("Read README.md")
        exit(1)

    main(api_key)