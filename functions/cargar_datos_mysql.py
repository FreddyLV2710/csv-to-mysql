from sqlalchemy import create_engine

def cargar_datos_mysql(ti, tabla_destino):
    dataframe = ti.xcom_pull(key='final', task_ids='TRANSFORMACION.filtrar')
    engine = create_engine("mysql+pymysql://root:dwh@mysql_dwh:3306/dwh")
    with engine.begin() as connection:
        dataframe.to_sql(name=tabla_destino, con=connection, if_exists='append', index=False)
