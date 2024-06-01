import logging

def filtrar_columnas(ti, valor):
    dataframe = ti.xcom_pull(key='dataframe', task_ids='TRANSFORMACION.seleccion')
    final = dataframe[dataframe['Ingresos'] > valor]
    ti.xcom_push(key='final', value=final)
    logging.info("Filtrado de columnas realizado")
