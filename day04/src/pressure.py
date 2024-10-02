import random

def emit_gel(step):
    pressure: int = 50
    while pressure < 100 and pressure >= 0:
        recieved = yield pressure
        if recieved:
            step = recieved
        if step >= 0:
            pressure += random.randint(0, step + 1)
        else:
            pressure += random.randint(step, 0 + 1)

step: int = 10
gen = emit_gel(step)
iteration: int = 0

try:
    for i in gen:
        print(i)
        if (i > 80 and step > 0) or (i < 20 and step < 0):
            step = -step
            gen.send(step)
            iteration += 1
except(KeyboardInterrupt):
    print('stopped')
finally:
    print(f'wow! its {iteration} iterations!')