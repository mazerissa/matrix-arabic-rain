<div align="center">

<h1>Matrix Arabic Rain 🌧️🔢</h1>

<img src="https://img.shields.io/badge/matrix-arabic%20rain-brightgreen" alt="Matrix Arabic Rain">
<img src="https://img.shields.io/badge/python-3.6+-blue.svg" alt="Python 3.6+">
<img src="https://img.shields.io/badge/terminal-ascii%20color-green" alt="Terminal ASCII Color">
<img src="https://img.shields.io/badge/license-mit-yellow.svg" alt="MIT License">

<br>
<br>

<img src="matrix_demo.gif" width="1200">
<br>
<em>Arabic script cascading in the iconic Matrix style</em>

</div>

A mesmerizing terminal-based digital rain effect inspired by **The Matrix**, but with a twist – it uses beautiful Arabic script instead of Japanese katakana. Watch as Arabic letters and numbers cascade down your screen in the iconic green-on-black Matrix style.

## ✨ Features

- **Authentic Matrix Effect**: Real digital rain with proper fading trails and speed variations
- **Arabic Script**: Uses Arabic letters (أ ب ت ث...) and Eastern Arabic numerals (٠ ١ ٢...)
- **Cinematic Visuals**:
  - Bright white head characters
  - Green-to-faint color gradients
  - Glitch effects like in the movie
  - Variable drop speeds and lengths
- **No Dependencies**: Pure Python, works anywhere
- **Terminal Friendly**: Automatically adjusts to terminal size
- **Silent Operation**: No intros, no status bars – just pure visuals

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/mazerissa/matrix-arabic-rain.git
cd matrix-arabic-rain

# Run it!
python matrix_final.py
```

Press **Ctrl+C** to exit gracefully.

## 📁 Project Structure

```
matrix-arabic-rain/
├── matrix_basic.py      # Basic Arabic rain
├── matrix_numbers.py    # Added Arabic numbers
├── matrix_fade.py       # Enhanced with fading trails
├── matrix_glitch.py     # Added Matrix glitch effects
├── matrix_speed.py      # Variable speed drops
├── matrix_final.py      # Final optimized version ★
├── requirements.txt     # Python requirements (none needed!)
├── README.md           # This file
├── matrix_demo.gif     # Demo animation
├── LICENSE             # MIT License
└── .gitignore         # Git ignore file
```

## 🔧 Requirements

- **Python 3.6+** (no external libraries needed!)
- **Terminal with UTF-8 support** (for Arabic characters)
- **ANSI color support** (most modern terminals have this)

### Terminal Recommendations:
- **Windows**: Windows Terminal, PowerShell 7+
- **macOS**: Terminal.app, iTerm2
- **Linux**: GNOME Terminal, Konsole, xterm
- **All Platforms**: WezTerm, Alacritty

## 🎮 Usage

### Run the Final Version
```bash
python matrix_final.py
```

### Try Different Versions
See the evolution of the effect:
```bash
python matrix_basic.py     # Basic rain
python matrix_numbers.py   # Added numbers
python matrix_fade.py      # With fading effect
python matrix_glitch.py    # With glitch effects
python matrix_speed.py     # Variable speeds
```

### Best Viewing Experience
1. **Maximize** your terminal window
2. Use a **black background** for the best effect
3. **Turn off lights** for full cinematic immersion
4. Terminal with **true color support** recommended

## 🎨 Visual Features

### Color Scheme
- **Head**: Bright white (changes rapidly)
- **Body**: Classic Matrix green (#00FF00)
- **Trail**: Fading green to faint green
- **Glitches**: Occasional screen flickers and character corruption

### Character Set
- **70% Arabic letters**: أ ب ت ث ج ح خ د ذ ر ز س ش ص ض ط ظ ع غ ف ق ك ل م ن ه و ي ة ى
- **30% Arabic numerals**: ٠ ١ ٢ ٣ ٤ ٥ ٦ ٧ ٨ ٩
- **No other symbols**: Pure Arabic script only

### Effects
- **Variable speeds**: Each drop moves at its own pace
- **Fading trails**: Characters fade out naturally
- **Matrix glitches**: Rare screen flickers and corruption
- **Density variations**: Some columns are empty, creating rain-like patterns
- **Resize aware**: Automatically adjusts to terminal size changes

## 📚 Development Journey

This project was built in logical steps, each adding a new feature:

| # | Feature Added | File |
|---|--------------|------|
| 1 | Basic Arabic rain | `matrix_basic.py` |
| 2 | Arabic numbers | `matrix_numbers.py` |
| 3 | Fading trail effect | `matrix_fade.py` |
| 4 | Matrix glitch effects | `matrix_glitch.py` |
| 5 | Variable speed drops | `matrix_speed.py` |
| 6 | Final optimized version | `matrix_final.py` |
| 7 | Requirements | `requirements.txt` |
| 8 | Complete documentation | `README.md` |
| 9 | Demo animation | `matrix_demo.gif` |
| 10 | License file | `LICENSE` |
| 11 | Git ignore file | `.gitignore` |

## 🧪 How It Works

The effect uses a simple but effective algorithm:

1. **Drop Management**: Each column can have a "drop" of characters
2. **Position Tracking**: Each drop has position, speed, and length
3. **Character Selection**: Random Arabic characters for each position
4. **Color Grading**: Position-based color selection (head→white, body→green, tail→faint)
5. **Screen Buffer**: Builds the entire frame then renders at once for smooth animation
6. **Glitch System**: Random screen flickers and character corruption

## 🐛 Troubleshooting

### Arabic Characters Not Showing?
```bash
# Check your terminal encoding
echo $LANG

# On Linux/macOS, try setting UTF-8
export LANG=en_US.UTF-8

# On Windows, use Windows Terminal or PowerShell 7+
```

### Colors Not Working?
- Ensure your terminal supports ANSI colors
- Try a different terminal application
- Check terminal settings for "Enable ANSI colors"

### Too Fast/Slow?
Edit `matrix_final.py` and change the sleep time:
```python
time.sleep(0.05)  # Change this value (0.03 = faster, 0.08 = slower)
```

## 🤝 Contributing

Want to make this even cooler? Here are some ideas:

- [ ] Add different color themes (blue, red, custom)
- [ ] Create a "wave" mode where drops move in sine waves
- [ ] Add sound effects (beeps for glitches)
- [ ] Make it interactive (pause, speed up, slow down)
- [ ] Create a web version with JavaScript

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details.

## 🌟 Credits

- Inspired by **The Matrix** (1999)
- Arabic script adds a unique cultural twist
- Pure Python implementation - no dependencies!
- Built for terminal enthusiasts and Matrix fans

## 🎯 Perfect For

- **Terminal screensavers**
- **Coding break entertainment**
- **Teaching Arabic script in a fun way**
- **Matrix-themed events**
- **Impressing your developer friends**

---

<div align="center">

**"You take the blue pill, the story ends. You take the red pill, you stay in Wonderland, and I show you how deep the rabbit hole goes."**  
*- Morpheus*

[![Watch the Demo](https://img.shields.io/badge/WATCH-DEMO-red?style=for-the-badge)](https://github.com/mazerissa/matrix-arabic-rain/blob/main/matrix_demo.gif)
[![Star this repo](https://img.shields.io/badge/⭐-Star_this_repo-yellow?style=for-the-badge)](https://github.com/mazerissa/matrix-arabic-rain/stargazers)
[![Fork](https://img.shields.io/badge/🍴-Fork_me-blue?style=for-the-badge)](https://github.com/mazerissa/matrix-arabic-rain/fork)

</div>

---

**Tip**: For the full experience, run this in a dark room with your terminal maximized. The green glow of Arabic script raining down is hypnotic! 🌌