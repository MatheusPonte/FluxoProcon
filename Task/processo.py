from Task.cadastro import cadastrar
from function.logger import log
from Task.cadastro import NenhumCompromissoEncontrado
from pathlib import Path
import winsound
import pandas as pd

def etapa_processo(df, df_path):
    log.info(f"📄 df_path recebido: {df_path}")

    if 'status' not in df.columns:
        df['status'] = ''
    else:
        df['status'] = df['status'].fillna('')

    for index, row in df.iterrows():
        if str(row.get('status')).strip().lower() == 'concluído':
            continue

        log.info(f"Iniciando processamento da requisição: {row['Nome da Requisição']}")

        try:
            cadastrar(row)
            df.at[index, 'status'] = 'concluído'
            log.success(f"Requisição {row['Nome da Requisição']} concluída!")

        except NenhumCompromissoEncontrado:
            df.at[index, 'status'] = 'ignorado'
            log.info(f"Requisição {row['Nome da Requisição']} ignorada (nenhum compromisso encontrado).")

        except Exception as e:
            df.at[index, 'status'] = 'erro'
            log.warning(f"Erro na requisição {row['Nome da Requisição']}: {e}")

        # Salva a cada linha processada
        if df_path:
            try:
                with pd.ExcelWriter(df_path, engine="openpyxl", mode="w") as writer:
                    df.to_excel(writer, index=False)
                log.success(f"💾 Planilha atualizada: {df_path}")
            except Exception as e:
                log.critical(f"❌ Erro ao salvar planilha: {e}")
        else:
            log.warning("⚠️ df_path vazio, não salvou a planilha.")

    # 🔊 Som personalizado após tudo
    try:
        som_path = Path(__file__).resolve().parent.parent / "sounds" / "acabou.wav"
        winsound.PlaySound(str(som_path), winsound.SND_FILENAME)
        log.info("🔊 Som de conclusão personalizado tocado!")
    except Exception as e:
        log.warning(f"⚠️ Falha ao tocar som: {e}")
