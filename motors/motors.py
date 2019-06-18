#!/usr/bin/env python3

import linkbot3.peripherals
import linkbot3.async as linkbot
import asyncio
import time

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

async def play_tone(robot,freq,duration):
  robot.set_buzzer_frequency(freq)
  await asyncio.sleep(duration)
  robot.set_buzzer_frequency(0)
 
async def play_score(serial_id,score,tempo):
    for freq,duration in [(notes[n.upper()],durations[d]) for n,d in score]:
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


async def task(l):
    accel = await l.motors[0].accel()
    decel = await l.motors[0].decel()
    print('Current accel, decel values: ', await accel, await decel)
    print('Setting to a slow value of 30 deg/s/s')
    fut = await l.motors[0].set_accel(30)
    await fut
    fut = await l.motors[0].set_decel(30)
    await fut
    fut = await l.motors[0].set_omega(180)
    await fut
    print('Testing a series of smooth movements...')
    fut = await l.motors[0].set_controller(linkbot3.Motor.Controller.SMOOTH)
    await fut
    angle = 360

    for i in range(5):
        fut = await l.motors[0].move(angle)
        await fut
        fut = await l.motors[0].move_wait()
        await fut

        fut = await l.motors[0].move(-angle)
        await fut
        fut = await l.motors[0].move_wait()
        await fut

        angle /= 2

    print('Testing again with faster accel/decel of 120 deg/s/s')
    fut = await l.motors[0].set_accel(120)
    await fut
    fut = await l.motors[0].set_decel(120)
    await fut
    angle = 360

    for i in range(5):
        fut = await l.motors[0].move(angle)
        await fut
        fut = await l.motors[0].move_wait()
        await fut

        fut = await l.motors[0].move(-angle)
        await fut
        fut = await l.motors[0].move_wait()
        await fut

        angle /= 2

async def task2(serial_id):
  while 1:
    print(serial_id+' it works')
    await asyncio.sleep(0.5)

async def get_bot(serial_id):
  l = await linkbot.AsyncLinkbot.create(serial_id)
  return l

async def run_main():
  #asyncio.run(multiple_tasks('6J3Q'))

if __name__ == '__main__':
  loop = asyncio.get_event_loop()
  loop.run_until_complete(asyncio.gather(
    task(l),
    #task2('6J3Q'),
    play_score(l,hobbits,0.5)
))
  loop.close() 
