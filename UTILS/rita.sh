#! /bin/bash
# Script para descargar pyenv y virtualenv, para crear ambiente donde se corre luigi

## Instrucciones:
# apt-get update && apt-get install nano
# nano rita.sh # Copia el contenido de este file y salvalo (ctrl +v, ctrl +o, crtl +x)
# chmod +x rita.sh # Permisos de ejecucion
# bash rita.sh
# Nota: en cierta para de la compilacion hay que introducir datos de zona horaria
# en un menu interactivo, dar 2 y luego 97

# Despues de correrlo, en la terminal correr
# source ~/.bashrc

sudo apt update
#sudo apt update
# Instalamos librerias necesarias para pyenv y otras utilidades

sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev\
 libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev\
  xz-utils tk-dev libffi-dev liblzma-dev python-openssl git
#sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev\
 #libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev\
  #xz-utils tk-dev libffi-dev liblzma-dev python-openssl git
cd ~

sudo apt-get install -y  libpq-dev


sudo curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash

echo '********* Iniciamos modificacion del bashrc ************'
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
#source ~/.bashrc
#echo 'eval "$(pyenv init -)"' >> ~/.bashrc
#echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc

echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bashrc
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
#source ~/.bashrc
#source ~/.bashrc
#exec "$SHELL"
#echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
#source ~/.bashrc
#exec "$SHELL"

echo '********* Final de modificacion del bashrc +************'
