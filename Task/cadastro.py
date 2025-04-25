from time import sleep

import pyautogui as pya
import pyperclip
import keyboard as key
import re

from function.click_and_fill import click_and_fill
from function.imgfuction import searchimage, search_image_time
from function.read_dataframe import copiar, copiar2, data_util_em_tres_dias, pegar_data_do_clipboard_ou_util
from function.logger import log


class NenhumCompromissoEncontrado(Exception):
    pass


def copiar_com_requisicao(texto_original: str):
    padrao = r"\(ATRASAD[OA]\)"
    novo_texto = re.sub(padrao, "(COM REQUISIÇÃO)", texto_original, flags=re.IGNORECASE)

    pyperclip.copy(novo_texto)
    log.success(f"🔁 Texto modificado copiado: {novo_texto}")
    return novo_texto


def cadastrar(row):
    log.info('Buscando Titulo: ' + row['Nome da Requisição'])
    sleep(2)
    click_and_fill('pesquisar', 'pesquisar clicado', 'pesquisar não encontrado')
    sleep(1)
    pya.hotkey('ctrl', 'a')
    sleep(1)
    pya.press("backspace", presses=9)
    sleep(2)
    key.write(row['Nome da Requisição'])
    sleep(2)
    pya.hotkey('enter')
    sleep(5)
    pya.scroll(-800)
    sleep(2)

    if search_image_time('nenhum', 'nenhum encontrado', 'nenhum não encontrado!'):
        pya.scroll(800)
        log.warning('Nenhum compromisso encontrado. Pulando...')
        raise NenhumCompromissoEncontrado()

    print('proximo if:')

    if search_image_time('atrasada', 'atrasada encontrado', 'atrasada não encontrado!') or search_image_time('atrasado', 'atrasado encontrado', 'atrasado não encontrado!') or search_image_time('atrasadoprocon',' atrasado procon encontrado', ' atrasado procon nao encontrado'):
        sleep(1)
        searchimage('3pontos','3pontos clicados', '3pontos não encontrado')
        sleep(1)
        searchimage('editar','editar clicados', 'editar não encontrado')
        sleep(6)
        #clica onde tem a data
        click_and_fill('adiantar','adiantando data', 'data adiantada não encontrada')
        sleep(1)
        pya.hotkey('ctrl', 'a')
        sleep(1)
        #aqui ele copia a data:
        pya.hotkey('ctrl', 'c')
        sleep(1)
        pya.press("backspace", presses=9)
        sleep(1)
        #aqui é pra ele aplicar data de acordo com a função
        nova_data = pegar_data_do_clipboard_ou_util()
        click_and_fill("adiantar", "adiantar data", "Campo de data não encontrado", nova_data)
        sleep(7)
        click_and_fill('trocar', 'trocando nome de atrasado para requisição', 'atrasado nao encontrado')
        sleep(1)

        pya.hotkey('ctrl', 'a')
        sleep(0.5)
        pya.hotkey('ctrl', 'c')
        sleep(0.5)
        texto_original = pyperclip.paste()
        novo_texto = copiar_com_requisicao(texto_original)
        pya.press("backspace", presses=9)
        key.write(novo_texto)

        sleep(8)
        if search_image_time('vencido',' vencido encontrado','vencido não encontrado') or search_image_time('prazo','prazo encontrado', 'prazo nao encontrado'):
            sleep(3)
            searchimage('subatrasado','subatrasado encontrado','subatrasado não encontrado')
        sleep(1)
        searchimage('salvar','salvar encontrado','salvar não encontrado')
        print('indo para o proximo nome')
        sleep(5)
        pya.scroll(800)
    else:
        log.info('Indo para o proximo nome:')
        pya.scroll(800)
        raise NenhumCompromissoEncontrado()




