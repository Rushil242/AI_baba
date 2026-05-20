from datetime import datetime

ZODIAC_RANGES = [
    ("Capricorn", (12, 22), (1, 19)),
    ("Aquarius", (1, 20), (2, 18)),
    ("Pisces", (2, 19), (3, 20)),
    ("Aries", (3, 21), (4, 19)),
    ("Taurus", (4, 20), (5, 20)),
    ("Gemini", (5, 21), (6, 20)),
    ("Cancer", (6, 21), (7, 22)),
    ("Leo", (7, 23), (8, 22)),
    ("Virgo", (8, 23), (9, 22)),
    ("Libra", (9, 23), (10, 22)),
    ("Scorpio", (10, 23), (11, 21)),
    ("Sagittarius", (11, 22), (12, 21)),
]

def get_zodiac_sign(day: int, month: int) -> str:
    for sign, start, end in ZODIAC_RANGES:
        sm, sd = start
        em, ed = end
        if sm == 12 and month == 1 and day <= ed:
            return sign
        if month == sm and day >= sd:
            return sign
        if month == em and day <= ed:
            return sign
    return "Capricorn"

def parse_dob(date_obj) -> tuple[int, int, int]:
    if isinstance(date_obj, datetime):
        return date_obj.day, date_obj.month, date_obj.year
    return date_obj.day, date_obj.month, date_obj.year