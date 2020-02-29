## Descarga la base de datos Rita desde 1987 hasta el presente (YYYY_MM)
#! /bin/bash

BASE_URL="https://transtats.bts.gov/PREZIP/On_Time_Reporting_Carrier_On_Time_Performance_1987_present_"
BASE_ZIP="On_Time_Reporting_Carrier_On_Time_Performance_1987_present_"

## Esto linea deberia ser dinamica cuando se ejecute periodicamente

YEAR=2019
MONTH=11

# Obtenemos el zip
wget ${BASE_URL}${YEAR}"_"${MONTH}".zip"

# Descomprimimos el zip, eliminando archivos remanentes
unzip ${BASE_ZIP}${YEAR}"_"${MONTH}".zip" # Crea .csv
rm ${BASE_ZIP}${YEAR}"_"${MONTH}".zip"
rm 'readme.html'
