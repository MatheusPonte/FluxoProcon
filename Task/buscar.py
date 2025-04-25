from time import sleep

import keyboard as key
import pyautogui as pya
from selenium.webdriver.common.by import By
import time
from function.click_and_fill import click_and_fill
from function.imgfuction import searchimage
from function.webdriver import WebDriverManager
from function.logger import log

def buscar():
   searchimage('aceitar', 'aceitar encontrado', 'aceitar não encontrado')
   sleep(1)
   searchimage('calendario', 'calendrio encontrado', 'calendario não encontrado')
   sleep(1)
   searchimage('calendario2', 'calendrio encontrado', 'calendario não encontrado')
   sleep(1)
   searchimage('avancar', 'avancar encontrado', 'avancar não encontrado')
   searchimage('tipo', 'tipo encontrado', 'tipo não encontrado')
   sleep(1)
   key.write('PROCON TRIBANCO')
   sleep(1)
   searchimage('procontribanco', 'procontribanco encontrado', 'procontribanco não encontrado')
   sleep(1)
   click_and_fill('clique', 'caminho do clique encontrado', 'caminho do clique não encontrado')
   sleep(1)
   #searchimage('subtipo', 'subtipo encontrado', 'subtipo não encontrado')
   #sleep(1)
   #key.write('DEFESA PROCON (Atrasada)')
   #searchimage('defesaprocon', 'defesaprocon encontrado', 'defesaprocon não encontrado')
   #sleep(1)
   searchimage('compromisso', 'clicando em compromisso', 'compromisso não encontrado')
   searchimage('pendente', 'pendente encontrado', 'pendente não encontrado')
   sleep(3)
   click_and_fill('data1','data1 clicado','data não encontrado')
   sleep(1)
   pya.hotkey('ctrl', 'a')
   sleep(1)
   pya.press("backspace", presses=9)
   sleep(1)
   click_and_fill('clique', 'caminho do clique encontrado', 'caminho do clique não encontrado')
   sleep(1)
   click_and_fill('data2','data2 clicado', 'data não encotrada')
   sleep(1)
   pya.hotkey('ctrl', 'a')
   sleep(1)
   pya.press("backspace", presses=9)



