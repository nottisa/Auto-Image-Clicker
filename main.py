#Written by bobthedeveloper90368
timetowait = 0.5 #Time to wait in beetween each button click (In Seconds)

###IMPORTS###
#import pyautogui

def locatenextbutton():
    try:
        location = pyautogui.locateOnScreen('./images/Nextbutton.png', confidence=0.9)
    except:
        return False, False
    else: 
        return pyautogui.center(location)[0], pyautogui.center(location)[1]

def locateselectiondot():
    try:
        location = pyautogui.locateOnScreen('./images/Selectiondot.png', confidence=0.9)
    except:
        return False, False
    else: 
        return pyautogui.center(location)[0], pyautogui.center(location)[1]


while True:
    pass
#im2 = pyautogui.screenshot('./my_screenshot.png')
#location = pyautogui.locateOnScreen('./images/Nextbutton')
#pyautogui.click('calc7key.png')