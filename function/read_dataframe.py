from logging import exception
import pandas as pd
import pyperclip
from tkinter import filedialog
from function.logger import log
from datetime import datetime, timedelta


from tkinter import filedialog, Tk

def ler_arquivo():
    root = Tk()
    root.withdraw()
    root.call('wm', 'attributes', '.', '-topmost', True)
    caminho = filedialog.askopenfilename(
        title="Selecione o arquivo BASE DE DEVEDORES",
        filetypes=[("Arquivos Excel", "*.xlsx *.xls")]
    )
    root.destroy()
    return caminho



def copiar(valor: str, date: bool = False, time: bool = False):
    try:
        if date and not time:
            valor = pd.to_datetime(valor, format='%d/%m/%Y', errors='coerce')
            if pd.notnull(valor) and valor.year > 1900:  # Ignorar anos inválidos
                valor = valor.strftime('%d/%m/%Y')  # ✅ Formata corretamente
            else:
                log.error('Data inválida')
                return None

        if time and not date:
            valor = pd.to_datetime(valor, format='%H:%M:%S', errors='coerce')
            if pd.notnull(valor):
                valor = valor.strftime('%H:%M:%S')  # ✅ Formata corretamente
            else:
                log.error('Hora inválida')
                return None

        if pd.notnull(valor):
            valor_final = str(valor)
            pyperclip.copy(valor_final)
            log.success(f'Valor Copiado: {valor_final}')
            return valor_final
        else:
            log.error('Erro ao processar o valor.')
            return None

    except Exception as e:
        log.error(f'Erro: {e}')
        return None

def copiar2(valor):
    try:
        if isinstance(valor, pd.Timestamp):
            valor = valor.strftime('%d/%m/%Y')

        elif isinstance(valor, str):
            valor = pd.to_datetime(valor, errors='coerce')
            if pd.notnull(valor):
                valor = valor.strftime('%d/%m/%Y')

        if pd.notnull(valor):
            pyperclip.copy(valor)
            log.success('Valor Copiado!')
            return valor
        else:
            log.warning('Valor é nulo, nada copiado.')
            return None

    except Exception as e:
        log.error(f"Erro ao copiar valor: {e}")
        return None



from datetime import datetime, timedelta
import pyperclip
from function.logger import log


from datetime import datetime, timedelta
import pyperclip
from function.logger import log

# Mapeamento de abreviações PT-BR para EN-US
MESES_PT_EN = {
    'jan': 'Jan', 'fev': 'Feb', 'mar': 'Mar', 'abr': 'Apr',
    'mai': 'May', 'jun': 'Jun', 'jul': 'Jul', 'ago': 'Aug',
    'set': 'Sep', 'out': 'Oct', 'nov': 'Nov', 'dez': 'Dec'
}

def data_util_em_tres_dias():
    data = datetime.now() + timedelta(days=3)
    if data.weekday() == 5:
        data += timedelta(days=2)
    elif data.weekday() == 6:
        data += timedelta(days=1)
    return data.strftime("%d/%m/%Y")


def adicionar_dias_uteis(data, dias_uteis):
    dias_adicionados = 0
    while dias_adicionados < dias_uteis:
        data += timedelta(days=1)
        if data.weekday() < 5:  # 0 a 4 = segunda a sexta
            dias_adicionados += 1
    return data


def pegar_data_do_clipboard_ou_util():
    texto = pyperclip.paste().strip().lower()

    try:
        # Converte "abr" para "Apr"
        for pt, en in MESES_PT_EN.items():
            if f" {pt} " in texto:
                texto = texto.replace(f" {pt} ", f" {en} ")
                break

        data = datetime.strptime(texto, "%d %b %Y")  # agora sim
        data_final = adicionar_dias_uteis(data, 3)
        data_formatada = data_final.strftime("%d/%m/%Y")
        log.success(f"📋 Data ajustada com +3 dias úteis: {data_formatada}")
        return data_formatada

    except Exception:
        log.warning("⚠️ Data do clipboard inválida ou não reconhecida, usando data atual +3 dias úteis.")
        return data_util_em_tres_dias()


