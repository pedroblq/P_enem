import pandas as pd

d_parts = pd.read_csv("MICRODADOS_ENEM_2022.csv", encoding = "ISO-8859-1", low_memory=False, sep = ';', iterator = True, chunksize = 1000000)

for parts in d_parts:
    parts.drop(columns = ['Q001','Q002','Q003','Q004','Q005','Q007','Q008','Q009','Q010','Q011','Q012','Q013','Q014','Q015','Q016','Q017','Q018','Q019','Q020','Q021','Q022','Q023','Q024','TP_ESTADO_CIVIL','TP_NACIONALIDADE','CO_MUNICIPIO_ESC','CO_UF_ESC','CO_MUNICIPIO_PROVA','NO_MUNICIPIO_PROVA','CO_UF_PROVA','SG_UF_PROVA','CO_PROVA_CN','CO_PROVA_CH','CO_PROVA_LC','CO_PROVA_MT','TX_RESPOSTAS_CN','TX_RESPOSTAS_CH','TX_RESPOSTAS_LC','TX_RESPOSTAS_MT','TX_GABARITO_CN','TX_GABARITO_CH','TX_GABARITO_LC','TX_GABARITO_MT'], inplace = True)
    print(parts)