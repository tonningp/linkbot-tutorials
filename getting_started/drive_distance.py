#!/usr/bin/env python3
"""
Author: Paul T
date: June 15
program: drive_distance.py
"""
import linkbot
robot = linkbot.CLinkbot("P3S1")

robot.driveDistance(8, 1.75)
robot.driveDistance(-5, 1.75)
