from llm.api import BaseApi
import requests

class DeepSeekAPI(BaseApi):
    def __init__(self, base_url: str, model: str, system_initial_prompt: str, api_key: str):
        super().__init__(base_url, "chat/completions", model, system_initial_prompt, api_key)

    def generate(self, prompt: str, timeout: int = 120, stream: bool = False) -> str | None:
        url = f"{self.base_url}/{self.generation_route}"

        header = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }

        payload = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": self.system_initial_prompt},
                {"role": "user", "content": prompt}
            ],
            "stream": stream
        }

        try:
            response = requests.post(url, headers=header, json=payload, stream=stream, timeout=timeout)
            response.raise_for_status()
            data = response.json()
            return data["choices"][0]["message"]["content"].strip()
        except Exception as e:
            print(f"⚠️ DeepSeek API error: {e}")
            return None