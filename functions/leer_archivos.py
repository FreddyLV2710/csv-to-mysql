import pandas as pd
import logging

def leer_archivos(ti, ruta_archivo):
    dataframe = pd.read_csv(ruta_archivo, sep=';')
    ti.xcom_push(key='dataframe', value=dataframe)
    logging.info("Archivo leído con éxito", dataframe.columns)
