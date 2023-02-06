# Opponent
## A Rock
## B Paper
## C Scissors
# Other
## A Rock
## B Paper
## C Scissors

# Me
## X Rock 1
## Y Paper 2 
## Z Scissors 3

# Scores
## Lose: 0
## Draw: 3
## Win: 6


def calculate_score(opponent, me):
    score = 0
    if me == "X":
        score += 1
        if opponent == "A":
            return score + 3
        elif opponent == "B":
            return score
        else:
            return score + 6
    elif me == "Y":
        score += 2
        if opponent == "A":
            return score + 6
        elif opponent == "B":
            return score + 3
        else:
            return score
    else:
        score += 3
        if opponent == "A":
            return score
        elif opponent == "B":
            return score + 6
        else:
            return score + 3

def get_rounds_inputs(round):
    opponent = round[0]
    me = round[-1]

    return opponent, me




def main():
    total_score = 0

    with open("input2") as f:
        mylist = f.read().splitlines() 

    mylist.pop(-1)

    for i in mylist:
        opponent, me = get_rounds_inputs(i)
        score_of_round = calculate_score(opponent, me)
        total_score += score_of_round

    print(total_score)

if __name__ == "__main__":
    main()
