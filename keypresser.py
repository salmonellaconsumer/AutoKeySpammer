import sys
import time
import threading
import subprocess
from pynput.keyboard import Controller, Key
import pyautogui

class KeyPresser:
    def __init__(self):
        self.running = False
        self.base_key = 'a'
        self.interval = 0.1
        self.keyboard = Controller()

        if sys.platform.startswith('linux'):
            if not subprocess.call(["which", "xdotool"], stdout=subprocess.DEVNULL) == 0:
                raise EnvironmentError("Install xdotool with `sudo apt install xdotool`")
        elif sys.platform == 'win32':
            try:
                import pyautogui
            except ImportError:
                raise EnvironmentError("Install pyautogui with `pip install pyautogui`")

    def configure(self, base_key: str, interval_ms: int):
        self.base_key = getattr(Key, base_key, base_key)
        self.interval = interval_ms / 1000.0

    def start(self):
        if not self.running:
            self.running = True
            threading.Thread(target=self._spam_loop, daemon=True).start()

    def stop(self):
        self.running = False

    def _spam_loop(self):
        while self.running:
            if sys.platform.startswith('linux'):
                subprocess.run(["xdotool", "key", self.base_key])
            elif sys.platform == 'win32':
                pyautogui.press(self.base_key)  # Simula la pulsación de una tecla en Windows
            else:
                self.keyboard.press(self.base_key)
                self.keyboard.release(self.base_key)
            time.sleep(self.interval)
