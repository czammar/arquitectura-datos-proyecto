FROM ubuntu:bionic

RUN apt-get update && export DEBIAN_FRONTEND=noninteractive && echo "America/Mexico_City" > /etc/timezone && apt-get install -y tzdata

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

RUN apt-get update && apt-get install -y \
            sudo \
            nano \
            python3-dev \
            python3-pip \
            python3-setuptools \
            libpq-dev && pip3 install --upgrade pip  && pip3 install awscli --upgrade

# Creamos al usuario rita
RUN groupadd rita
RUN useradd rita -g rita -m -s /bin/bash
RUN echo 'rita ALL=(ALL:ALL) NOPASSWD:ALL' | (EDITOR='tee -a' visudo)
RUN echo 'rita:rita' | chpasswd

# Instalamos paquetes necesarios para el proyecto
RUN pip3 install pandas luigi boto3 wget pyarrow requests Psycopg2 datetime

# Instala diferentes librerias para al proyecto
USER rita
WORKDIR /home/rita/
