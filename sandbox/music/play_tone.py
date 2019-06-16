#!/usr/bin/env python3

import struct
import numpy as np
from scipy import signal as sg

def get_sine_tone(sampling_rate=44100,freq=440,duration=1.0):
    return 100 * np.sin(2 * np.pi * freq * np.arange(sampling_rate*duration) / sampling_rate)

#sq_y = 100 * sg.square(2*np.pi * freq * x / sampling_rate)

get_sine_tone(freq=220).astype(np.int16).tofile('test.wav')
