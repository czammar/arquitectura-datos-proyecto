###EXTRACT

CREATE TABLE extract(
  fecha DATE,
  parametros CHAR(30),
  usuario CHAR(20),
  ip_ec2 CHAR(20),
  num_renglones CHAR(10),
  nombre_archivo CHAR(20),
  ruta_s3 CHAR(30),
  variable_datos CHAR(30)
);


###TRANSFORM

CREATE TABLE transfom(
  fecha DATE,
  usuario CHAR(20),
  who_exec CHAR(20),
  num_obs_clean CHAR(10),
  status CHAT(10),
  
)



###LOAD


CREAT TABLE load(
  fecha DATE,
  usuario CHAR(20),
  ip_ec2 CHAR(20),
  where_exec CHAR(20),
  exec CHAR(20),
  nums_obs_up CHAR(10),
  status CHAR(10)
)
;