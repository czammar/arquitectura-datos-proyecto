#Download base image ubuntu 16.04
FROM quay.io/python-devs/ci-image:latest

# Instala diferentes librerias para al proyecto
USER runner
WORKDIR /home/runner/

RUN pip3 install pandas luigi boto3 wget requests
RUN pip3 install pyarrow
