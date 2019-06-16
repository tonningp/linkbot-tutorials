#!/usr/bin/env python3
"""
Author: Paul T
Date: 6/14/2019

"""

import linkbot
robot = linkbot.CLinkbot("ABCD") # change to your id
radius = 1.75
robot.driveDistance(6,radius)
robot.driveDistance(-8,radius)
robot.driveDistance(2,radius)
