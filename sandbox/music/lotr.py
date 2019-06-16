#!/usr/bin/env python3

import linkbot
import time


robot = linkbot.Linkbot('p3s1') # Replace "ABCD" with your Linkbot's ID

def half_step(n):
    a = 1.059463094359
    f0 = 440
    return f0 * (a**n)
    
base_d = 0.5 
durations = {
    '1/32' : base_d * 0.125,
    '1/16' : base_d * 0.25,
    '1/8' : base_d * 0.5,
    'd1/8' : base_d * 0.5 + base_d * 0.25,
    '1/4' : base_d,
    '1/3' : base_d * 0.3,
    'd1/4' : base_d + base_d * 0.5,
    '1/2' : base_d * 2,
    '1' : base_d * 4
}

base_notes = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']
notes = { "{}{}".format(base_notes[i%12],i//12) : x for i,x in list(enumerate([half_step(x) for x in range(-57,51)])) }

def play_tone(robot,freq,duration):
    robot.set_buzzer_frequency(freq)
    time.sleep(duration)
    robot.set_buzzer_frequency(0)
 
def play_score(score,tempo):
    for freq,duration in [(notes[n.upper()],durations[d]) for n,d in score]:
        print(duration,freq)
        play_tone(robot,freq,duration*tempo)
        
hobbits = [
    # https://www.8notes.com/scores/435.asp
    ('D5','1/16'),('E5','1/16'),
    ('F#5','1/4'),('A5','1/4'),('F#5','1/4'),('E5','1/4'),
    ('D5','1/2'),('F#5','1/4'),('A5','1/4'),
    ('B5','d1/4'),('D6','1/8'),('C#6','1/4'),('A5','1/4'),
    ('F#5','d1/4'),('G5','1/16'),('F#5','1/16'),('E5','d1/4'),('D5','1/16'),('E5','1/16'),
    ('F#5','1/4'),('A5','1/4'),('F#5','1/8'),('E5','1/16'),('D5','d1/8'),('E5','1/16'),
    ('D5','1/2'),('F#5','1/4'),('A5','1/4'),
    ('b5','1/2'),('a5','1/4'),('f#5','1/4'),
    ('a5','1/8'),('f#5','1/2'),('d5','d1/4'),('d5','1/16'),('e5','1/16'),
    ('f#5','1/4'),('a5','1/4'),('f#5','1/4'),('e5','1/4'),
    ('d5','1/2'),('f#5','1/4'),('a5','1/4'),
    ('b5','d1/4'),('d6','1/8'),('c#6','1/4'),('a5','1/4'),
]

play_score(hobbits,0.5)

