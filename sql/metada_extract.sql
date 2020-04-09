CREATE SCHEMA IF NOT EXISTS metadatos;


---- EXTRACT
DROP TABLE IF EXISTS metadatos.extract;

CREATE TABLE metadatos.extract(
  fecha VARCHAR,
  nombre_task VARCHAR,
  year VARCHAR,
  month VARCHAR,
  usuario VARCHAR,
  ip_ec2 VARCHAR,
  tamano_zip VARCHAR,
  nombre_archivo VARCHAR,
  ruta_s3 VARCHAR,
  task_status VARCHAR
);


---- TRANSFORM

-- CREATE TABLE metadatos.transform(
--   fecha DATE,
--   usuario CHAR(20),
--   who_exec CHAR(20),
--   num_obs_clean CHAR(10),
--   status CHAT(10)
-- );
