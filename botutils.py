import random

def get_quote():
    quotes = [
        "Jag har inget plan!",
        "Man kan ju göra så, men det är inte rätt",
        "Alperna är toppen, och flaggan är ett stort plus",
        "Om folket får välja, så kan de ju välja fel",
        "Jag tänker alltså är jag, hur kan du då existera?",
        "Det är ett löfte att det är en målsättning som vi lovar att ha som mål att arbeta för"
    ]
    return random.choice(quotes)
