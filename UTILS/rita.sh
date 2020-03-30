# Script para descargar pyenv y virtualenv, para crear ambiente donde se corre luigi

## Instrucciones:
# apt-get update && apt-get install nano
# nano rita.sh # Copia el contenido de este file y salvalo (ctrl +v, ctrl +o, crtl +x)
# chmod +x rita.sh # Permisos de ejecucion
# bash rita.sh

# Despues de correrlo, en la terminal correr
# exec "$SHELL"
# pyenv activate rita # activa el ambiente virtual
# pip3 install nombre-paquete # instala paquete nombre-paquete que haga falta

apt update
#sudo apt update
# Instalamos librerias necesarias para pyenv y otras utilidades
apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python-openssl git
#sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python-openssl git
apt-get install -y  libpq-dev # libreria para instalar Pyscopg2
#sudo apt-get install -y  libpq-dev # libreria para instalar Pyscopg2

# Instalamos pyenv y configuramos el .bashrc
git clone https://github.com/pyenv/pyenv.git ~/.pyenv
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bashrc
#exec "$SHELL" # reinicia la consola

# Instalamos pyenv virtualenv y configuramos el .bashrc
git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
#exec "$SHELL" # reinicia la consola

# Creamos ambiente virtual rita
pyenv install 3.7.3 # Instala esta version de Python (se puede modificar)
pyenv virtualenv 3.7.3 rita # Crea ambiente virtual "rita" con la version de Python previa
echo "rita" > .python-version # aparece (rita) a lado de la terminal

pyenv activate rita # activa el ambiente virtual "rita"
pip3 install pandas luigi boto3 wget pyarrow requests Psycopg2 datetime
