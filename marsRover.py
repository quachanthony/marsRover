#test case:
# 5 5
# 1 2 N
# LMLMLMLMM

from rover import*
from inputParser import*

    
def executeInstructions(rover, instructions):
    
    for i in instructions:
        if i == "L":
            rover.turnLeft()
        elif i == "R":
            rover.turnRight()
        elif i == "M":
            rover.moveForward()
        else: # the rover will ignore any invalid commands 
            pass
    

def main():
    
    instructions = parseInstructions('instructions.txt')
    minMax = instructions[0]
    R1_start = instructions[1]
    R1_instructions = instructions[2]
    R2_start = instructions[3]
    R2_instructions = instructions[4]
    rover1 = Rover("Spirit", R1_start)
    executeInstructions(rover1, R1_instructions)
    rover2 = Rover("Opportunity", R2_start)
    executeInstructions(rover2, R2_instructions)

    print(rover1.returnPosition())
    print(rover2.returnPosition())
    
    

if __name__=="__main__":
    main()






