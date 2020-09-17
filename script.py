import random

LETTERS = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G"
]

ACCIDENTALS = [
    "sharp",
    "flat",
    "natural"
]

QUALITIES = [
    "Major",
    "Minor",
    "Augmented",
    "Diminished",
]

FIELDS = [
    LETTERS, ACCIDENTALS, QUALITIES
]

for field in FIELDS:
    random.shuffle(field)

print("OK - play {} {} {} ".format(LETTERS[0],ACCIDENTALS[0], QUALITIES[0]))