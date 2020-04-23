###TRANSFORM

CREATE TABLE transfom(
  fecha DATE,
  usuario CHAR(20),
  who_exec CHAR(20),
  num_obs_clean CHAR(10),
  status CHAT(10),
  
);


###LOAD


CREAT TABLE load(
  fecha DATE,
  usuario CHAR(20),
  ip_ec2 CHAR(20),
  where_exec CHAR(20),
  exec CHAR(20),  nums_obs_up CHAR(10),
  status CHAR(10)
)
;

###Clean


CREAT TABLE clean_data(
  fecha DATE,
  nombre_task VARCHAR,
  year VARCHAR,
  month VARCHAR,
  usuario VARCHAR,
  ip_clean VARCHAR,
  where_exec VARCHAR,
  exec VARCHAR,
  nums_filas_modificadas VARCHAR,
  variables_limpias VARCHAR,
  status VARCHAR
)
;

### Feature Engineering
CREAT TABLE feature_engineering(
    
  fecha DATE,
  nombre_task CHAR(20),
  YEAR CHAR(20),
  MONTH CHAR(20),
  usuario CHAR(20),
  ip_ec2 CHAR(20),
  filas_modificadas CHAR(20),
  variables CHAR(20), 
  ruta_s3 CHAR(10),
  task_status CHAR(10)
)
;
