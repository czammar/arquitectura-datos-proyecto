# Script para descargar la base completa de RITA hasta
# 12/2019 (ultima fecha de publicacion conocida)

# No olvidemos darle permisos chmod +x download_rita_parametric.sh
# Ejecutamos como: ./download_rita_parametric.sh

BASE_URL="https://transtats.bts.gov/PREZIP/On_Time_Reporting_Carrier_On_Time_Performance_1987_present_"

function download_data() {
    for url in "${BASE_URL}"{1987..2019}"_"{1..12}".zip"
    do
        echo ${url}
        wget ${url}
    done
}

download_data
