# cap man hinh sau 2s gui ve may tinh de xu ly
#print creen = exec-out screencap

import os
import time

class Tool:
    def __init__(self, device):
        self.device = device

    def screen(self):
        os.system(f"adb -s {self.device} exec-out screencap -p > ./pic/{self.device}.png")


p1 =Tool("emulator-5554")

while True:
    p1.screen()
    time.sleep(2)
