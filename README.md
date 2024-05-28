# Implementación de ETL

## Requisitos de PC
- Procesador: Core i5 o superior  
- RAM: 8GB o más
- Windows 10 o superior

## Pre-requisitos
- [Instalar Docker Desktop](https://docs.docker.com/get-docker/)
- [Instalar Visual Studio Code](https://code.visualstudio.com/download)  

## Instalacion de Apache Airflow
1. Abrir la terminal. **Visual Studio Code -> Terminal -> Nueva Terminal**
2. En la terminal ejecutar el siguiente comando: **` docker-compose up -d `**
3. Esperar entre 2 a 5 minutos.
4. Abre tu navegador y dirigite a http://localhost:8080/
    - `Usuario:` airflow
    - `Clave:` airflow

## Eliminar Docker container, images y volumes
Ejecutar los siguientes comandos en orden:
1. Para eliminar docker containers: **` docker-compose down `**
2. Para eliminar docker volumes: **` docker volume prune `**
3. Para eliminar docker images: **` docker rmi -f $(docker images -aq) `**
