#!/bin/bash
. credentials_psql.txt

#echo $user $password $host

PGPASSWORD=$password psql -U $user -h $host -d $db_name -c "\COPY raw.rita FROM 'data.csv'  WITH CSV HEADER;"

echo "Insersion de datos a esquema raw.rita terminada"
