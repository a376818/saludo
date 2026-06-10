# Saludo

Esta app envía un mensaje en terminal, mostrando el nombre de la computadora y la hora actual.

## Comenzando

Estas instrucciones le permitirán obtener una copia del proyecto corriendo en su máquina local para porpósitos de desarrollo y pruebas. Vea las notas de despliegue para desplegar el proyecto en un sistema en vivo.

### Prerequisitos

### `Python`

Descargue la versión adecuada para su dispositivo del [sitio web de Python](https://www.python.org/).\
Siga las instrucciones del instalador.

### `Pyinstaller`

En el directorio del proyecto, puede correr `pip install pyinstaller` para instalar el intérprete de Python.\
Esto permitirá crear el ejecutable.

### Instalación

Una vez que haya clonado el repositorio en su dispositivo, puede abrir `saludo.py` en cualquier IDE compatible con Python.

## Despliegue

En el directorio del proyecto, puede correr:

### `pyinstaller saludo.py`

Para crear el ejecutable.\
El archivo saludo.exe será creado en `\dist\saludo`.

### `docker build -t py-saludo .`

Para crear la imagen de Docker.\
Seguido de:

### `docker run -t -i py-saludo`

Para correr el programa en Docker con interactividad.

## Construido con

* [Python](https://www.python.org/doc/) - El lenguaje de programación utilizado.

## Versiones

La etiqueta de Docker para la versión actual es `v1.0.0`.\
Para cambios menores, cambiar el último dígito.

## Autores

* **Damaris Naomi Trujillo García** - *Trabajo inicial* - [a376818](https://github.com/a376818)