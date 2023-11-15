# Universidad - Django App 
Este repositorio contiene una herramienta de software desarrollada en Django para gestión de facultades, programas y profesores de una universidad. 

### Instrucciones para Clonar y Configurar la App
Si usas Windows, se recomienda utilizar GitBash.
___
Primero debes clonar el proyecto desde el repositorio:
```bash
git clone git@github.com:SegundoPaladines/Universidad.git
```
Una vez clonado, debes ubicarte en la carpeta del proyecto:
```bash
cd universidad
```
Si aún no has instalado virtualenv, deberás instalarlo, asumiendo que tienes instalado Python y pip:
```bash
pip install virtualenv
```
Ahora debemos crear el entorno virtual a utilizar:
```bash
virtualenv env
```
Iniciamos el entorno virtual:

## Linux
```bash
source env/bin/activate
```
##  Windows
Si usas windows,  desde acá, mejor usar el powershell del vscode:
```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
```bash
env/Scripts/activate
```
___
## Una vez iniciado el entorno virtual, debes ejecutar los siguientes comandos, esto es independiente del sistema operativo que se use:
Primero, instalamos los requerimientos necesarios para que la aplicación pueda funcionar:
```bash
pip install -r requirements.txt
```
Revisar si las dependencias se instalaron correctamente (puedes revisar el archivo requirements.txt para verificar que todas las dependencias están correctamente instaladas):
```bash
pip freeze
```
Hacer las migraciones correspondientes a los modelos:
```bash
python manage.py makemigrations
```
Realizar la migración a la base de datos:
```bash
python manage.py migrate
```
Crear el usuario administrador para poder acceder al administrador del sistema:
```bash
python manage.py createsuperuser
```
Correr el servidor:
```bash
python manage.py runserver
```