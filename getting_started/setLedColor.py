#!/usr/bin/env python3
import linkbot

robot = linkbot.CLinkbot("ABCD")  # put the serial id of the linkbot in the string
red = 55      # the red intensity from 0 to 255
green = 255   # the green instensity from 0 to 255
blue = 0      # the blue intensity
robot.set_led_color(red,green,blue)  # this will set the color to green
