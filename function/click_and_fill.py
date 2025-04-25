import logging

import pyautogui as pya
from time import sleep
from function.imgPath import POSITION
from function.logger import log


def click_and_fill(position_name, description: object, exe: object, value: str = None, delay_before: float = 0, delay_after: float = 0.75,
                   command: str = 'click', interval: float = 0, num_clicks: int = 1):
    try:

        x, y = POSITION[position_name]

        if delay_before > 0:
            sleep(delay_before)

        action_function = getattr(pya, command)
        log.success(description)

        if command == 'doubleClick':
            action_function(x, y)
        else:
            action_function(x, y, num_clicks, interval)

        if value is not None:
            sleep(0.5)
            pya.write(value)
            sleep(1)

        if delay_after > 0:
            sleep(delay_after)

    except Exception as e:
        log.warning(exe)

