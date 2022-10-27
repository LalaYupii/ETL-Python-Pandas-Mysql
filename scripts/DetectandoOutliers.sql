
#La idea aquí es una clasificación en dónde cada número en el campo 
#outlier representa un tipo de outlier.
#Por fines práctico no se armo una tabla en dónde se encontrarian los tipos de outliers.

#-------Buscamos Outliers en la tabla Precio------------
-- 1 -> precio con valor 0.0
-- 2 -> precio que es mayor al promedio
-- 3 -> inconsistencia en precio (caso especial del archivo xlsx precio_semana_20200426) 

#Outlier de precio cero
UPDATE operacion
SET outlier = 1 where precio = 0.0;

#Outlier precios que superar el promedio
UPDATE operacion q1
JOIN (	SELECT IdSucursal, round(avg(precio), 2) as Promedio, stddev(precio) as Desv
		from operacion
		GROUP BY IdSucursal) q2
ON (q1.IdSucursal = q2.IdSucursal)
SET q1.outlier = 2
WHERE q1.precio > round((q2.Promedio + (3*q2.Desv)), 2);

#Outlier de caso especial del archivo de excel precios_semana_20200426
UPDATE operacion
SET outlier = 3 where fecha = '2020-04-26';


