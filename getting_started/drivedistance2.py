#!/usr/bin/env python3

import linkbot
robot = linkbot.CLinkbot("P3S1")
radius = 1.75
robot.driveDistance(6,radius)
robot.driveDistance(-8,radius)
robot.driveDistance(2,radius)
