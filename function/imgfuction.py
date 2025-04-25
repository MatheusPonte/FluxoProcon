from logging import exception
import pyautogui as pya
import time
from function.imgPath import IMG
from function.logger import log



def searchimage(image_alias: object, description: object, excep: object) -> object:
    while True:
        try:
            image_dimension = pya.locateOnScreen(IMG[image_alias], confidence=0.9, grayscale=True)
            if image_dimension:
                pya.click(image_dimension)
                log.success(description)
                break

        except:
            log.warning(excep)
            time.sleep(0.5)

def search_image_time(image_alias: object, description: object,excep: object):
    for i in range(5):
        try:
            image_dimension = pya.locateOnScreen(IMG[image_alias], confidence=0.9)
            if image_dimension:
                pya.click(image_dimension)
                log.success(description)
                return True

        except Exception:
            log.warning(excep)
            i += 1

