import linkbot

robot = linkbot.CLinkbot("ABCD") # change to your Id

radius = 1.75  # if you are using the blue wheels, 2.0 if using the teal wheels
trackwidth = 3.69

robot.driveAngle(720)
robot.turnLeft(90,radius)
robot.driveDistance(6,radius)
robot.turnRight(90,radius)
