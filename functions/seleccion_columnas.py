import logging

def seleccion_columnas(ti, columnas):
    dataframe = ti.xcom_pull(key='dataframe', task_ids='EXTRAER')
    dataframe = dataframe[columnas]
    ti.xcom_push(key='dataframe', value=dataframe)
    logging.info("Selección de columnas realizada")
