from contextlib import suppress
from rover import*
from inputParser import*
import sys



def marsRover(input_file):

    instructions = parseInstructions(input_file)
    #default outputs for rover position for unit testing, if a Rover object can't properly initate it will default to None
    r1Position = None
    r2Position = None

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
        rover1 = Rover("Spirit", R1_start, boundary, R1_instructions)
        rover1.executeInstructions()
        print(rover1.returnFinalPosition())
        r1Position = rover1.returnFinalPosition()
    
        rover2 = Rover("Opportunity", R2_start, boundary, R2_instructions)
        rover2.executeInstructions()
        print(rover2.returnFinalPosition())
        r2Position = rover2.returnFinalPosition()

    except:
        # since there a couple types of errors that can occur I use the generic Exception class here
        with suppress(Exception):
            rover2 = Rover("Opportunity", R2_start, boundary, R2_instructions)
            rover2.executeInstructions()
            print(rover2.returnFinalPosition())
            r2Position = rover2.returnFinalPosition()

    return r1Position, r2Position

def main():
    try:
        input_file = sys.argv[1]
        marsRover(input_file)
    except:
        pass

if __name__=="__main__":
    main()






