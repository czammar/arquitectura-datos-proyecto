## Instrucciones



## Desde la instancia de EC2 (Bastion):

**Script rita.sh**

Este script instala pyenv y pyenv-virtualenv para crear un ambiente virtual donde se correra luigi con el resto de paquetes que necesitaremos en el pipeline.

******

```bash
apt-get update && apt-get install wget
wget https://raw.githubusercontent.com/czammar/arquitectura-datos-proyecto/master/UTILS/rita.sh
chmod +x rita.sh # en caso de que necesite permisos de ejecucion
bash rita.sh # ejecutamos el script recien creado
source ~/.bashrc
```



**Nota:** en cierta para de la compilacion hay que introducir datos de zona horariae n un menu interactivo, dar 2 y luego 97

**Script rita2.sh**

Este script instala python 3.7.3 en pyenv, y crea un ambiente virtual llamda *rita*, concretamente instala todos los paquetes que usamos en el pipeline hasta ahora

**Nota:**Se asume que ya se corrio el primer script.

******

```bash
wget https://raw.githubusercontent.com/czammar/arquitectura-datos-proyecto/master/UTILS/rita2.sh
chmod +x rita2.sh # en caso de que necesite permisos de ejecucion
bash rita2.sh # ejecutamos el script recien creado
```



**Pasos siguientes:**

Ingresar a la carpeta del repositorio, dentro de la instancia, esto deberia activar por defecto el entorno virtual "rita" automaticamente. Debe aparece (rita) al lado izquierdo de la terminal.

```bash
cd ~/arquitectura-datos-proyecto/ETL #
```

Si algun paquete falta, basta user el siguiente comando dentro de este ambiente virtual o investigar en internet

```bash
pip3 install nombre_paquete
```

**Nota:** En caso de que el amnbiente virtual no se active solo, estas son las instrucciones para activar a desactivar el ambiente de manera manual

```bash
pyenv activate rita # activa el ambiente virtual rita
pyenv deactivate rita # desactiva el ambiente virtual rita
```

