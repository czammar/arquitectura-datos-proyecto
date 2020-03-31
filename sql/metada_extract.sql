CREATE SCHEMA IF NOT EXISTS metadatos;


---- EXTRACT
DROP TABLE IF EXISTS metadatos.extract;

CREATE TABLE metadatos.extract(
  fecha TEXT,
  nombre_task TEXT,
  parametros TEXT,
  usuario TEXT,
  ip_ec2 TEXT,
  tamano_zip TEXT,
  nombre_archivo TEXT,
  ruta_s3 TEXT,
  task_status TEXT
);


---- TRANSFORM

-- CREATE TABLE metadatos.transform(
--   fecha DATE,
--   usuario CHAR(20),
--   who_exec CHAR(20),
--   num_obs_clean CHAR(10),
--   status CHAT(10)
-- );
