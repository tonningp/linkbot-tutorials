"""
Author: Alex B
date: June 15
program: review.ch 
"""
import linkbot
robot = linkbot.CLinkbot("P3S1")

robot.driveAngle(360)
robot.turnLeft(90, 1.75, 3.69)
robot.driveDistance(6, 1.75)
