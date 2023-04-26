#Written by bobthedeveloper90368; https://www.buymeacoffee.com/nottisa
###IMPORTS###
import pyautogui

def clickimage(toclick):
    t = pyautogui.locateCenterOnScreen(toclick, grayscale=True)
    if not t == None:
        x, y = t
        pyautogui.moveTo(x,y)
        pyautogui.click()



while True:
    #To add an image simply pass in the image path via the function below. Copy the function below to click another image.
    clickimage("./test.png")
