#! /bin/bash

# Creamos ambiente virtual rita
cd ~
pyenv install 3.7.3 # Instala esta version de Python (se puede modificar)
pyenv virtualenv 3.7.3 rita # Crea ambiente virtual "rita" con la version de Python previa

git clone https://github.com/czammar/arquitectura-datos-proyecto
cd arquitectura-datos-proyecto/ETL
echo "rita" > .python-version # aparece (rita) a lado de la terminal

#pyenv activate rita # activa el ambiente virtual "rita"
pip3 install pandas luigi boto3 wget pyarrow requests Psycopg2 datetime publicip
