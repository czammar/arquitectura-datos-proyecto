#! /bin/bash
# Script para descargar pyenv y virtualenv, para crear ambiente donde se corre luigi

sudo apt update

# Instalamos librerias necesarias para pyenv y otras utilidades

sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev\
 libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev\
  xz-utils tk-dev libffi-dev liblzma-dev python-openssl git

cd ~

sudo apt-get install -y libpq-dev postgresql postgresql-contrib # Librerias para postgreSQL y psql

# Instalador de pyenv
sudo curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash

echo '********* Iniciamos modificacion del bashrc ************'
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bashrc
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
echo '********* Final de modificacion del bashrc +************'
