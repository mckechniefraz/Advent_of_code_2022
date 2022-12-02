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
            score = score + checkRock(result)
        elif result[1] == "Y":
            score = score + checkPaper(result)
        elif result[1] == "Z":
            score = score + checkScissors(result)
    
    return score
        
    
def checkRock(result):
    '''
    Function to check result if we play rock
    '''
    score = 0
    if result[0] == "C" and result[1] == "X":
        score = score + 7
    elif result[0] == "A" and result[1] == "X":
        score = score + 4
    else:
        score = score + 1
    
    return score


def checkPaper(result):
    '''
    Function to check result if we play paper
    '''
    score = 0
    if result[0] == "A" and result[1] == "Y":
            score = score + 8
    elif result[0] == "B" and result[1] == "Y":
        score = score + 5
    else:
        score = score + 2
    
    return score



def checkScissors(result):
    '''
    Function to check result if we play scissors
    '''
    score = 0
    if result[0] == "B" and result[1] == "Z":
        score = score + 9
    elif result[0] == "C" and result[1] == "Z":
        score = score + 6
    else:
        score = score + 3
    
    return score





if __name__ == "__main__":
    input_path = "./day_02/input.txt"
    plan = getPlan(input_path)
    print (playGame(plan))

