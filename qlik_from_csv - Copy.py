import settings as st
from pathlib import Path
import pandas as pd
import kpi_script as kpi_scr

import functions as ft

df_KPI_punt_file = Path(st.intermediate, st.definitivo, 'df_KPI_definitivo_puntuali_rett.csv')
ft.generate_qlik_input(df_KPI_punt_file, 'prova555.csv', calcola_bu_re=True)


'''
#================================================================================
#FUNZIONE PER CREARE IL FILE DI INPUT DELLA DASHBOARD A PARTIRE DA MERCATO FISSO
#=================================================================================
#devo dire quali colonne importare
column_list = [2018013, 2018023, 2018033, 2018043, 2018053, 2018063, 2018073, 2018083, 2018093, 2018103]
ft.qlik_data_from_excel("Mercato Fisso 2018.xlsx", column_list, 'qlik.csv')
'''


'''

#================================================
#--GENERAZIONE DATA SOURCE KPI PROGRESSIVI QLIK
#===============================================
#leggo il dataframe
#df_KPI_prog = pd.read_csv(Path(st.intermediate,st.definitivo, st.KPI_progressivi_def + '.csv'))
df_KPI_prog = pd.read_csv(Path(st.intermediate,st.definitivo,'OTT_2018','DECADE_3', 'df_KPI_punt_report' + '.csv'))
df_KPI_prog.set_index('KPI_ID', inplace=True)

#creo un dizionario per i KPI
KPI_prog = list()

#itero nel dataframe per costruire il dizionario KPI
for col in df_KPI_prog:
    anno = str(col[:4])
    mese = str(col[4:6])
    decade = str(col[6])
    df_KPI_dict = df_KPI_prog[col].to_dict()
    dict_bu = kpi_scr.calcola_business(df_KPI_dict)
    dict_tot = {}
    dict_tot.update(df_KPI_dict)
    dict_tot.update(dict_bu)
    for index, row_value in dict_tot.items():
        #print('colonna: ' + str(col) + ' riga: ' + str(index) + ' valore: ' + str(row_value) )
        KPI_list = list()
        kpi = str(index)
        kpi_id = str(index.split('_')[1])
        kpi_seg = str(index.split('_')[0])
        value = row_value
        KPI_list=[kpi, kpi_id, kpi_seg, anno, mese, decade, value]
        KPI_prog.append(KPI_list)
header = ['kpi', 'kpi_id', 'kpi_seg','anno','mese','decade','valore']

df_qlik_prog = pd.DataFrame.from_records(KPI_prog, columns=header)

df_qlik_prog.to_csv(Path(st.intermediate,st.definitivo, st.df_qlik_puntuali_name + '.csv'), sep=',', index=False)

'''


