from google import genai
from src.config import GEMINI_API_KEY, GEMINI_MODEL

def get_client():
    return genai.Client(api_key=GEMINI_API_KEY)

def generate_fortune(prompt: str) -> str:
    client = get_client()
    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=prompt
    )
    return response.text.strip()

def parse_response_blocks(text: str):
    result = {
        "zodiac_sign": "",
        "personality_snapshot": "",
        "lucky_color": "",
        "lucky_number": "",
        "best_hour": "",
        "incident_prediction": "",
        "image_prompt": "",
        "raw_text": text,
    }

    current_key = None
    key_map = {
        "zodiac sign:": "zodiac_sign",
        "personality snapshot:": "personality_snapshot",
        "lucky color:": "lucky_color",
        "lucky number:": "lucky_number",
        "best hour:": "best_hour",
        "today's incident prediction:": "incident_prediction",
        "image prompt:": "image_prompt",
    }

    for line in text.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        lower = stripped.lower()
        matched = False
        for k, v in key_map.items():
            if lower.startswith(k):
                result[v] = stripped.split(":", 1)[1].strip() if ":" in stripped else ""
                current_key = v
                matched = True
                break
        if not matched and current_key:
            result[current_key] += (" " if result[current_key] else "") + stripped

    return result