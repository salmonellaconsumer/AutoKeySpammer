# Auto Key Spammer - Multi-Platform Key Spammer

Auto Key Spammer is a lightweight tool designed to repeatedly press a specific key with customizable settings. It allows you to automate keypresses on multiple platforms: Linux, Windows, and macOS. The program features an intuitive graphical user interface (GUI) built with Tkinter, making configuration and control easy.

---

![screenshot](https://i.imgur.com/p7KrT2V.png)


## Features

- **Customizable Spam Key**: Choose the key you want to spam.
- **Adjustable Key Press Interval**: Set the delay between key presses in milliseconds.
- **Simple GUI**: A user-friendly interface built with Tkinter for easy configuration.
- **Start/Stop Key**: Control the spamming with a configurable start/stop key.
- **Cross-Platform Support**: Works on Linux, Windows, and macOS.
- **Fully Customizable Keys**: Tailor the key press settings to your needs by modifying the keys' text file.
- **Easy translation**: Add a column to the translations CSV file to support additional languages.

## Requirements

- **Python 3.x** (for testing or compiling the program; releases will be available later).
    - `pynput` library: Install with `pip install pynput`.
    - `pyautogui` library: Install with `pip install pyautogui`.
    - `xdotool` (Linux only): Install with `sudo apt install xdotool`.

---

## How to Run

Follow these steps to create the environment, install dependencies, and run the program.

### 1. Clone the Repository

If you haven’t already, start by cloning this repository to your local machine:

```bash
git clone https://github.com/yourusername/auto-key-spammer.git
cd auto-key-spammer
```

### 2. Create a Virtual Environment

It's recommended to use a virtual environment to manage dependencies. If you don’t have `venv` installed, make sure you have Python 3.x installed on your system.

- **Linux/macOS**:

```bash
python3 -m venv venv
source venv/bin/activate
```

- **Windows**:

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

Once the virtual environment is activated, install the required libraries:

```bash
pip install -r requirements.txt
```

Alternatively, you can manually install the libraries with the following commands:

```bash
pip install pynput pyautogui
```

- For **Linux users**, make sure you have `xdotool` installed by running:

```bash
sudo apt install xdotool
```

### 4. Run the Program

Once all dependencies are installed, run the `main.py` script to start the program:

```bash
python main.py
```

This will launch the graphical user interface (GUI) where you can configure your key press settings.

---
## How to Use

### Configuration
1. **Base Key (Spam)**: Choose the key you want to spam (e.g., 'Esc', 'Enter', 'Space','a', 'b', etc.).
2. **Start/Stop Key**: Set the key to start/stop spamming (e.g., 'Esc', 'Enter', 'Space','a', 'b', etc.).
3. **Interval (ms)**: Set the interval (in milliseconds) between each key press.

### Start/Stop Spamming
- Press the configured start/stop key to begin or stop spamming.

---

## WINDOWS USERS: Please Note

- Windows Defender may flag the executable from the releases as a virus. This is a common issue with PyInstaller.
  If it causes too much trouble or makes you feel uncomfortable, consider running the program using Python directly instead.


---

## Linux Specific Requirements

On Linux, this program uses `xdotool` to simulate key presses. Make sure it's installed with the following command:

```bash
sudo apt install xdotool
