#this class represents the rover, and since there two rovers a class would be appropriate here
class Rover(object):

    def __init__(self, name, coordinates, boundary):

        self.name = name
        self.x = coordinates[0]
        self.y = coordinates[1]
        self.direction = coordinates[2]
        self.x_bound = boundary[0]
        self.y_bound = boundary[1]

    #depending on which way the Rover is currently facing make it turn left
    #inputParser will turn the lower case to upper case
    def turnLeft(self):
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
        if self.direction ==  'N':
            self.direction = "E"
        elif self.direction == "W":
            self.direction = "N"
        elif self.direction == "S":
            self.direction = "W"
        elif self.direction == "E":
            self.direction = "S"

    def safetyCheck(self):
        if self.x < 0:
            errorMsg = self.name + " is about to fall off the plateau. Stopping here: " + "0", str(self.y), self.direction
            exit(errorMsg)
        elif self.y < 0:
            errorMsg = self.name + " is about to fall off the plateau. Stopping here: " + str(self.x), "0", self.direction
            exit(errorMsg)
        elif self.x > self.x_bound:
            errorMsg = self.name + " is about to fall off the plateau. Stopping here: " + str(self.x_bound), str(self.y), self.direction
            exit(errorMsg)
        elif self.y > self.y_bound:
            errorMsg = self.name + " is about to fall off the plateau. Stopping here: " + str(self.x), str(self.y_bound), self.direction
            exit(errorMsg)

    #depending on which way the rover is facing, make it move in that direction
    def moveForward(self):
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

    #useful for returning the end position of the rover to check where it ended up
    def returnPosition(self):
        return self.x, self.y

    def returnFinalPosition(self):
        return self.x, self.y, self.direction

    