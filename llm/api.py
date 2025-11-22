from abc import ABC, abstractmethod

class BaseApi(ABC):
    base_url: str
    generation_route: str
    model: str
    system_initial_prompt: str
    api_key: str

    def __init__(self, base_url: str, generation_route: str, model: str, system_initial_prompt: str, api_key: str):
        assert(isinstance(base_url, str))
        assert(isinstance(generation_route, str))
        assert(isinstance(model, str))
        assert(isinstance(system_initial_prompt, str))
        assert(isinstance(api_key, str))
        self.base_url = base_url
        self.model = model
        self.system_initial_prompt = system_initial_prompt
        self.generation_route = generation_route
        self.api_key = api_key

    @abstractmethod
    def generate(self, prompt: str) -> str:
        pass