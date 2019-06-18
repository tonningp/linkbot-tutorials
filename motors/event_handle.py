#!/usr/bin/env python3
import linkbot

robot = linkbot.CLinkbot("6J3Q")
robot.move_to(0,0,0)
robot.motors[0].move(720, wait=False)
robot.motors[2].move(720, wait=False)
robot.motors[0].move_wait()
robot.motors[2].move_wait()
