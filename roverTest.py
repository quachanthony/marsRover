import os
from marsRover import marsRover
from inputParser import*

#these functions are quality of life functions, they print to the console in different colors so you can easily see if tests pass or fail
#rprint is red, gprint is green, mprint is magenta 
def rprint(skk): print("\033[91m{}\033[00m" .format(skk))
def gprint(skk): print("\033[92m{}\033[00m" .format(skk))
def mprint(skk): print("\033[95m{}\033[00m" .format(skk))

class UnitTest(object):
    """
    @desc - This is a class for making a Unit Test object that we will use to test the various use cases that the Rovers will encounter
    @param - testName(string): This is a short description of what the test is that object will be testing\
           - input_file(.txt file): This is the input that the object will read and must correspond to the test being run
    @returns - The output from marsRover and a green string if the test passed and a red string if the test failed with the wrong out
               output and the expected correct output
    """

    def __init__(self, testName, input_file):
        #Class constructor
        self.testName = testName
        self.input_file = input_file

    def passOrFail(self, expected):
        """
        @desc - This class method is responsible for calling marsRover and comparing the output to an expected value
        @param - expected(list): this list should contain two items. The first is output for Spirit, the second for Opportunity
                 If marsRover cannot successfully initate and take a Rover to completion, it will return None.
        @returns - prints the test name and result, pass or fail, to the console.
        @throws - any errors that were encountered during the execution of marsRover will also be printed to the console 
        """
        answer = marsRover(self.input_file)
        if answer == expected:
            gprint(self.testName + " PASSED")
            print("___________________________________________________________________")
        else:
            rprint(self.testName + " FAILED" + " got " + str(answer) + " instead of " + str(expected))
            print("___________________________________________________________________")

    def showInput(self):
        #this is just a helper function to show what the input text file looks like for more complicated cases
        f = open(self.input_file, "r").readlines()
        for line in f:
            print(line)

def testMarsRover():
    """
    @desc - this is the main testing function. This is where all the UnitTest objects are created and where the expected outputs
            should be entered
    @param - takes no parameters
    @returns - results of the tests to the terminal 
    """
    #for organization, I put all the test files into their own directory. Change directories to access these files
    os.chdir('marsRover/test_files')

    mprint("********************")
    mprint("1. TESTING BASE CASE")
    mprint("********************")
    
    #Given example case
    UnitTest("Base Case", "baseCase.txt").passOrFail(('Spirit: 1 3 N', 'Opportunity: 5 1 E'))

    mprint("*****************************")
    mprint("2. TESTING INPUT FILE FORMATS")
    mprint("*****************************")
    UnitTest("Invalid File Extension", "instructions.jpg").passOrFail((None, None))
    UnitTest("Too Few Rows", "tooFewRows.txt").passOrFail((None, None))
    UnitTest("Empty Text File", "empty.txt").passOrFail((None, None))
    UnitTest("Too Many Rows", "tooManyRows.txt").passOrFail(('Spirit: 1 3 N', 'Opportunity: 5 1 E'))
    UnitTest("Blank Rows at the End of File", "blankRowsEnd.txt").passOrFail(('Spirit: 1 3 N', 'Opportunity: 5 1 E'))
    UnitTest("Blank Rows in Middle of File", "blankRowsMiddle.txt").passOrFail(('Spirit: 1 3 N', 'Opportunity: 5 1 E'))
    #extra info in the middle, where part of it is valid (lrm will make it move N 1 step)
    UnitTest("Extra Info in the Middle", "extraInfoMiddle.txt").passOrFail(('Spirit: 1 3 N', None))

    mprint("******************************")
    mprint("3. TESTING PLATEAU COORDINATES")
    mprint("******************************")
    UnitTest("Invalid Plateau Coordinate", "invalidPlateau.txt").passOrFail((None,None)) 
    UnitTest("Only 1 Plateau Coordinate", "onePlateauCoordinate.txt").passOrFail((None, None))
    UnitTest("3 Plateau Coordinates Given", "3PlateauCoordinates.txt").passOrFail(('Spirit: 1 3 N', 'Opportunity: 5 1 E'))
    UnitTest("Plateau Coordinate Contains Float","floatPlateau.txt").passOrFail((None, None))
    UnitTest("Negative Plateau Coordinate Given", "negativePlateauCoordinate.txt").passOrFail((None, None))
    UnitTest("Double Digit Numbers for Plateau", "doubleDigitPlateau.txt").passOrFail(('Spirit: 1 3 N', 'Opportunity: 5 1 E'))
    UnitTest("Too many spaces between Plateau Inputs", "tooManyPlateauSpaces.txt").passOrFail(('Spirit: 1 3 N', 'Opportunity: 5 1 E'))
    
    mprint("****************************")
    mprint("4. TESTING ROVER COORDINATES")
    mprint("****************************")
    UnitTest("Rover Coordinates Contain Float Given to Spirit", "roverFloat.txt").passOrFail((None, 'Opportunity: 5 1 E'))
    UnitTest("Negative Rover Coordinate Given to Spirit", "negativeRoverCoordinate.txt").passOrFail(('Spirit: 1 3 N', None))
    UnitTest("Negative Rover Coordinate Given to Opportunity", "negativeStartingCoordinate.txt").passOrFail((None, 'Opportunity: 5 1 E'))
    UnitTest("Spirit Coordinates Contain Invalid Character", "invalidRoverCoordinate.txt").passOrFail((None, 'Opportunity: 5 1 E'))
    UnitTest("Opportunity Coordinates Contain Invalid Character", "invalidRoverCoordinate2.txt").passOrFail(('Spirit: 1 3 N', None))
    UnitTest("Double Digit Initial Rover Coordinates", "ddRover.txt").passOrFail(('Spirit: 10 21 N', 'Opportunity: 32 28 E'))
    UnitTest("Rover Instructions Contain No Valid Commands", "noValidCommands.txt").passOrFail(('Spirit: 1 2 N', 'Opportunity: 3 3 E'))
    UnitTest("Only 1 Rover Coordinate Given", "oneRoverCoordinate.txt").passOrFail(('Spirit: 1 3 N', None))
    UnitTest("No Heading Given to Opportunity", "noHeadingGiven.txt").passOrFail(('Spirit: 1 3 N', None))
    UnitTest("No Heading Given to Spirit", "noHeadingGiven2.txt").passOrFail((None, 'Opportunity: 5 1 E'))
    UnitTest("Spirit Given Invalid Heading", "invalidHeading.txt").passOrFail((None, 'Opportunity: 5 1 E'))
    UnitTest("Opportunity Given Invalid Heading", "invalidHeading2.txt").passOrFail(('Spirit: 1 3 N', None))
    UnitTest("Opportunity Initial Coordinates off the Max Bounds of Plateau", "outOfBounds.txt").passOrFail(('Spirit: 1 3 N', None))
    UnitTest("Spirit Initial Coordinates off the Max Bounds of Plateau", "outOfBounds2.txt").passOrFail((None, 'Opportunity: 5 1 E'))
    UnitTest("Only Lowercase Commands Given to Both Rovers", "lowercaseCommands.txt").passOrFail(('Spirit: 1 3 N', 'Opportunity: 5 1 E'))
    UnitTest("Too many spaces between Rover Coordinates", "tooManyRoverSpaces.txt").passOrFail(('Spirit: 1 3 N', 'Opportunity: 5 1 E'))
    UnitTest("Heading as Word", "headingAsWord.txt").passOrFail((None, 'Opportunity: 5 1 E'))

    mprint("********************************")
    mprint("5. TESTING ROVER LEAVING PLATEAU")
    mprint("********************************")
    # I chose to show the inputs for these tests to better illustrate this mechanic
    north = UnitTest("Move North Off Plateau", "moveOffY.txt")
    north.showInput()
    north.passOrFail(('Spirit: 1 5 N', 'Opportunity: 5 1 E'))
    northCorrect = UnitTest("Moving North Off Plateau, but Later Commands Keep It On", "correctiveActionN.txt")
    northCorrect.showInput()
    northCorrect.passOrFail(('Spirit: 3 5 E', 'Opportunity: 5 1 E'))

    south = UnitTest("Move South Off Plateau", "moveToNegativeY.txt")
    south.showInput()
    south.passOrFail(('Spirit: 1 0 S', 'Opportunity: 5 1 E'))
    southCorrect = UnitTest("Moving South Off Plateau, but Later Commands Keep It On", "correctiveActionS.txt")
    southCorrect.showInput()
    southCorrect.passOrFail(('Spirit: 2 0 E', 'Opportunity: 5 1 E'))

    east = UnitTest("Move East Off Plateau", "moveOffX.txt")
    east.showInput()
    east.passOrFail(('Spirit: 5 2 E', 'Opportunity: 5 1 E'))
    eastCorrect = UnitTest("Moving East Off Plateau, but Later Commands Keep It On", "correctiveActionE.txt")
    eastCorrect.showInput()
    eastCorrect.passOrFail(('Spirit: 5 4 N', 'Opportunity: 5 1 E'))
    
    west = UnitTest("Move West Off Plateau", "moveToNegativeX.txt")
    west.showInput()
    west.passOrFail(('Spirit: 0 2 W', 'Opportunity: 5 1 E'))
    westCorrect = UnitTest("Moving West Off Plateau, but Later Commands Keep It On", "correctiveActionW.txt")
    westCorrect.showInput()
    westCorrect.passOrFail(('Spirit: 0 3 N', 'Opportunity: 5 1 E'))

    

def main():
    testMarsRover()
    
if __name__=="__main__":
    main()