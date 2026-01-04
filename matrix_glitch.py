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
    
    arabic_chars = "أبتثجحخدذرزسشصضطظعغفقكلمنهويبةى٠١٢٣٤٥٦٧٨٩"
    
    colors = {
        'reset': "\033[0m",
        'white': "\033[97m",
        'bright': "\033[92m",
        'green': "\033[32m",
        'dim': "\033[90m"
    }
    
    glitch_timer = 0
    
    for i in range(cols):
        if random.random() < 0.3:
            drop_pos[i] = random.uniform(-10, 0)
            drop_speed[i] = random.uniform(0.6, 1.4)
            drop_len[i] = random.randint(8, 22)
    
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
                for i in range(cols):
                    if random.random() < 0.3:
                        drop_pos[i] = random.uniform(-10, 0)
                        drop_speed[i] = random.uniform(0.6, 1.4)
                        drop_len[i] = random.randint(8, 22)
        except:
            pass
        
        sys.stdout.write("\033[H")
        
        lines = []
        glitch_active = False
        
        # Random glitch effect
        if random.random() < 0.002:
            glitch_active = True
            glitch_timer = 3
        
        if glitch_timer > 0:
            glitch_timer -= 1
        
        for y in range(rows):
            line = []
            for x in range(cols):
                char = ' '
                if drop_pos[x] > y:
                    pos = int(drop_pos[x] - y)
                    if pos < drop_len[x]:
                        char = random.choice(arabic_chars)
                        
                        # Glitch effect
                        if glitch_active:
                            if random.random() < 0.3:
                                char = random.choice(['█', '▓', '▒', '░', ' '])
                        
                        if pos == 0:
                            color = colors['white']
                        elif pos < 4:
                            color = colors['bright']
                        elif pos < 10:
                            color = colors['green']
                            if random.random() < 0.1:
                                char = ' '
                        else:
                            color = colors['dim']
                            if random.random() < 0.4:
                                char = ' '
                        
                        line.append(f"{color}{char}{colors['reset']}")
                    else:
                        line.append(" ")
                else:
                    line.append(" ")
            lines.append("".join(line))
        
        sys.stdout.write("\n".join(lines))
        sys.stdout.flush()
        
        # Screen flash glitch
        if glitch_active:
            sys.stdout.write("\033[?5h")
            sys.stdout.flush()
            time.sleep(0.03)
            sys.stdout.write("\033[?5l")
            sys.stdout.flush()
        
        for i in range(cols):
            if drop_pos[i] <= 0 and random.random() < 0.02:
                drop_pos[i] = 1
                drop_speed[i] = random.uniform(0.5, 1.7)
                drop_len[i] = random.randint(8, 24)
            
            if drop_pos[i] > 0:
                drop_pos[i] += drop_speed[i]
                if random.random() < 0.01:
                    drop_speed[i] = random.uniform(0.4, 1.8)
                if drop_pos[i] > rows + 25:
                    drop_pos[i] = 0
        
        time.sleep(0.05)

except KeyboardInterrupt:
    clean_exit()
except Exception as e:
    clean_exit()