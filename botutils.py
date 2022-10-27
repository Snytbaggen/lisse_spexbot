import random

def get_quote():
    quotes = [
        "Jag har inget plan!",
        "Man kan ju göra så, men det är inte rätt",
        "Alperna är toppen, och flaggan är ett stort plus",
        "Om folket får välja, så kan de ju välja fel",
        "Jag tänker alltså är jag, hur kan du då existera?",
        "Det är ett löfte att det är en målsättning som vi lovar att ha som mål att arbeta för",
        "Ja! Maicar sense.",
        "Tjallare har inga tjommar",
        "Det är Zambia Gambia grej som i Bruneis tåg",
        "Holger, jag ser dig mer som en bekant.",
        "Inga män!",
        "…och Mockfjärdsrevolvern är inte en bok heller.",
        "Vänner *tar hand om* varann.",
        "En tumme är tre korn, tre tummar ryms i en handflata och tre handflator är en räckvidd lång. Tar du tjugotvå räckvidder så får du en stång. Sätter du ihop tre stänger med 25 länkar så får du en kedja. Delar du kedjan i tiondelar så ryms dom i en famn, och hundra famnar, det är en kabel. Häpp!",
        "Han är en oskyldig säl som inte förtjänar att bli klubbad.",
        "Bra tänkt! Jag tackor och bockar."
        "Spöken av järn? Hur läskigt är de? Menar du typ Fe?",
        "Mannen, myten, matberedaren – Mazarin maximerar!"
    ]
    return random.choice(quotes)
