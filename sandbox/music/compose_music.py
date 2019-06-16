#!/usr/bin/env python3

import struct
import numpy as np
from scipy import signal as sg
from scipy.io.wavfile import write
import linkbot
import time

def get_sine_tone(amp=100,sampling_rate=44100,freq=440,duration=1.0):
    #w =  wavesize * np.sin(2 * np.pi * freq * np.arange(sampling_rate*duration) / sampling_rate)
    #return w
    t = np.linspace(0,duration,duration*sampling_rate)
    data = np.sin(2*np.pi*freq*t) * amp
    return np.trim_zeros(data.astype(np.int16))
    #return np.insert(data.astype(np.int16),0,[0] * 10000)

#sq_y = 100 * sg.square(2*np.pi * freq * x / sampling_rate)


def half_step(n):
    a = 1.059463094359
    f0 = 440
    return f0 * (a**n)
    
base_d = 0.5 
durations = {
    '1/32' : base_d * 0.125,
    '1/16' : base_d * 0.25,
    '1/8' : base_d * 0.5,
    '1/4' : base_d,
    '1/3' : base_d * 0.3,
    'd1/4' : base_d + base_d * 0.5,
    '1/2' : base_d * 2,
    '1' : base_d * 4
}

base_notes = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']
notes = { "{}{}".format(base_notes[i%12],i//12) : x for i,x in list(enumerate([half_step(x) for x in range(-57,51)])) }

def play_tone(freq,duration):
    return get_sine_tone(amp=32767,freq=freq,duration=duration)
 
def play_score(score,tempo):
    s = []
    for freq,duration in [(notes[n.upper()],durations[d]) for n,d in score]:
        for n in play_tone(freq,duration*tempo):
            s.append(n)
    return np.array(s)
        

beethoven9 = [
    # https://www.8notes.com/scores/435.asp
    ('C#4','1/4'), ('C#4','1/4'), ('D4','1/4'), ('E4','1/4'), 
    ('E4','1/4'),('D4','1/4'), ('C#4','1/4'), ('B3','1/4'), 
    ('A3','1/4'), ('A3','1/4'),('B3','1/4'), ('C#4','1/4'), 
    ('C#4','d1/4'), ('B3','1/8'),('B3','1/2'),
    ('C#4','1/4'), ('C#4','1/4'),('D4','1/4'), ('E4','1/4'),
    ('E4','1/4'),('D4','1/4'), ('C#4','1/4'), ('B3','1/4'), 
    ('A3','1/4'), ('A3','1/4'),('B3','1/4'), ('C#4','1/4'), 
    ('B3','d1/4'), ('A3','1/8'), ('A3','1/2'),
    ('b3','1/4'), ('b3','1/4'),('c#4','1/4'),('a3','1/4'),
    ('b3','1/4'),('c#4','1/8'),('d4','1/8'),('c#4','1/4'),('a3','1/4'),
    ('b3','1/4'),('c#4','1/8'),('d4','1/8'),('c#4','1/4'),('b3','1/4'),
    ('a3','1/4'),('b3','1/4'),('e3','1/2'),
    ('C#4','1/4'), ('C#4','1/4'), ('D4','1/4'), ('E4','1/4'), 
    ('E4','1/4'),('D4','1/4'), ('C#4','1/4'), ('B3','1/4'), 
    ('A3','1/4'), ('A3','1/4'),('B3','1/4'), ('C#4','1/4'), 
    ('b3','1/2'),('a3','1/8'),('a3','1/2'),
]
starwars = [
    ('C4','1/3'),('C4','1/3'),('C4','1/3'),('F4','1/4'),('c5','1/2'),
    ('A#4','1/3'),('a4','1/3'),('g4','1/3'),('f5','1/4'),('c5','1/2'),
    ('A#4','1/3'),('a4','1/3'),('g4','1/3'),('f5','1/4'),('c5','1/2'),
    ('A#4','1/3'),('a4','1/3'),('a#4','1/3'),('g4','1/2'),
    ('C4','1/3'),('C4','1/3'),('C4','1/3'),('F4','1/4'),('c5','1/2'),
    ('A#4','1/3'),('a4','1/3'),('g4','1/3'),('f5','1/4'),('c5','1/2'),
    ('A#4','1/3'),('a4','1/3'),('g4','1/3'),('f5','1/4'),('c5','1/2'),
    ('A#4','1/3'),('a4','1/3'),('a#4','1/3'),('g4','1/2'),
    
    
    
    ]
scale = [
('C0','1/4'),
('D0','1/4'),
('E0','1/4'),
('F0','1/4'),
('G0','1/4'),
('A0','1/4'),
('B0','1/4'),
('C1','1/4'),
('D1','1/4'),
('E1','1/4'),
('F1','1/4'),
('G1','1/4'),
('A1','1/4'),
('B1','1/4'),
('C2','1/4'),
('D2','1/4'),
('E2','1/4'),
('F2','1/4'),
('G2','1/4'),
('A2','1/4'),
('B2','1/4'),
('C3','1/4'),
('D3','1/4'),
('E3','1/4'),
('F3','1/4'),
('G3','1/4'),
('A3','1/4'),
('B3','1/4'),
('C4','1/4'),
('D4','1/4'),
('E4','1/4'),
('F4','1/4'),
('G4','1/4'),
('A4','1/4'),
('B4','1/4'),
('C5','1/4'),
('D5','1/4'),
('E5','1/4'),
('F5','1/4'),
('G5','1/4'),
('A5','1/4'),
('B5','1/4'),
('C6','1/4'),
('D6','1/4'),
('E6','1/4'),
('F6','1/4'),
('G6','1/4'),
('A6','1/4'),
('B6','1/4'),
('C7','1/4'),
('D7','1/4'),
('E7','1/4'),
('F7','1/4'),
('G7','1/4'),
('A7','1/4'),
('B7','1/4'),
('C8','1/4'),
]
zero = [
('C0','1/4'),
('D0','1/4'),
('E0','1/4'),
('F0','1/4'),
('G0','1/4'),
('A0','1/4'),
('B0','1/4'), 
('C1','1/4')
]
one = [
('C1','1/4'),
('D1','1/4'),
('E1','1/4'),
('F1','1/4'),
('G1','1/4'),
('A1','1/4'),
('B1','1/4'), 
('C2','1/4')
]
two = [
('C2','1/4'),
('D2','1/4'),
('E2','1/4'),
('F2','1/4'),
('G2','1/4'),
('A2','1/4'),
('B2','1/4'), 
('C3','1/4')
  
]

data = play_score(beethoven9,1.0)
#scaled = np.int16(data/np.max(np.abs(data)) * 32767)
write('9th.wav',44100,data)
data = play_score(starwars,1.0)
#scaled = np.int16(data/np.max(np.abs(data)) * 32767)
write('starwars.wav',44100,data)

#play_score(starwars,0.25)

