ROCK        = 1
PAPER       = 2
SCISSORS    = 3


RESULT_SCORES = [3, 6, 0]
def get_result_score(you, them):
    you = YOU[you]
    return RESULT_SCORES[(you - THEM[them]) % 3] + you

THEM = {
    "A": ROCK,
    "B": PAPER,
    "C": SCISSORS
}

YOU = {
    "X": ROCK,
    "Y": PAPER,
    "Z": SCISSORS
}

with open("day2.txt", "r") as f:
    strategy = (line.strip().split(" ") for line in f.readlines())

score = sum((get_result_score(you=you, them=them) for them, you in strategy))

print(score)