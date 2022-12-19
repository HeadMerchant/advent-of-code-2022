ROCK        = 1
PAPER       = 2
SCISSORS    = 3

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

# you lose, draw, win
MATCH_END = {
    "X": -1,
    "Y": 0,
    "Z": 1
}



def result_new_decode(them, match_result):
    match_result = MATCH_END[match_result]
    match_score = 3*(match_result+1)

    them = THEM[them]
    choice_score = 1+(them-1+match_result)%3
    return match_score + choice_score

score = sum((result_new_decode(match_result=match_result, them=them) for them, match_result in strategy))

print(score)