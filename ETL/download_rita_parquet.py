#importamos las librerias
import requests
import wget
import zipfile
import os
#librerias para pasar a parquet
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

#Definimos los URL base para poder actualizarlo automaticamente despues
BASE_URL="https://transtats.bts.gov/PREZIP/On_Time_Reporting_Carrier_On_Time_Performance_1987_present_"
BASE_ZIP="On_Time_Reporting_Carrier_On_Time_Performance_1987_present_"
#Definimos el mes y el anio base
YEAR=1987
MONTH=10
#url_act es el url actualizado
url_act = BASE_URL+str(YEAR)+"_"+str(MONTH)+".zip"
zip_name = BASE_ZIP+str(YEAR)+"_"+str(MONTH)+".zip"
#descargamos el archivo en formato zip
wget.download(url_act)
#unzipeamos el archivo
with zipfile.ZipFile(zip_name, 'r') as zip_ref:
    zip_ref.extractall()

#eliminamos el zip
os.remove(zip_name)
os.remove("readme.html")

#identificamos el csv file
csv_file = "On_Time_Reporting_Carrier_On_Time_Performance_(1987_present)_"+str(YEAR)+"_"+str(MONTH)+".csv"

parquet_file = 'On_Time_Reporting.parquet'
chunksize = 100_000

csv_stream = pd.read_csv(csv_file, sep='\t', chunksize=chunksize, low_memory=False)

for i, chunk in enumerate(csv_stream):
    if (i<1):
        print("Chunk", i)
        if i == 0:
            # Guess the schema of the CSV file from the first chunk
            parquet_schema = pa.Table.from_pandas(df=chunk).schema
            # Open a Parquet file for writing
            parquet_writer = pq.ParquetWriter(parquet_file, parquet_schema, compression='snappy')
        # Write CSV chunk to the parquet file
        table = pa.Table.from_pandas(chunk, schema=parquet_schema)
        parquet_writer.write_table(table)

#eliminamos el csv
#os.remove(csv_file)
parquet_writer.close()
