#!/usr/bin/env python3

import linkbot
import time

robot = linkbot.CLinkbot("P3S1")

# Move joint 1 720 degrees, accelerating at 45 deg/sec, traveling at
# a maximum speed of 90 deg/sec, and decelerating at 120 deg/sec at
# the end of the motion.
robot.set_joint_accelerations(45, 45, 45)
robot.set_joint_speeds(180, 180, 180)
robot.set_joint_decelerations(120, 120, 120)
#robot.move(720, j2, j3, mask=mask, wait=False)
robot.move_smooth(720, 0, 720)
