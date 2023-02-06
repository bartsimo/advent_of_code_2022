# Opponent
## A Rock
## B Paper
## C Scissors

# Me
## X Lose 1
## Y Draw 2 
## Z Win 3

# Scores
## Lose: 0
## Draw: 3
## Win: 6

# for comments, see two.py the only thing that changed is the rule for how points are received
def calculate_score(opponent, me):
    score = 0
    if me == "X":
        if opponent == "A":
            return score + 3
        elif opponent == "B":
            return score + 1
        else:
            return score + 2
    elif me == "Y":
        score += 3
        if opponent == "A":
            return score + 1
        elif opponent == "B":
            return score + 2
        else:
            return score + 3
    else:
        score += 6
        if opponent == "A":
            return score + 2
        elif opponent == "B":
            return score + 3
        else:
            return score + 1

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
