# Extracion, transformacion y procesamiento de RITA en Postgres


Los archivos presentes en este directorio permita la descar de datos de RITA, empleando scripts de Bash, los cuales obtienen un archivo .zip con toda la informacion historica relativa a la multicitada base, hasta el ultimo periodo disponible, para posteriormente facilitar su carga hacia PostgreSQL (o simplemente Posgres).

## 1. Instrucciones del script para obtener los datos

Desde un sistema tipo Unix, asegurar de tener instalada la herramienta *wget*, tras ello dar permisos de ejecucion al archivo **download_rita.sh**

```
chmod +x
./download_rita.sh

```

Este paso baja la base zippeada y la descomprime en este directorio (en un .csv de aprox 250 MB)

**Nota:** Dicho paso es esencial para lograr el paso que sigue.

## 2. Instrucciones para generar los esquemas y cargar datos hacia raw

Desde un sistema tipo Unix, asegurarse de tener Postgres y psql instalados (ver referencia)[https://www.digitalocean.com/community/tutorials/como-instalar-y-utilizar-postgresql-en-ubuntu-18-04-es].

Ahora debemos cambiarnos a un usuario con permisos de interaccion con Postgres (se debe crear un role, aqui asumimos que entraremos con el usuario default *postgres*)

```
sudo su postres # cambiamos de usuario a postgres
psql # nos conecta al cliente con interaccion a postgres
```

Ahora podemos crear bases, hacer querys, etc. Con ello ejecutamos los scripts *.sql* presentes en la carpeta, tras conectarnos a psql:

**Creacion de esquemas raw, cleaned y semantic**

```
 \i create_schemas.sql
```

**Creacion de tabla raw.rita**

```
 \i create_raw_tables.sql
```

**Nota:** todas las variables de esta tabla son tipo texto, lo que se puede verificar con el comando:

```
 \d raw.rita
```


**Poblamos la tabla raw.rita con el .csv que descargamos**

```
 \i load_rita.sql
```

**Nota:** podemos revisar que la carga se ha hecho con querys, por ejemplo:

```
 SELECT Month from raw.rita;
```


**Nota:** Entiendo que esto lo hariamos en un RDS de AWS; se modificaran las presentes rutinas segun alcance y funciones de limpieza diseñadas por Danahi y Leon.
