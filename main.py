#Written by bobthedeveloper90368; https://www.buymeacoffee.com/nottisa
timetowait = 0.5 #Time to wait in beetween each button click (In Seconds)

###IMPORTS###
import pyautogui, time

def locatenextbutton():
    t = pyautogui.locateCenterOnScreen("./images/Selectiondot.png", grayscale=True)
    if not t == None:
        x, y = t
        pyautogui.moveTo(x,y)
        pyautogui.click()

def locateselectiondot():
    t = pyautogui.locateCenterOnScreen("./images/Selectiondot.png", grayscale=True)
    if not t == None:
        x, y = t
        pyautogui.moveTo(x,y)
        pyautogui.click()


while True:
    locatenextbutton()
    time.sleep(timetowait)
    locateselectiondot()
    time.sleep(timetowait)