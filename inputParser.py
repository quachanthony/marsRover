

def checkGridSize(input_list):
    if len(input_list) < 2:
        print("Insufficient information received. Please send new instructions.")
    elif len(input_list) > 2:
        print("Too much info received, ignoring excess info.")

    passed_check = []
    if not input_list[0].isnumeric() or not input_list[1].isnumeric():
        print("Invalid initial coordinates")
    else:
        passed_check.append(int(input_list[0]))
        passed_check.append(int(input_list[1]))
    
    return passed_check

def checkInitialCoordinates(input_list):
    # check the number of arguments
    passed_check = []
    if len(input_list) != 3:
        print('Invalid number of inputs. Please send new instructions.')
    
    # check that the coordinate arguments are numeric
    if not input_list[0].isnumeric() or not input_list[1].isnumeric():
        print("Invalid initial coordinates")
    else:
        passed_check.append(int(input_list[0]))
        passed_check.append(int(input_list[1]))

    # check that the heading given to the rover is valid, we will accept lowercase as well
    valid_headings = ['N','S','E','W','n','s','e','w']
    heading = input_list[2]
    if any(valid in valid_headings for valid in heading):
        passed_check.append(heading.upper())
    else:
        print('That is not a valid heading. Please send new instructions.')

    return passed_check
    

#This script validates the input before passing it off to the other functions and objects
def parseInstructions(file):
    # read in the text file line by line
    f = open(file, "r").readlines()
    
    #check to see if there are the correct lines in the text file
    if len(f) < 5:
        print("Insufficient information received. Please send new instructions.")
    elif len(f) > 5:
        print("Too much info received, ignoring excess info.")
    #remove the newline characters and split the string up into a list
    clean_inputs = []
    for line in f:
        # it is possible that there could be empty lines in between valid lines
         if line not in ['\n', '\r', '\r\n']: 
            clean_inputs.append(line.strip().split(" "))

    #all of these inputs are strings and we need some of them to be numbers
    gridArea = clean_inputs[0]
    rover1_initial = clean_inputs[1]
    rover1_instructions = clean_inputs[2][0]
    rover2_initial = clean_inputs[3]
    rover2_instructions = clean_inputs[4][0]

    return checkGridSize(gridArea), checkInitialCoordinates(rover1_initial), rover1_instructions, checkInitialCoordinates(rover2_initial), rover2_instructions

    
    
    
    