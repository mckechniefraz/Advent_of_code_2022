def getItems(file_name):
    '''
    Function to import the list of calories per elf, splitting the list by blank line.
    '''

    with open(file_name, "r") as inputfile:
        itemList = inputfile.read().split("\n")
        
    return itemList

def moveCrates(crateLocation, moveSteps):

    crate = crateLocation
    for step in moveSteps:
        step = step.strip().split(",")
        step = [int(i) for i in step]
        # At this point we have a three item list of Ints next step is to move the crates from one pile to another.
        moves = 0
        while moves < step[0]:
            crateMoveing = crate[step[1]-1].pop()
            crate[step[2]-1].append(crateMoveing)
            moves = moves + 1
    return  crate    

def getTopCrates(final_crates):

    topCrates = ""
    for pile in final_crates:
        topCrates = topCrates + pile.pop()
    
    return topCrates



if __name__ == "__main__":
    input_path = "./day_05/input.txt"
    crates_input_path = "./day_05/crates.txt"
    
    steps = getItems(input_path)
    '''
    Example steps to move crates
    ['5,8,2', '2,4,5', '3,3,9', '4,1,8', '5,9,1']
    First number = number of creates
    Second number = source pile
    Third number = destination pile 
    '''

    startingCratesString = getItems(crates_input_path)
    startingCratesList = []
    for crate in startingCratesString:
        crate = crate.strip().split(",")
        startingCratesList.append(crate)

    final_crates = moveCrates(startingCratesList,steps)

    print (getTopCrates(final_crates))