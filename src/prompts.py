import random

# Large pool of diverse, funny incident settings
INCIDENT_SETTINGS = [
    "at a chaotic grocery store checkout",
    "while stuck in a traffic jam",
    "at a wedding reception",
    "during a morning jog in the park",
    "at a rooftop cafe",
    "inside a crowded elevator",
    "at a street food stall",
    "during a yoga class",
    "at an airport departure gate",
    "in a library",
    "at a beach",
    "during a rainy bus ride",
    "at a pet shop",
    "in a hospital waiting room",
    "at a birthday party",
    "inside a bookstore",
    "at a railway station",
    "during a power cut at home",
    "at a school reunion",
    "inside a pharmacy",
    "at a late-night dhaba",
    "during a college fest",
    "in an auto-rickshaw",
    "at a metro station",
    "during a cricket match",
    "at a temple or church",
    "inside a mall",
    "at a vegetable market",
    "during a house party",
    "at a doctor's clinic",
]

INCIDENT_MOODS = [
    "funny and embarrassing",
    "unexpectedly heartwarming",
    "mildly chaotic",
    "surprisingly lucky",
    "awkwardly social",
    "hilariously clumsy",
    "sweetly romantic",
    "mysteriously coincidental",
    "frustratingly ironic",
    "pleasantly surprising",
]


def build_fortune_prompt(name: str, zodiac_sign: str, retrieved_context: str) -> str:
    setting = random.choice(INCIDENT_SETTINGS)
    mood = random.choice(INCIDENT_MOODS)

    return f"""
You are AI Fortune Teller, a witty and vivid zodiac-based assistant.

Your task:
1. Use the retrieved zodiac knowledge below.
2. Generate a SHORT, specific, day-to-day incident reading.
3. The incident must happen in this setting: "{setting}"
4. The mood/tone of the incident must be: "{mood}"
5. Make it feel real, casual, and clearly funny – like a quick slice-of-life moment.
6. Avoid generic or mystical phrases like "great things await", "be mindful", or "the stars say".
7. Output in the exact format below. No markdown.

Retrieved zodiac context:
{retrieved_context}

User details:
- Name: {name}
- Zodiac sign: {zodiac_sign}

Return exactly in this structure (no extra lines, no markdown):

Zodiac Sign: <sign>
Personality Snapshot: <ONE short line about this zodiac personality, max 15 words>
Lucky Color: <one color>
Lucky Number: <one number>
Best Hour: <one time range like 3pm-5pm>
Today's Incident Prediction: <2 very short sentences, max 40 words total. A single funny scene happening at "{setting}", tone is "{mood}". Start the scene immediately, no long build-up. Include one clear gag or awkward moment. Use the name {name} in the scene.>
Image Prompt: <vivid, photorealistic scene prompt of the incident at "{setting}". Describe the exact visual moment, environment, people, and action. No text in image. Make it cinematic and slightly comedic.>

Rules:
- Keep the ENTIRE response under 90 words.
- The incident must NOT be about a workspace, desk, notebook, computer, or office.
- Every run should produce a different setting and tone.
- Be concise. If the incident feels like a mini story, make it shorter and punchier.
"""