#!/usr/bin/env python3

import os
import random
import time
import sys

def clean_exit():
    sys.stdout.write("\033[?25h\033[0m\033[2J\033[H")
    sys.stdout.flush()
    sys.exit(0)

try:
    sys.stdout.write("\033[?25l")
    sys.stdout.flush()
    
    cols, rows = 80, 24
    try:
        cols, rows = os.get_terminal_size()
        cols = min(cols, 200)
        rows = min(rows, 60)
    except:
        pass
    
    drop_pos = [0] * cols
    drop_speed = [0] * cols
    
    arabic_chars = "أبتثجحخدذرزسشصضطظعغفقكلمنهويبةى"
    
    reset = "\033[0m"
    green = "\033[92m"
    white = "\033[97m"
    
    for i in range(cols):
        if random.random() < 0.3:
            drop_pos[i] = random.uniform(-10, 0)
            drop_speed[i] = random.uniform(0.8, 1.2)
    
    while True:
        try:
            new_cols, new_rows = os.get_terminal_size()
            if new_cols != cols or new_rows != rows:
                cols, rows = new_cols, new_rows
                cols = min(cols, 200)
                rows = min(rows, 60)
                drop_pos = [0] * cols
                drop_speed = [0] * cols
                for i in range(cols):
                    if random.random() < 0.3:
                        drop_pos[i] = random.uniform(-10, 0)
                        drop_speed[i] = random.uniform(0.8, 1.2)
        except:
            pass
        
        sys.stdout.write("\033[H")
        
        lines = []
        for y in range(rows):
            line = []
            for x in range(cols):
                char = ' '
                if drop_pos[x] > y:
                    pos = int(drop_pos[x] - y)
                    if pos < 15:
                        char = random.choice(arabic_chars)
                        color = white if pos == 0 else green
                        line.append(f"{color}{char}{reset}")
                    else:
                        line.append(" ")
                else:
                    line.append(" ")
            lines.append("".join(line))
        
        sys.stdout.write("\n".join(lines))
        sys.stdout.flush()
        
        for i in range(cols):
            if drop_pos[i] <= 0 and random.random() < 0.02:
                drop_pos[i] = 1
                drop_speed[i] = random.uniform(0.8, 1.2)
            
            if drop_pos[i] > 0:
                drop_pos[i] += drop_speed[i]
                if drop_pos[i] > rows + 20:
                    drop_pos[i] = 0
        
        time.sleep(0.06)

except KeyboardInterrupt:
    clean_exit()
except Exception as e:
    clean_exit()