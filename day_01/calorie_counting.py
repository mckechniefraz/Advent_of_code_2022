
def getElves(file_name):
    '''
    Function to import the list of calories per elf, splitting the list by blank line.
    '''

    with open(file_name, "r") as inputfile:
        elfList = inputfile.read().split("\n\n")
    
    return elfList


def findCalories(elfList):
    '''
    Taking the list of Elves and seeing which Elf is carrying the most calories.

    '''
    maxCalories = 0
    for elf in elfList:
        elfCalories = elf.strip().split("\n")
        elfCalories = [int(i) for i in elfCalories]
        if sum(elfCalories) >= maxCalories:
            maxCalories = sum(elfCalories)
    
    return maxCalories

def findTopThreeCalories(elfList):

    '''
    Taking the list of Elves and creating a dict of all the totals, then returning the sum of the top 3. 

    '''
    
    summedCalories = []
    for elf in elfList:
        elfCalories = elf.strip().split("\n")
        elfCalories = [int(i) for i in elfCalories]
        summedCalories.append(sum(elfCalories))
    
    return sum(sorted (summedCalories, reverse=True) [0:3])

if __name__ == "__main__":
    input_path = "./day_01/input.txt"

    elfList = getElves(input_path)
    # maxCalories = findCalories(elfList)
    topThreeCalories = findTopThreeCalories(elfList)
    print (topThreeCalories)
