# dnd.py
import time


class DoNotDisturb:
    def __init__(self, state, seconds):
        self.state = state
        self.seconds = seconds

    def get_seconds(self):
        return self.seconds

    def toggle(self):
        self.state = not self.state

    def set_led(self):
        print("LED is", self.state)


dnd = DoNotDisturb(True, 2)
while True:
    dnd.set_led()
    time.sleep(dnd.get_seconds())
    dnd.toggle()
