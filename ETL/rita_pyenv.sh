# Script para descargar pyenv y virtualenv, para crear ambiente donde se corre luigi

sudo apt update
sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python-openssl git

# Instalamos pyenv y configuramos el .bashrc
# .bashrc es el archivo para debian/ubuntu, se deberia adaptar
#  por .bash_profile o .zshrc en caso de usar zsh/oh-my-zsh

git clone https://github.com/pyenv/pyenv.git ~/.pyenv
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bashrc
nano /etc/ssh/sshd_config
exec "$SHELL"
bash

# Instalamos Python 3.7.3
pyenv install 3.7.3


# Instalamos pyenv virtualenv y configuramos el .bashrc

# Descargamos virtualenv
git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv
exec "$SHELL"

# Creamos ambiente virtual rita
pyenv virtualenv 3.7.3 rita
echo "rita" > .python-version # aparece (rita) a lado de la terminal
# pyenv activate rita # En caso que no apareza

# Instalamos paquetes necesarios para Luigi
pip install pandas luigi boto3 wget pyarrow requests 
