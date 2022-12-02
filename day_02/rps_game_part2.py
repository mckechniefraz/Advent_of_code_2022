def getPlan(file_name):
    '''
    Function to import the list of calories per elf, splitting the list by blank line.
    '''

    with open(file_name, "r") as inputfile:
        gamePlan = inputfile.read().split("\n")
        
    return gamePlan


def playGame(gamePlan):
    '''
    Function to play the game
    '''
    score = 0
    for game in gamePlan:
        result = game.strip().split(" ")
        if result[1] == "X":
            score = score + lose(result)
        elif result[1] == "Y":
            score = score + draw(result)
        elif result[1] == "Z":
            score = score + win(result)
        
    
    return score
        

def lose(result):
    '''
    Function to return the score if we lose the game
    '''
    score = 0

    if result[0] == "A":
        score = score + 3
    elif result[0] == "B":
        score = score + 1
    elif result[0] == "C":
        score = score + 2

    return score

def draw(result):
    '''
    Function to return the score if we draw the game
    '''
    scores = {"A":1,"B":2,"C":3}

    score = scores.get(result[0], None)

    score = score + 3

    return score


def win(result):
    '''
    Function to return the score if we win the game
    '''
    score = 6

    if result[0] == "A":
        score = score + 2
    elif result[0] == "B":
        score = score + 3
    elif result[0] == "C":
        score = score + 1

    return score




if __name__ == "__main__":
    input_path = "./day_02/input.txt"
    plan = getPlan(input_path)
    print (playGame(plan))

