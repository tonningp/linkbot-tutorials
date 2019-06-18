#!/usr/bin/env python3

import linkbot3 as linkbot

l = linkbot.CLinkbot('P3S1') # My robot's ID is "ABCD"
l.move_nb(90, 0, 90) # Begin moving each motor 90 degrees
l.move_wait()         # Wait for the motion to complete
l.set_led_color(255, 0, 0)  # Change the LED color
