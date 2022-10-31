#test case:
# 5 5
# 1 2 N
# LMLMLMLMM

from rover import*
from inputParser import*
import sys
    
def executeInstructions(rover, instructions):
    
    for i in instructions:
        if i == "L" or i == "l":
            rover.turnLeft()
        elif i == "R" or i == "r":
            rover.turnRight()
        elif i == "M" or i == "m":
            rover.moveForward()
        else: # the rover will ignore any invalid commands 
            pass
    

def main():
    
    instructions = parseInstructions(sys.argv[1])
    boundary = instructions[0]

    #There is a scenario where the inputs for the first rover are invalid and we need to skip
    #it and move on to the next rover
    R1_start = instructions[1]
    R1_instructions = instructions[2]


    R2_start = instructions[3]
    R2_instructions = instructions[4]

    #since the rovers move sequentially, there is the scenario where the first rover can't move,
    #but the second one can. We can catch this exception in a try/except
    try:
        rover1 = Rover("Spirit", R1_start, boundary)
        executeInstructions(rover1, R1_instructions)
        print(rover1.returnFinalPosition())

        rover2 = Rover("Opportunity", R2_start, boundary)
        executeInstructions(rover2, R2_instructions)
        print(rover2.returnFinalPosition())
    except:
        rover2 = Rover("Opportunity", R2_start, boundary)
        executeInstructions(rover2, R2_instructions)
        print(rover2.returnFinalPosition())

    
    
    
    

if __name__=="__main__":
    main()






