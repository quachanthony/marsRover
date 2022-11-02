#this class represents the rover, and since there two rovers a class would be appropriate here. 
class Rover(object):

    def __init__(self, name, coordinates, boundary, instructions):
        """
        @desc - This is the constructor method for the Rover class, the main class in this program
        @param - name (string): the name of the Rover since there are two I will call them Spirit and Opportunity after the real ones
               - coordinates (array): should contain the initial coordinates of the rover in the order x, y, direction 
               - boundary (array): should contain the x and y coordinates that describe the top right corner of the plateau
               - instructions (string): the string of commands given to the Rover to move around the plateau
        @returns - a fully or sometimes partially defined Rover object
        @throws - Will see errors printed on the console
                - IndexError and TypeError will be thrown most often when the object isn't fully defined going into the rest of the program
                - These errors will be handled by the try/except in main mostly
        """
        self.name = name
        self.x = coordinates[0]
        self.y = coordinates[1]
        self.direction = coordinates[2]
        self.x_bound = boundary[0]
        self.y_bound = boundary[1]
        self.instructions = instructions
        
    def turnLeft(self):
        """
        @desc - class method for Rover that changes the heading to the Left based on the instructions. It is a setter
        @param - is called on a Rover object
        @returns - Alters the Rover's current heading
        @throws - Errors are handled in the inputParser function
        """
        #there are a lot of ways to do this, but since the inputParser will only accept valid headings, I thought this way would be simplest
        #also there are only 4 possible ways it can move, so it's easily handled in this way
        if self.direction ==  'N':
            self.direction = "W"
        elif self.direction == "W":
            self.direction = "S"
        elif self.direction == "S":
            self.direction = "E"
        elif self.direction == "E":
            self.direction = "N"
        
    #make the rover turn right
    def turnRight(self):
        """
        @desc - class method for Rover that changes the heading to the Right based on the instructions. It is a setter
        @param - is called on a Rover object
        @returns - Alters the Rover's current heading
        @throws - Errors are handled in the inputParser function
        """
        if self.direction ==  'N':
            self.direction = "E"
        elif self.direction == "W":
            self.direction = "N"
        elif self.direction == "S":
            self.direction = "W"
        elif self.direction == "E":
            self.direction = "S"

    def safetyCheck(self):
        """
        @desc - This class method checks to see if the Rover is going to make a move that will put it outside the bounds of the plateau.
                If it is about to come off, the Rover will stop and report it's position. Combine this method with moveForward() to check
                the progress of the Rover as it moves across the Plateau.
        @param - is called on a Rover object
        @returns - prints a warning message to the console. 
        """
        if self.x < 0:
            self.x = 0
            errorMsg = self.name + " is about to fall off the plateau. Stopping here: " + self.returnPosition() #str(self.x) + " " +str(self.y) + " "+ self.direction
            print(errorMsg)
        elif self.y < 0:
            self.y = 0
            errorMsg = self.name + " is about to fall off the plateau. Stopping here: " +  self.returnPosition() #str(self.x) + " "+ str(self.y) + " "+ self.direction
            print(errorMsg)
        elif self.x > self.x_bound:
            self.x = self.x_bound
            errorMsg = self.name + " is about to fall off the plateau. Stopping here: " + self.returnPosition() #str(self.x_bound) + " "+ str(self.y) + " "+ self.direction
            print(errorMsg)
        elif self.y > self.y_bound:
            self.y = self.y_bound
            errorMsg = self.name + " is about to fall off the plateau. Stopping here: " +  self.returnPosition()#str(self.x) + " "+ str(self.y_bound) + " "+ self.direction
            print(errorMsg)

    #depending on which way the rover is facing, make it move in that direction
    def moveForward(self):
        """
        @desc - This class method moves the Rover forward, in its current direction, when it receives the instruction to do so
        @param - is called on a Rover object
        @returns - alters the x and y values of the Rover
        @throws - console warnings from safetyCheck() 
        """
        if self.direction ==  "N":
            self.y = self.y + 1
            self.safetyCheck()
        elif self.direction ==  "S":
            self.y = self.y - 1
            self.safetyCheck()
        elif self.direction ==  "W":
            self.x = self.x - 1
            self.safetyCheck()
        elif self.direction == "E":
            self.x = self.x + 1
            self.safetyCheck()

    def executeInstructions(self):
        """
        @desc - This class method executes the instructions that were passed to the rover
        @param - is called on a Rover object
        @returns - alters the x and y values of the Rover
        @throws - console warnings from safetyCheck() 
        """
        for i in self.instructions:
            #this method will accept lowercase inputs from instructions as well
            if i == "L" or i == "l":
                self.turnLeft()
            elif i == "R" or i == "r":
                self.turnRight()
            elif i == "M" or i == "m":
                self.moveForward()
            else: # the rover will ignore any invalid commands 
                pass

    
    def returnPosition(self):
        """
        @desc - This class method is used by safetyCheck() to show the last safe position of the Rover before it falls off the Plateau
        @param - is called on a Rover object
        @returns - the x, y and heading of the Rover in a string to the console
        """
        return str(self.x) + " "+ str(self.y) + " "+ str(self.direction)

    #purely for reporting purposes 
    def returnFinalPosition(self):
        """
        @desc - This class method shows the final position that the Rover ended up after all the instructions were executed
        @param - is called on a Rover object
        @returns - the name, x, y and heading of the Rover in a string to the console
        """
        return self.name + ": " + str(self.x) + " " + str(self.y) + " " + str(self.direction)

    