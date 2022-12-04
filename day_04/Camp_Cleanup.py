
def getItems(file_name):
    '''
    Function to import the list of calories per elf, splitting the list by blank line.
    '''

    with open(file_name, "r") as inputfile:
        itemList = inputfile.read().split("\n")
        
    return itemList


def compareAreas(areas):
    '''
    Function to compare each of the areas for overlap
    '''
    

    duplicateCount = 0

    for pair in areas:
        duplicateA = True
        duplicateB = True

        area = pair.strip().split(",")
        # Creating the list for each Elf and changing those strings into Integers
        elfOneArea = area[0].split("-")
        elfOneAreas = range(int(elfOneArea[0]), int(elfOneArea[1])+1)
        elfTwoArea = area[1].split("-")
        elfTwoAreas = range(int(elfTwoArea[0]), int(elfTwoArea[1])+1)  

        # Checking to see if each of the areas for Elf One appear in Elf Two, if they don't set duplicate to False.    
        for i in elfOneAreas:
            if i not in elfTwoAreas:
                duplicateA = False
        
        # Checking to see if each of the areas for Elf Two appear in Elf One, if they don't set duplicate to False.    
        for l in elfTwoAreas:
            if l not in elfOneAreas:
                duplicateB = False
        # If either duplicate A or B are True, add 1 to the duplicate count. 
        if duplicateA == True or duplicateB == True:
            duplicateCount = duplicateCount + 1

    return (duplicateCount)






if __name__ == "__main__":
    input_path = "./day_04/input.txt"
    '''
    Example input 71-87,70-88
    '''


    areas = getItems(input_path)
    duplicate = compareAreas(areas)
    print (duplicate)

