import os
import json
import requests
from utils import strip_think_blocks, strip_markdown_blocks

API_KEY="YOUR API KEY"

class DeepSeekClient:
    def __init__(self, host="http://localhost:11434", model="deepseek-r1"):
        self.url = f"{host}/chat/completions"
        self.model = model

    def generate(self, prompt: str, timeout: int = 120, stream: bool = False):
        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": stream
        }

        try:
            resp = requests.post(self.url, json=payload, stream=stream, timeout=timeout)
            resp.raise_for_status()

            if stream:
                output = ""
                for line in resp.iter_lines():
                    if not line:
                        continue
                    data = json.loads(line)
                    chunk = data.get("response", "")
                    #os.system('clear')
                    output += chunk
                    #print(output)
                return output.strip()
            else:
                data = resp.json()
                return data.get("response", "")

        except Exception as e:
            print(f"⚠️ DeepSeek error: {e}")
            return ""

    def generate_online(self, prompt: str, timeout: int = 120, stream: bool = False):
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {API_KEY}"
        }

        payload = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            "stream": stream
        }

        try:
            resp = requests.post(self.url, headers=headers, json=payload, stream=stream, timeout=timeout)
            resp.raise_for_status()

            if stream:
                output = ""
                for line in resp.iter_lines():
                    if not line or not line.startswith(b"data: "):
                        continue
                    data = line.decode("utf-8")[6:]  # retire "data: "
                    if data.strip() == "[DONE]":
                        break
                    try:
                        chunk = json.loads(data)
                        delta = chunk["choices"][0]["delta"].get("content", "")
                        output += delta
                        #print(delta, end="", flush=True)  # si vous voulez un rendu en live
                    except Exception:
                        continue
                return output.strip()

            else:
                data = resp.json()
                return data["choices"][0]["message"]["content"].strip()

        except Exception as e:
            print(f"⚠️ DeepSeek error: {e}")
            return ""
        
deepseek = DeepSeekClient("https://api.deepseek.com", "deepseek-reasoner")
        
if __name__ == "__main__":
    raw = deepseek.generate("" \
    "you are a test agent. " \
    "Introduce yourself in JSON only. " \
    "Exemple: { 'message': 'hello' }. " \
    "Do not include ANY markdown." \
    "Just raw JSON."
    )
    clean = strip_think_blocks(raw)
    clean = strip_markdown_blocks(clean)
    clean = clean.replace("\n", "")
    print(clean)
        