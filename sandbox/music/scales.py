#!/usr/bin/env python3
import linkbot
import time
import score

#robot = linkbot.Linkbot('98j7') # Replace "98j7" with your Linkbot's ID

def half_step(n):
    a = 1.059463094359
    f0 = 440
    return f0 * (a**n)
    
base_d = 0.25    
durations = {
    '1/32' : base_d * 0.125,
    '1/16' : base_d * 0.25,
    '1/8' : base_d * 0.5,
    '1/4' : base_d,
    'd1/4' : base_d + base_d * 0.5,
    '1/2' : base_d * 2,
    '1' : base_d * 4
}

base_notes = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']
notes = { base_notes[i%12]+str(i//12) : x for i,x in list(enumerate([half_step(x) for x in range(-57,51)])) }

def play_note(robot,note,duration):
    robot.set_buzzer_frequency(notes[note])
    time.sleep(duration)
    robot.set_buzzer_frequency(0)
 
def play_score(score,tempo):
    for n,d in score:
        #play_note(robot,n,durations[d]*tempo)
        print(n,durations[d],notes[n])
        time.sleep(durations[d]*tempo)

play_score(score.beethoven9,1.0)
