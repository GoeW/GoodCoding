#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# team: Marcel, Gorden, 
# Expert name: unknown, blabla

import random
import time
import sys
import matplotlib.pyplot as plt

def get_random_number(start, end):
    num = random.randint(start, end)
    return num


def write_log_file(outputfilename, data):
    f = open(outputfilename + ".log", "a")
    f.write("Our randomly generated number is " + str(data) + " (" + time.strftime("%H:%M:%S") + ")\n")
    f.close()

def get_colour_by_dice(spots):
    colordict = {1: 'red', 2: 'blue', 3: 'purple', 4: 'yellow', 5: 'green', 6: 'black'}
    return colordict[spots]

if __name__ == "__main__":
    outputfilename = "randomNumber"
    roll_list = []
    for i in range(6):
        roll = get_random_number(1, 6)
        rolls_list.append(roll)
    color = get_colour_by_dice(roll)
    write_log_file(outputfilename, color)
    print(rolls_list)
    sys.stdout.flush()
    plt.bar(range(6),rolls_list)
    plt.show()
