#!/usr/bin/env python3

"""
Author: Darrell H
Date: 6/17/2019

Note: this only works with the older version of PyLinbot
"""
import linkbot
import math
import time

robot = linkbot.Linkbot("ABCD") # replace ABCD with an id number`
robot.wheel_diameter = 4
robot.track_width = 3.7
robot.set_joint_speeds(70, 0, 200)
robot.set_joint_states(1, 0, -1)
time.sleep(4 * 9 / 7)
robot.stop()
