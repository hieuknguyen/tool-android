from ppadb.client import Client
import threading
import cv2
import numpy as np

adb = Client(host="127.0.0.1", port=5037)

devices = adb.devices();
class Tool:
    def __init__(sefl,total):
        sefl.total = total
    def test(self):
        print(devices[self.total].serial, '\n')
        devices[self.total].shell('input tap 581 210')
        
    def screen(self):
        device = devices[self.total].serial

        devices[self.total].shell(f'screencap -p /sdcard/{device}.png')
        
        devices[self.total].pull(f'/sdcard/{device}.png', f'./pic/{device}.png')
        
        devices[self.total].shell(f'rm /sdcard/{device}.png')
        print(device)
        
    def check(self):
        device = devices[self.total].serial  
    
        path = fr'C:/Users/nguye/Downloads/a/pic/{device}.png'
    
    
        path1 = r'C:/Users/nguye/Downloads/a/a.png'
        img = cv2.imread(path)
        img1 = cv2.imread(path1)

        result = cv2.matchTemplate(img, img1, cv2.TM_CCOEFF_NORMED)


        threshold = 0.9
        loc = np.where(result >= threshold)


        if len(loc[0]) > 0:
            print("true")
        else:
            print("false")
threads = []

for i in range(len(devices)):
    p1 = Tool(i)
    t1 = threading.Thread(target=p1.screen)
    threads.append(t1)
    t1.start()
    
for t in threads:
    t.join()
