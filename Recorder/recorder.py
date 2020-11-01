import tkinter as recorder
import cv2
import pyautogui
import numpy as np
import time



import win32gui
import win32con
from os import mkdir



try:
    mkdir("recording")
except FileExistsError:
    pass
def minimizeWindow():
    window = win32gui.FindWindow(None,"screen recorder")
    win32gui.ShowWindow(window,win32con.SW_MINIMIZE)
# display screen resolution
SCREEN_SIZE = (1366, 768)
# define the codec
fourcc = cv2.VideoWriter_fourcc(*"XVID")
# create the video write object
output = cv2.VideoWriter("recording/"+"ScreenRecording "+time.strftime("%H-%M-%S %d-%m-%y")+".mp4",
                         fourcc, 20.0, (SCREEN_SIZE))

print('Recording Started.... \nwindow minimized in taskbar.\npress q to exit')

minimized = False
while True:
    # make screenshot
    img = pyautogui.screenshot()
    frame = np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    cv2.imshow("screen recorder", frame)
    if minimized== True:
        pass
    else:
        minimized = True
        minimizeWindow()



    output.write(frame)
    if cv2.waitKey(1) == ord('q'):
        print('\rRecording Finished') 
        break

output.release()
cv2.destroyAllWindows()


























