def exportar_titulos_para_excel():
    import imaplib
    import email
    import re
    import os
    import pandas as pd
    from email.header import decode_header
    from function.config import load_environment
    from imapclient import imap_utf7
    from function.logger import log


    load_environment()

    usuario = os.getenv('EMAIL')
    senha = os.getenv('PASS')

    # Verifica se já existe planilha antiga
    nomes_existentes = set()
    arquivo_excel = "requisicoes_extraidas.xlsx"

    if os.path.exists(arquivo_excel):
        df_existente = pd.read_excel(arquivo_excel, dtype=str)
        if 'Nome da Requisição' in df_existente.columns:
            nomes_existentes = set(df_existente['Nome da Requisição'].dropna().str.strip())

    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(usuario, senha)

    mail.select('"requisi&AOcA9Q-es executadas"')

    print(imap_utf7.encode("requisições executadas").decode())

    status, mensagens = mail.search(None, 'ALL')
    ids = mensagens[0].split()
    titulos = []

    for num in ids:
        status, dados = mail.fetch(num, '(BODY.PEEK[])')  # não marca como lido
        raw_email = dados[0][1]
        msg = email.message_from_bytes(raw_email)

        assunto = decode_header(msg["Subject"])[0][0]
        if isinstance(assunto, bytes):
            assunto = assunto.decode()

        corpo = ""

        if msg.is_multipart():
            for part in msg.walk():
                content_type = part.get_content_type()
                if content_type in ["text/plain", "text/html"]:
                    try:
                        corpo = part.get_payload(decode=True).decode(errors='ignore')
                        if corpo:
                            break
                    except:
                        continue
        else:
            try:
                corpo = msg.get_payload(decode=True).decode(errors='ignore')
            except:
                corpo = ""

        # Extrair título
        match = re.search(r'T[íi]tulo:\s*(.+?)\s*-\s*\d{3}\.\d{3}\.\d{3}-\d{2}', corpo)
        if match:
            nome_requisicao = match.group(1).strip()
        else:
            nome_requisicao = 'Título não encontrado'

        # Extrair fase
        fase_match = re.search(r'Fase:\s*(\w+)', corpo, re.IGNORECASE)

        if fase_match:
            fase = fase_match.group(1).strip()
        else:
            fase = 'Fase não encontrada'

        # Evita duplicado
        if nome_requisicao in nomes_existentes:
            print(f"Pulado (já extraído): {nome_requisicao}")
            continue

        # Adiciona novo
        titulos.append({
            'Assunto': assunto,
            'Nome da Requisição': nome_requisicao,
            'Fase': fase
        })


        log.info(f"📥 Nova requisição adicionada: {nome_requisicao} | Fase: {fase}")

    mail.logout()

    df = pd.DataFrame(titulos)
    df.to_excel("requisicoes_extraidas.xlsx", index=False)
    return "requisicoes_extraidas.xlsx"
