#!/usr/bin/env python3
# Matrix Arabic Rain - Final Version

import os
import random
import time
import sys

def clean_exit():
    """Clean up terminal on exit"""
    sys.stdout.write("\033[?25h\033[0m\033[2J\033[H")
    sys.stdout.flush()
    sys.exit(0)

def main():
    try:
        # Hide cursor
        sys.stdout.write("\033[?25l")
        sys.stdout.flush()
        
        # Get terminal size
        cols, rows = 80, 24
        try:
            cols, rows = os.get_terminal_size()
            cols = min(cols, 200)
            rows = min(rows, 60)
        except:
            pass
        
        # Initialize drops
        drop_pos = [0] * cols
        drop_speed = [0] * cols
        drop_len = [0] * cols
        
        # Arabic characters
        arabic_letters = "أبتثجحخدذرزسشصضطظعغفقكلمنهويبةى"
        arabic_numbers = "٠١٢٣٤٥٦٧٨٩"
        arabic_chars = arabic_letters + arabic_numbers
        
        # Matrix colors
        colors = {
            'reset': "\033[0m",
            'head': "\033[97m",      # White
            'bright': "\033[92m",    # Bright green
            'green': "\033[32m",     # Green
            'dim': "\033[90m",       # Dim green
            'faint': "\033[38;5;22m" # Very faint green
        }
        
        # Start with some drops
        for i in range(cols):
            if random.random() < 0.3:
                drop_pos[i] = random.uniform(-20, 0)
                drop_speed[i] = random.uniform(0.5, 1.5)
                drop_len[i] = random.randint(10, 25)
        
        # Main loop
        while True:
            # Handle terminal resize
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
                            drop_pos[i] = random.uniform(-20, 0)
                            drop_speed[i] = random.uniform(0.5, 1.5)
                            drop_len[i] = random.randint(10, 25)
            except:
                pass
            
            # Move cursor to top
            sys.stdout.write("\033[H")
            
            # Build screen
            lines = []
            for y in range(rows):
                line = []
                for x in range(cols):
                    char = ' '
                    
                    if drop_pos[x] > y:
                        pos = int(drop_pos[x] - y)
                        
                        if pos < drop_len[x]:
                            # Choose character
                            if random.random() < 0.7:
                                char = random.choice(arabic_letters)
                            else:
                                char = random.choice(arabic_numbers)
                            
                            # Get color based on position
                            if pos == 0:
                                color = colors['head']
                            elif pos < 3:
                                color = colors['bright']
                            elif pos < 8:
                                color = colors['green']
                                if random.random() < 0.1:
                                    char = ' '
                            elif pos < 15:
                                color = colors['dim']
                                if random.random() < 0.3:
                                    char = ' '
                            else:
                                color = colors['faint']
                                if random.random() < 0.6:
                                    char = ' '
                            
                            line.append(f"{color}{char}{colors['reset']}")
                        else:
                            line.append(" ")
                    else:
                        line.append(" ")
                
                lines.append("".join(line))
            
            # Draw screen
            sys.stdout.write("\n".join(lines))
            sys.stdout.flush()
            
            # Update drops
            for i in range(cols):
                # Start new drops
                if drop_pos[i] <= 0 and random.random() < 0.02:
                    drop_pos[i] = 1
                    drop_speed[i] = random.uniform(0.4, 1.8)
                    drop_len[i] = random.randint(8, 28)
                
                # Move existing drops
                if drop_pos[i] > 0:
                    drop_pos[i] += drop_speed[i]
                    
                    # Random speed changes
                    if random.random() < 0.01:
                        drop_speed[i] = random.uniform(0.3, 2.0)
                    
                    # Reset if off screen
                    if drop_pos[i] > rows + 30:
                        drop_pos[i] = 0
            
            # Matrix glitch effect (rare)
            if random.random() < 0.001:
                sys.stdout.write("\033[?5h")
                sys.stdout.flush()
                time.sleep(0.04)
                sys.stdout.write("\033[?5l")
                sys.stdout.flush()
            
            # Frame rate
            time.sleep(0.05)
    
    except KeyboardInterrupt:
        clean_exit()
    except Exception:
        clean_exit()

if __name__ == "__main__":
    main()