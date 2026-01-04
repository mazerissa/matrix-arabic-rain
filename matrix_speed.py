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
    drop_len = [0] * cols
    drop_age = [0] * cols
    
    arabic_chars = "أبتثجحخدذرزسشصضطظعغفقكلمنهويبةى٠١٢٣٤٥٦٧٨٩"
    
    colors = {
        'reset': "\033[0m",
        'white': "\033[97m",
        'bright': "\033[92m",
        'green': "\033[32m",
        'dim': "\033[90m",
        'faint': "\033[38;5;22m"
    }
    
    for i in range(cols):
        if random.random() < 0.3:
            drop_pos[i] = random.uniform(-15, 0)
            drop_speed[i] = random.uniform(0.4, 1.8)
            drop_len[i] = random.randint(8, 26)
            drop_age[i] = 0
    
    while True:
        try:
            new_cols, new_rows = os.get_terminal_size()
            if new_cols != cols or new_rows != rows:
                cols, rows = new_cols, new_rows
                cols = min(cols, 200)
                rows = min(rows, 60)
                drop_pos = [0] * cols
                drop_speed = [0] * cols
                drop_len = [0] * cols
                drop_age = [0] * cols
                for i in range(cols):
                    if random.random() < 0.3:
                        drop_pos[i] = random.uniform(-15, 0)
                        drop_speed[i] = random.uniform(0.4, 1.8)
                        drop_len[i] = random.randint(8, 26)
                        drop_age[i] = 0
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
                    if pos < drop_len[x]:
                        # Some characters appear more often
                        if random.random() < 0.6:
                            char = random.choice(arabic_chars[:20])
                        else:
                            char = random.choice(arabic_chars)
                        
                        # Color based on position and speed
                        speed_factor = drop_speed[x] / 1.8
                        if pos == 0:
                            color = colors['white']
                        elif pos < 3:
                            color = colors['bright']
                        elif pos < 8:
                            color = colors['green']
                        elif pos < 15:
                            color = colors['dim']
                            if random.random() < 0.2 + speed_factor * 0.1:
                                char = ' '
                        else:
                            color = colors['faint']
                            if random.random() < 0.5 + speed_factor * 0.2:
                                char = ' '
                        
                        line.append(f"{color}{char}{colors['reset']}")
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
                drop_speed[i] = random.uniform(0.3, 2.0)
                drop_len[i] = random.randint(6, 28)
                drop_age[i] = 0
            
            if drop_pos[i] > 0:
                drop_pos[i] += drop_speed[i]
                drop_age[i] += 1
                
                # Speed changes based on age and randomness
                if drop_age[i] > 20 and random.random() < 0.01:
                    drop_speed[i] = random.uniform(0.3, 2.2)
                
                # Older drops can speed up or slow down
                if drop_age[i] > 50 and random.random() < 0.02:
                    drop_speed[i] *= random.uniform(0.8, 1.2)
                
                if drop_pos[i] > rows + 30:
                    drop_pos[i] = 0
                    drop_age[i] = 0
        
        # Occasionally change many speeds at once (wind effect)
        if random.random() < 0.005:
            for i in range(cols):
                if drop_pos[i] > 0:
                    drop_speed[i] *= random.uniform(0.9, 1.1)
        
        time.sleep(0.05)

except KeyboardInterrupt:
    clean_exit()
except Exception as e:
    clean_exit()