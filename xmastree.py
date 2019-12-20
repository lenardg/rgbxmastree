from tree import RGBXmasTree
from time import sleep
import sys
from colorzero import Hue, Color
from random import randint, random, choice

tree = RGBXmasTree()
tree.brightness = 0.5

def red_to_blue(duration):
    hue = 1.0
    t = 0
    tree.color = Color.from_hsv(hue, 1.0, 0.5)
    while t < duration * 20:
        relt = t%100
        if relt > 50:
            hue = 1.0 - ((100-relt) / 50.0 * 0.4)
        else:
            hue = 1.0 - (relt / 50.0 * 0.4)
        tree.color = Color.from_hsv(hue, 1.0, 0.5)
        t = t + 1
        sleep(0.05)

def classical(duration):
    t = 0
    while ( t < duration / 2 ):
        colors = []
        for i in range(len(tree)):
            colors.append(choice([Color('red'), Color('green'), Color('yellow')]))
        tree.value = colors
        t = t + 1
        sleep(2)

def classical_with_blue(duration):
    t = 0
    while ( t < duration / 2 ):
        colors = []
        for i in range(len(tree)):
            colors.append(choice([Color('red'), Color('green'), Color('yellow'), Color('blue'), Color('cyan')]))
        tree.value = colors
        t = t + 1
        sleep(2)

def sparkle(duration):
    t = 0
    c = randint(1,4)
    while t < duration * 20:
        brig = [random() for x in range(len(tree))]
        if c == 1:
            colors = [(b,b,b) for b in brig]
        elif c == 2:
            colors = [(b,0,0) for b in brig]
        elif c == 3:
            colors = [(0,b,0) for b in brig]
        elif c == 4:
            colors = [(0,0,b) for b in brig]

        colors[3] = (1,1,0)
        tree.value = colors
        t = t + 1
        sleep(0.05)

def sparkle2(duration):
    t = 0
    c = randint(1,4)
    brig = [random() for x in range(len(tree))]
    speed = [randint(1,2) for x in range(len(tree))]
    while t < duration * 20:
        if c == 1:
            colors = [(b,b,b) for b in brig]
        elif c == 2:
            colors = [(b,0,0) for b in brig]
        elif c == 3:
            colors = [(0,b,0) for b in brig]
        elif c == 4:
            colors = [(0,0,b) for b in brig]

        colors[3] = (1,1,0)
        tree.value = colors
        
        for i in range(len(speed)):
            if speed[i] == 1:
                if brig[i] < 0.2:
                    speed[i] = 2
                else:
                    brig[i] = brig[i] - 0.1
            elif speed[i] == 2:
                if brig[i] > 0.9:
                    speed[i] = 1
                else:
                    brig[i] = brig[i] + 0.1
        t = t + 1
        sleep(0.01)


def colorswirl(duration):
    t = 0
    groups = [[0, 1, 2],[16, 17, 18],[13,14,15],[4,5,6],[10,11,12],[22,23,24],[19,20,21],[7,8,9]]
    colors = [(1,1,0) for x in range(25)]
    hue = 0
    while t < duration * 20:
        gh = hue
        for g in groups:
            for i in g:
                colors[i] = Color.from_hsv(gh, 1.0, 1.0)
            gh = gh + 0.125
            if gh > 1:
                gh = gh - 1
        hue = hue + 1.0/45.0
        if hue > 1:
            hue = hue - 1

        tree.value = colors
        t = t + 1
        sleep(0.05)

def lighthouse(duration):
    t = 0
    groups = [[0, 1, 2],[16, 17, 18],[13,14,15],[4,5,6],[10,11,12],[22,23,24],[19,20,21],[7,8,9]]
    colors = [(1,1,0) for x in range(25)]
    hue = 0
    while t < duration * 20:
        gh = hue
        for g in groups:
            for i in g:
                colors[i] = Color.from_hsv(1.0, 0.0, gh)
            gh = gh + 0.125
            if gh > 1:
                gh = gh - 1
        hue = hue + 1.0/45.0
        if hue > 1:
            hue = hue - 1

        tree.value = colors
        t = t + 1
        sleep(0.05)


def main(tree):
    while True:
        duration = randint(5,20)
        nextf = randint(1,8)

        if nextf == 1:
            red_to_blue(duration)
        elif nextf == 2:
            classical(duration)
        elif nextf == 3:
            classical_with_blue(duration)
        elif nextf == 4 or nextf == 5:
            sparkle(duration)
        elif nextf == 6 or nextf == 7:
            sparkle2(duration)
        elif nextf == 8:
            colorswirl(duration)

try:
    main(tree)
    tree.off()
except KeyboardInterrupt:
    tree.off()
    sys.exit(0)


