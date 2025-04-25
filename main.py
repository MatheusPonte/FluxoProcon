import flet as ft
from Task.processo import etapa_processo
from end import endpoints
import os
import pandas as pd
from Task.login import logar
from function.logger import log
from function.config import load_environment
from function.gmail_reader import exportar_titulos_para_excel
from Task.buscar import buscar
from function.read_dataframe import ler_arquivo


load_environment()
url = endpoints['TRI']

import sys
from pathlib import Path


if getattr(sys, 'frozen', False):
    base_path = Path(sys._MEIPASS)
else:
    base_path = Path(__file__).parent


img_path = base_path / "img"

def main(page: ft.Page):
    page.title = "Automação do Robertinho"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    log.info('Automação iniciada')

    df = None
    df_path = None

    planilha_path = "requisicoes_extraidas.xlsx"


    usuario_dropdown = ft.Dropdown(
        label="Usuário",
        width=300,
        options=[ft.dropdown.Option("Robertinho")]
    )

    def extrair_titulos_do_gmail(e):
        nonlocal df, df_path
        try:
            log.info("Extraindo e-mails do Gmail...")
            caminho = exportar_titulos_para_excel()
            df = pd.read_excel(caminho, dtype=str)
            df_path = caminho
            page.add(ft.Text("✅ Planilha gerada a partir do Gmail com sucesso!", size=20, color=ft.colors.GREEN))
            log.success(f"Planilha gerada: {caminho}")
        except Exception as ex:
            import traceback
            traceback.print_exc()
            page.add(ft.Text("❌ Erro ao extrair dados do Gmail!", size=20, color=ft.colors.RED))
            log.warning(f"Erro ao gerar planilha do Gmail: {ex}")

    def importar(e):
        nonlocal df, df_path
        try:
            file_path = ler_arquivo()
            df_path = file_path
            df = pd.read_excel(file_path, dtype=str)
            log.success('Planilha carregada com sucesso.')
            page.add(ft.Text("📄 Planilha carregada!", size=20, color=ft.colors.GREEN))
        except Exception as ex:
            log.warning('Erro ao carregar planilha.')
            page.add(ft.Text("❌ Erro ao carregar planilha", size=20, color=ft.colors.RED))

    def iniciar_automacao(e):
        nonlocal df
        usern = ""
        passw = ""

        if usuario_dropdown.value == "Robertinho":
            usern = os.getenv("USERN")
            passw = os.getenv("SENHA")

        if not usern or not passw:
            log.warning("Usuário ou senha não definidos!")
            page.add(ft.Text("❌ Usuário não encontrado!", size=20, color=ft.colors.RED))
            return

        if df is None:
            log.info('Nenhuma Planilha foi carregada!')
            page.add(ft.Text('⚠️ Nenhuma Planilha foi carregada!', size=20, color=ft.colors.RED))
            return

        try:
            logar(url, usern, passw)
            buscar()
            etapa_processo(df, df_path)
            page.add(ft.Text(log.success('✅ Automação finalizada com sucesso!'), size=20, color=ft.colors.GREEN))
        except Exception as ex:
            page.add(ft.Text(log.critical('❌ Erro na automação'), size=20, color=ft.colors.RED))

    def sair(e):
        log.info("Automação fechada")
        os._exit(0)


    background = ft.Container(
        image_src=str(img_path / "fundo.jpg"),
        image_fit=ft.ImageFit.COVER,
        expand=True,
        content=ft.Row(
            [
                ft.Container(
                    bgcolor=ft.colors.with_opacity(0.1, ft.colors.BLACK),
                    border_radius=20,
                    padding=30,
                    content=ft.Column(
                        [
                            ft.Text("Bem-vindo à Automação do Robertinho", size=30, weight="bold", font_family="Arial Black", color=ft.colors.WHITE),
                            usuario_dropdown,
                            ft.ElevatedButton("Extrair do Gmail", on_click=extrair_titulos_do_gmail),
                            ft.ElevatedButton("Carregar Planilha", on_click=importar),
                            ft.ElevatedButton("Iniciar Automação", on_click=iniciar_automacao),
                            ft.ElevatedButton("Sair", on_click=sair),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

    page.add(background)

ft.app(target=main)
