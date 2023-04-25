#Written by bobthedeveloper90368; https://www.buymeacoffee.com/nottisa
timetowait = 0.5 #Time to wait in beetween each button click (In Seconds)

###IMPORTS###
import pyautogui, time

def locatenextbutton():
    try:
        pyautogui.click('./images/Nextbutton.png')
    except:
        return False
    else:
        return True

def locateselectiondot():
    try:
        pyautogui.click('./images/Selectiondot.png')
    except:
        return False
    else: 
        return True


while True:
    print(locatenextbutton())
    time.sleep(timetowait)
    print(locateselectiondot())
    time.sleep(timetowait)