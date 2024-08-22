from ppadb.client import Client
import threading
#581 210
adb = Client(host="127.0.0.1", port=5037)

devices = adb.devices();
def test(i):
    print(devices[i].serial, '\n')
    devices[i].shell('input tap 581 210')

threads = []
for i in range(len(devices)):
    t1 = threading.Thread(target=test,args=(i,))
    
    threads.append(t1)
    t1.start()
for t in threads:
    t.join()