import math

def signal(N, phase=0):
    for x in range(N):
        yield math.sin((2*math.pi*x + phase)/N)
