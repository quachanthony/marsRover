import os
from platform import platform

def checkGridSize(input_list):
    """
    @desc - this function is meant to parse the first line of the input file to make sure that plateau coordinates that we receive
            are actually valid.
    @param - input_list(list of strings): this list ideally contains two items from the text file that are the x and y coordinates 
             of the plateau
    @returns - passed_check(list of ints): this is the valid coordinates as ints if they exist. Can partially return too
    @throws - print statements to the terminal if errors are encountered 
    """
    passed_check = []
    if len(input_list) < 2:
        print("Cannot define plateau. Please send new instructions.")
        return passed_check
    elif len(input_list) > 2:
        print("Too much info received, ignoring excess info.")

    #check and see if the plateau coordinates are numbers 
    if not input_list[0].isnumeric() or not input_list[1].isnumeric():
        print("Invalid plateau dimensions. Please send new instructions.")
    else:
        passed_check.append(int(input_list[0]))
        passed_check.append(int(input_list[1]))
    
    
    return passed_check

def checkInitialCoordinates(input_list):
    """
    @desc - this function is meant to parse lines 2 and 4 of the text file for initial x,y, and heading of each Rover
    @param - input_list(list of strings): comes from the text file
    @returns - passed_check(list with 2 ints and string): if valid, it will return x and y as ints and the heading as a string. Can partially return too
    @throws - print statements to the terminal if errors are encountered 
    """
    # check the number of arguments
    passed_check = []
    if len(input_list) < 3:
        print("Invalid number of rover inputs. Please send new instructions.")
        return passed_check
    # check that the coordinate arguments are numeric
    # this also takes into account negative inputs
    elif not input_list[0].isnumeric() or not input_list[1].isnumeric():
        print("Invalid initial coordinates")
        return passed_check
    else:
        #these strings are transformed into ints and added to the list
        passed_check.append(int(input_list[0]))
        passed_check.append(int(input_list[1]))

    # check that the heading given to the rover is valid, we will accept lowercase as well
    valid_headings = ['N','S','E','W','n','s','e','w']
    heading = input_list[2]
    if len(input_list[2]) != 1:
        print('Heading must be a single letter.')
    elif any(valid in valid_headings for valid in heading):
        passed_check.append(heading.upper())
    else:
        print('That is not a valid heading. Please send new instructions.')

    return passed_check

#This script validates the input before passing it off to the other functions and objects
def parseInstructions(file):
    """
    @desc - This is the main parsing function that decides whether or not all the information that is needed is there
    @param - file(text file): this is the name of the text file that we want to read in
    @returns - list of lists in this order: plateau coordinates, Spirit initial coordinates, Spirit Instructions, Opp. initial coordinates, Opp Instructions
    @throws - printed error messages to the terminal
    """
    #determine if the file is a valid file type
    ext = os.path.splitext(file)[1]
    if ext != '.txt':
        print("Invalid file type. Please send new instructions.")
        #probably a better way to do this, but opted for an "all or nothing" strategy, so that I could get predictable failure modes for testing
        return None, None, None, None, None
        
    else:
        # read in the text file line by line
        f = open(file, "r").readlines()
        
        #check to see if there are the correct number of lines in the text file
        if len(f) < 5:
            print("Insufficient information received. Please send new instructions.") 
            return None, None, None, None, None
        #too much info can still be salvaged depending on what it is
        elif len(f) > 5:
            print("Too much info received, ignoring excess info.")

        #remove the newline characters and split the string up into a list
        clean_inputs = []
        for line in f:
            # it is possible that there could be empty lines in between valid lines
            if line not in ['\n', '\r', '\r\n', '\s']: 
                # this takes care of multiple spaces being in the row after the split and will return as normal
                clean = line.strip().split(" ")
                clean = list(filter(('').__ne__, clean))
                clean_inputs.append(clean)

        #all of these inputs are strings and we need some of them to be numbers which is handled in the above helper functions
        grid = clean_inputs[0]
        plateau = checkGridSize(grid)
        rover1_initial = clean_inputs[1]
        rover1_instructions = clean_inputs[2][0] #should be a 1 item list
        rover2_initial = clean_inputs[3]
        rover2_instructions = clean_inputs[4][0]

        return plateau, checkInitialCoordinates(rover1_initial), rover1_instructions, checkInitialCoordinates(rover2_initial), rover2_instructions

    
    
    
    