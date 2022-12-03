from string import ascii_lowercase, ascii_uppercase

def getItems(file_name):
    '''
    Function to import the list of calories per elf, splitting the list by blank line.
    '''

    with open(file_name, "r") as inputfile:
        itemList = inputfile.read().split("\n")
        
    return itemList

def checkBackPack(backPackList):
    '''
    Function to work out the priority per three elfs. 
    '''

    totalPriority = []
    priority = checkItems(backPackList)
    totalPriority = totalPriority + priority

    return totalPriority



def checkItems(items):
    '''
    Function to check each of the items carried by the first elf with elf two and three
    '''
    mixedItems = []
    firstElf = items[0]
    secondElf = items[1]
    thirdElf = items[2]

    for item in firstElf:
        if item in secondElf and item in thirdElf:
            if item not in mixedItems:
                mixedItems.append(item)
    
    lowerNumbers = [lowerLetters[character] for character in mixedItems if character in lowerLetters]
    upperNumbers = [upperLetters[character] for character in mixedItems if character in upperLetters]
    numbers = lowerNumbers + upperNumbers

    return numbers
   
def calcPriority(itemPriority):
    '''
    Function to add up all of the priorities and return a total. 
    '''

    itemInt = [int(i) for i in itemPriority]
    return sum(itemInt)

if __name__ == "__main__":
    input_path = "./day_03/input.txt"

    '''
    Using the ascii_lowercase and uppercase packages to map a-z and A-Z to numbers. 
    '''
    lowerLetters = {letter: str(index) for index, letter in enumerate(ascii_lowercase, start=1)} 
    upperLetters = {letter: str(index) for index, letter in enumerate(ascii_uppercase, start=27)} 

    itemList = getItems(input_path)
    priority = []
    '''
    Using backpack as a int to count the lines in groups of three, this will run while backpack is less than the total lines in the input file. 
    ''' 
    backpack = 0
    while backpack < len(itemList):
        
        backpackItems = [itemList[backpack], itemList[backpack+1], itemList[backpack+2]]
        backpack = backpack + 3
        priority = priority + checkBackPack(backpackItems)
    
    print (calcPriority(priority))


