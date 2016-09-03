# Problem Set 6: Simulating robots
# Name:
# Collaborators:
# Time:

import math
import random

import ps6_visualize
import pylab
import matplotlib.pyplot as plt

# === Provided classes

class Position(object):
    """
    A Position represents a location in a two-dimensional room.
    """
    def __init__(self, x, y):
        """
        Initializes a position with coordinates (x, y).
        """
        self.x = x
        self.y = y
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getNewPosition(self, angle, speed):
        """
        Computes and returns the new Position after a single clock-tick has
        passed, with this object as the current position, and with the
        specified angle and speed.

        Does NOT test whether the returned position fits inside the room.

        angle: float representing angle in degrees, 0 <= angle < 360
        speed: positive float representing speed

        Returns: a Position object representing the new position.
        """
        old_x, old_y = self.getX(), self.getY()
        # Compute the change in position
        delta_y = speed * math.cos(math.radians(angle))
        delta_x = speed * math.sin(math.radians(angle))
        # Add that to the existing position
        new_x = old_x + delta_x
        new_y = old_y + delta_y
        return Position(new_x, new_y)

# === Problems 1

class RectangularRoom(object):
    """
    A RectangularRoom represents a rectangular region containing clean or dirty
    tiles.

    A room has a width and a height and contains (width * height) tiles. At any
    particular time, each of these tiles is either clean or dirty.
    """
    def __init__(self, width, height):
        """
        Initializes a rectangular room with the specified width and height.

        Initially, no tiles in the room have been cleaned.

        width: an integer > 0
        height: an integer > 0
        """
        # raise NotImplementedError
        self.width = width
        self.height = height
        self.cleaned = dict()
    
    def cleanTileAtPosition(self, pos):
        """
        Mark the tile under the position POS as cleaned.

        Assumes that POS represents a valid position inside this room.

        pos: a Position
        """
        # raise NotImplementedError
        # assumption: for tile (2.1, 2.2), the tile (2, 2) is cleaned; 
        self.cleaned[(int(pos.getX()), int(pos.getY()))] = True

    def isTileCleaned(self, m, n):
        """
        Return True if the tile (m, n) has been cleaned.

        Assumes that (m, n) represents a valid tile inside the room.

        m: an integer
        n: an integer
        returns: True if (m, n) is cleaned, False otherwise
        """
        # raise NotImplementedError
        if (int(m), int(n)) in self.cleaned.keys(): return True
        else: return False
    
    def getNumTiles(self):
        """
        Return the total number of tiles in the room.

        returns: an integer
        """
        # raise NotImplementedError
        return int(self.width) * int(self.height)

    def getNumCleanedTiles(self):
        """
        Return the total number of clean tiles in the room.

        returns: an integer
        """
        # raise NotImplementedError
        return len(self.cleaned.keys())

    def getRandomPosition(self):
        """
        Return a random position inside the room.

        returns: a Position object.
        """
        # raise NotImplementedError
        return Position(random.uniform(0.0, float(self.width)), random.uniform(0.0, float(self.height)))

    def isPositionInRoom(self, pos):
        """
        Return True if pos is inside the room.

        pos: a Position object.
        returns: True if pos is in the room, False otherwise.
        """
        # raise NotImplementedError
        if pos.getX() >= 0 and pos.getX() < self.width and pos.getY() >= 0 and pos.getY() < self.height: return True
        return False

# if __name__ == '__main__':
#     '''
#     test for the room class
#     '''
#     testRoom = RectangularRoom(4, 5)
#     testpos = Position(2.1, 2.3)
#     testpos_clean = Position(3.9, 2.4)
#     testRoom.cleanTileAtPosition(testpos_clean)
#     testRoom.cleanTileAtPosition(Position(1.5, 3.4))
#     testRoom.cleanTileAtPosition(Position(1.6, 3.2))
#     print testRoom.isTileCleaned(.4, 2.1)


class Robot(object):
    """
    Represents a robot cleaning a particular room.

    At all times the robot has a particular position and direction in the room.
    The robot also has a fixed speed.

    Subclasses of Robot should provide movement strategies by implementing
    updatePositionAndClean(), which simulates a single time-step.
    """
    def __init__(self, room, speed):
        """
        Initializes a Robot with the given speed in the specified room. The
        robot initially has a random direction and a random position in the
        room. The robot cleans the tile it is on.

        room:  a RectangularRoom object.
        speed: a float (speed > 0)
        """
        # raise NotImplementedError
        self.room = room
        self.speed = speed
        self.position = Position(self.room.getRandomPosition().getX(), self.room.getRandomPosition().getY())
        self.direction = random.uniform(0.0, 360.0)

    def getRobotPosition(self):
        """
        Return the position of the robot.

        returns: a Position object giving the robot's position.
        """
        # raise NotImplementedError
        return self.position
    
    def getRobotDirection(self):
        """
        Return the direction of the robot.

        returns: an integer d giving the direction of the robot as an angle in
        degrees, 0 <= d < 360.
        """
        # raise NotImplementedError
        return self.direction

    def setRobotPosition(self, position):
        """
        Set the position of the robot to POSITION.

        position: a Position object.
        """
        # raise NotImplementedError
        self.position = position
        # return self.position

    def setRobotDirection(self, direction):
        """
        Set the direction of the robot to DIRECTION.

        direction: integer representing an angle in degrees
        """
        # raise NotImplementedError
        self.direction = direction 
        # return self.direction

    def updatePositionAndClean(self):
        """
        Simulate the raise passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        # raise NotImplementedError
        self.room.cleanTileAtPosition(self.position)
        self.position = self.position.getNewPosition(self.direction, self.speed)
        

# if __name__ == '__main__':
#     '''
#     test the robot class
#     '''
#     room = RectangularRoom(4, 5)
#     speed = 4.0
#     rob1 = Robot(room, speed)
#     pos = Position(2.3, 3.4)
#     rob1.setRobotPosition(pos)
#     rob1.setRobotDirection(340)
#     print rob1.getRobotPosition().getX(), rob1.getRobotPosition().getY()
#     print rob1.room.cleaned
#     rob1.updatePositionAndClean()
#     print rob1.room.cleaned
#     print rob1.getRobotPosition().getX(), rob1.getRobotPosition().getY()


# === Problem 2
class StandardRobot(Robot):
    """
    A StandardRobot is a Robot with the standard movement strategy.

    At each time-step, a StandardRobot attempts to move in its current direction; when
    it hits a wall, it chooses a new direction randomly.
    """
    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        # raise NotImplementedError
        while not self.room.isPositionInRoom(self.position.getNewPosition(self.direction, self.speed)):
            self.setRobotDirection(random.uniform(0.0, 360.0))
            # print self.direction
        Robot.updatePositionAndClean(self)

# if __name__ == '__main__':
#     '''
#     for checking the Standard Robot Class
#     '''
#     room = RectangularRoom(4, 5)
#     speed = 4.0
#     rob1 = StandardRobot(room, speed)
#     print rob1.getRobotPosition().getX(), rob1.getRobotPosition().getY()
#     print rob1.room.cleaned
#     rob1.updatePositionAndClean()
#     print rob1.getRobotPosition().getX(), rob1.getRobotPosition().getY()
#     print rob1.room.cleaned





# === Problem 4
#
# 1) How long does it take to clean 80% of a 20*20 room with each of 1-10 robots
#
# 2) How long does it take two robots to clean 80% of rooms with dimensions 
#	 20x20, 25x16, 40x10, 50x8, 80x5, and 100x4

def showPlot1():
    """
    Produces a plot showing dependence of cleaning time on number of robots.
    """ 
    # raise NotImplementedError
    x_axis = list()
    y_axis = list()
    for i in range(1, 11):
        
        x_axis.append(i)
        y_axis.append(runSimulation(i, 1.0, 20, 20, .8, 10, StandardRobot))

    plt.plot(x_axis, y_axis, 'bo')
    plt.xlabel('Robot Numbers')
    plt.ylabel('Avg Time to Clean a Room')
    plt.title('Robot Numbers versus Avg Cleaning Time')
    plt.show()


def showPlot2():
    """
    Produces a plot showing dependence of cleaning time on room shape.
    """
    # raise NotImplementedError
    x_axis = list()
    y_axis = list()
    width_list = [20, 25, 40, 50, 80, 100]
    height_list = [20, 16, 10, 8, 5, 4]
    
    for i in range(len(width_list)):    
        x_axis.append(width_list[i]*1.0/height_list[i])
        y_axis.append(runSimulation(2, 1.0, width_list[i], height_list[i], .8, 100, StandardRobot))

    plt.plot(x_axis, y_axis, 'bo')
    plt.xlabel('width/height ratio')
    plt.ylabel('Avg Time to Clean a Room')
    plt.title('width/height ratio versus Avg Cleaning Time')
    plt.show()

# if __name__ == '__main__':
#     showPlot2()


# === Problem 5

class RandomWalkRobot(Robot):
    """
    A RandomWalkRobot is a robot with the "random walk" movement strategy: it
    chooses a new direction at random after each time-step.
    """
    # raise NotImplementedError
    def updatePositionAndClean(self):
        self.setRobotDirection(random.uniform(0.0, 360.0))
        while not self.room.isPositionInRoom(self.position.getNewPosition(self.direction, self.speed)):
            self.setRobotDirection(random.uniform(0.0, 360.0))
        # print self.position.getX(), self.position.getY()
        Robot.updatePositionAndClean(self)

# === Problem 3

def runSimulation(num_robots, speed, width, height, min_coverage, num_trials,
                  robot_type):
    """
    Runs NUM_TRIALS trials of the simulation and returns the mean number of
    time-steps needed to clean the fraction MIN_COVERAGE of the room.

    The simulation is run with NUM_ROBOTS robots of type ROBOT_TYPE, each with
    speed SPEED, in a room of dimensions WIDTH x HEIGHT.

    num_robots: an int (num_robots > 0)
    speed: a float (speed > 0)
    width: an int (width > 0)
    height: an int (height > 0)
    min_coverage: a float (0 <= min_coverage <= 1.0)
    num_trials: an int (num_trials > 0)
    robot_type: class of robot to be instantiated (e.g. Robot or
                RandomWalkRobot)
    """
    # raise NotImplementedError
    
    
    counter = 0
    for i in range(num_trials):
        # anim = ps6_visualize.RobotVisualization(num_robots, width, height)
        room = RectangularRoom(width, height)       
        
        rob_list = list()
        for r in range(num_robots):
            rob_list.append(robot_type(room, speed))
        
        while min_coverage*room.getNumTiles() > room.getNumCleanedTiles(): 
            for r_b in rob_list: 
                r_b.updatePositionAndClean()

            # anim.update(room, rob_list)
            counter += 1
            
        # anim.done()
    return counter*1.0/num_trials



# if __name__ == '__main__':
#     print runSimulation(1, 1.0, 10, 10, .9, 10, StandardRobot)
# === Problem 6

# For the parameters tested below (cleaning 80% of a 20x20 square room),
# RandomWalkRobots take approximately twice as long to clean the same room as
# StandardRobots do.
def showPlot3():
    """
    Produces a plot comparing the two robot strategies.
    """
    # raise NotImplementedError
    x_0 = [5, 10, 15, 20, 25, 30]
    y_s = list()
    y_r = list()
    x = list()
    for i in x_0:
        x.append(i ** 2)
        y_s.append(runSimulation(1, 1.0, i, i, .9, 1, StandardRobot))
        y_r.append(runSimulation(1, 1.0, i, i, .9, 1, RandomWalkRobot))
    plt.plot(x, y_s, 'r^', x, y_r, 'bs')

    plt.xlabel('Room Area')
    plt.ylabel('Avg Time to Clean a Room')
    plt.title('different algorithm')
    
    plt.show()
    plt.show()
if __name__ == '__main__':
    showPlot3()