#this class represents the rover, and since there two rovers a class would be appropriate here
class Rover(object):

    headings = ("N", "E", "S", "W")

    def __init__(self, name, coordinates):

        self.name = name
        self.x = coordinates[0]
        self.y = coordinates[1]
        self.direction = coordinates[2]

    #depending on which way the Rover is currently facing make it turn left
    #make sure that the inputs are validated before it gets here
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

    #depending on which way the rover is facing, make it move in that direction
    def moveForward(self):
        if self.direction ==  "N":
            self.y = self.y + 1
        elif self.direction ==  "S":
            self.y = self.y - 1
        elif self.direction ==  "W":
            self.x = self.x - 1
        elif self.direction == "E":
            self.x = self.x + 1

    #useful for returning the end position of the rover to check where it ended up
    def returnPosition(self):
        return self.x, self.y, self.direction

    

   

    