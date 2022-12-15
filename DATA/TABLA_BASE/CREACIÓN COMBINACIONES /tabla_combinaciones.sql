CREATE DATABASE PROYECTO_FINAL;

-- COMBINACIONES ENTRE TABLAS
CREATE TABLE combinaciones
SELECT 
    DISTINCT
    c.COLORES CABELLO,
    o.COLORES OJOS,
    p.COLORES PIEL,
    cr.CROMA CROMA
FROM 
    cabello c,
    ojos o,
    piel p,
    croma cr;

SELECT * FROM combinaciones;

