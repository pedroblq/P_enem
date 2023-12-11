import pandas as pd

def calcular_media_coluna(MICRODADOS_ENEM_2022, TP_ESTADO_CIVIL):
    # Lê o arquivo CSV
    dados = pd.read_csv(MICRODADOS_ENEM_2022, encoding="ISO-8859-1", low_memory=False, sep=';', iterator=True, chunksize=500000)
        
    # Calcula a média da coluna
    media_coluna = dados[TP_ESTADO_CIVIL].mean()
    
    print(f'Média da coluna {nome_coluna_desejada}: {resultado_media}')

    return media_coluna