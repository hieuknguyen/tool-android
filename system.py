'''
67 = xoa
66 = enter
tap = click
toa do{555, 507}
'''
#adb -s devices shell input [tap, text, keyevent,...] content

import os
import time
import threading
def read_credentials(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            credentials = [line.strip().split('|') for line in lines if '|' in line]
            return credentials
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
        return []
    except ValueError:
        print("Some lines do not contain the expected format 'user|password'.")
        return []
# os.system('adb -s emulator-5554 shell input tap 555 507')
# os.system('adb -s emulator-5554 shell input tap 555 507')
# os.system('adb -s emulator-5554 shell input keyevent 67')
# os.system('adb -s emulator-5554 shell input keyevent 22')
file_path = '/Users/nguye/Downloads/a/bom.txt'
credentials_list = read_credentials(file_path)
def run_adb_command(device_id, text):
    os.system(f'adb -s {device_id} shell input text {text}')
def tap(devices, x ,y):
    os.system(f'adb -s {devices} shell input tap {x} {y}')
id = 5554
index = 1
threads = []
for line_number in range(len(credentials_list)):
    if line_number < index:
        user, password = credentials_list[line_number]
        devices = 'emulator-' + str(id)
        tap(devices, 733,456)
        time.sleep(1)
        tap(devices, 500, 400)
        tap(devices, 500, 400)
        run_adb_command(devices,user)
        time.sleep(1)
        tap(devices, 500, 460)
        tap(devices, 500, 460)
        run_adb_command(devices, password)
        tap(devices, 700, 555)
        # threading.Thread(target=tap, args=(733, 456)).start()
        
        # threading.Thread(target=tap, args=(500, 400)).start()
        # threading.Thread(target=tap, args=(500, 400)).start()
        # thread = threading.Thread(target=run_adb_command, args=(f'emulator-{str(id)}', user ,password))
        # threads.append(thread)
        # thread.start()
        # for thread in threads:
        #     thread.join()
        # threads.clear()
        
        # threading.Thread(target=tap, args=(700, 555)).start()
        id += 2
        
    else:
        break
