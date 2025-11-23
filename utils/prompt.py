import re

def load_prompt(path: str, *inputs) -> str:
    with open(path, "r", encoding="utf-8") as f:
        template = f.read()

    for i, val in enumerate(inputs):
        template = re.sub(fr"!<INPUT {i}>!", str(val), template)

    return template.strip()