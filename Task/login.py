import pyautogui as pya
from selenium.webdriver.common.by import By
import time
from function.click_and_fill import click_and_fill
from function.imgfuction import searchimage
from function.webdriver import WebDriverManager
from function.logger import log

def logar(site, login, senh):
    driver_manager = WebDriverManager()
    browser = driver_manager.get_driver()
    browser.get(site)
    time.sleep(7)
    click_and_fill('cookie','caminho do cookie encontrado','caminho do cookie não encontrado')
    searchimage('login','Clicando no login', 'login não encontrado')
    log.success('Login colocado')
    pya.write(login, interval=0.1)
    time.sleep(2)
    searchimage('senha','Clicando no senha', 'senha não encontrado')
    pya.write(senh, interval=0.1)
    log.success('Senha colocada')
    time.sleep(1)
    searchimage('acessar','Clicando no acessar', 'acessar não encontrado')
    log.success('Logando!')
    time.sleep(3)
    #acessando calendario



