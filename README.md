# Proyecto de investigación de simulación de nubes y estimaciones de CO2

Fork de [cloudSim](https://github.com/Cloudslab/cloudsim) y extensión de funcionalidades para generación de archivo **CSV** y script de procesamiento de datos para posterior análisis gráfico.
El repositorio contiene un paquete de replicación del experimento generado para la investigación desarrollada como proyecto final de la materia ***metodología de investigación***.
Se proporcionan todos los archivos y datos utilizados para la experimentación y las características del ambiente utilizado para la simulación.
# ABSTRACT

# Características del ambiente de pruebas

 1. IDE Eclipse 2020-03 (4.15.0) Build id: 20200313-1211.
 2. Deepin OS 20 Versión community 20.2.2 entorno de escritorio DDE y kernel 5.12.18-amd64-desktop.
 3.  Laptop Dell modelo Latitude E6420, 500 GB de SSD, 12GB RAM, 12GB de intercambio y procesador Core i7-2760QM de 2,40GHz.
 4. Workload 20110303 de planetLab.
# Archivos
El paquete de replicación esta compuesto por dos partes.

 1. [Script python](https://github.com/jquintanas/cloudsim/tree/main/script%20procesamiento%20data) para tratamiento de data.
 2. [Código fuente editado de cloudSim](https://github.com/jquintanas/cloudsim/tree/main/cloudsim) este paquete mantiene el código fuente de cloudSim con las configuraciones respectivas realizadas para la experimentación junto con los workloads que vienen para pruebas.

Tanto del script de procesamiento de datos como en cloudSim se recomiendan cambiar las rutas de entrada y salida de archivos, en el script se debe cambiar el **nombre del archivo de entrada y salida** a los generados por los replicadores y en cloudSim se debe cambiar en el archivo [powerDataCenter.java](https://github.com/jquintanas/cloudsim/blob/main/cloudsim-cloudsim-4.0/modules/cloudsim/src/main/java/org/cloudbus/cloudsim/power/PowerDatacenter.java)

## Instalación

 1. CloudSim
Dentro de la carpeta de cloudSim escribir los siguientes comandos.
```sh
mv clean
mv install
```
con esto se procedera a recrear el proyecto de cloudSim con las modificaciones creadas para la investigación. Se debe actualizar la ruta de salida de los archivos en el archivo [powerDataCenter.java](https://github.com/jquintanas/cloudsim/blob/main/cloudsim-cloudsim-4.0/modules/cloudsim/src/main/java/org/cloudbus/cloudsim/power/PowerDatacenter.java) como se observa a continuación.
![enter image description here](https://raw.githubusercontent.com/jquintanas/cloudsim/main/capturas/cloudSim.png)
 2. Script de procesamiento de data
Una vez configuradas las rutas de los archivos como se observa a continuación.
![enter image description here](https://raw.githubusercontent.com/jquintanas/cloudsim/main/capturas/python.png)
se debe ejecutar el siguiente comando para ejecutar el archivo
```sh
python nombreArchivo.py
```
## Procesar la data generada por el script python

Cuando ya se encuentre la data procesada, el script python generara un archivo con extensión CSV mismo que debera ser procesado con sistema de graficación de su preferencia.

## Tabla de resultados
A continuación se detallan los resultados de la presente investigación para que puedan ser comparados con investigaciones posteriores.

|Algoritmo|Consumo energético KWH|CO2 - Huella de carbono|CO2 - EEUU|CO2 - Ecuador|
|---------|----------------------|-----------------------|----------|-------------|
|DVFS     |776.72                |225.2488               |550.7     |379.82       |
|LR       |160.50                |46.55                  |113.8     |78.48        |
|IQR      |189.37                |54.9173                |134.26    |92.6         |


## Factores de conversión de KWH a CO2 tomados para la investigación.
Estos factores fueron tomados de estudios del 2019 y se trabajaron con los mismos para la estimación del consumo de CO2 de la simulación.
|País| valor en   kgCO2/kWh|
|--|--|
| Ecuador | 0.4509 |
| EEUU |  0.709|
| Huella de carbono |  0.29|

## Integrantes
| ![Karla Burgos perfil git](https://avatars.githubusercontent.com/u/43821172?v=4) | ![Jonathan Quintana perfil de git](https://avatars.githubusercontent.com/u/28455102?v=4) |
|--|--|
| [Karla Burgos](https://github.com/kbburgos) | [Jonathan Quintana](https://github.com/jquintanas) |

## Agradecimientos

# Licencia
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
