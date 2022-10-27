
#---------CONSULTAS DE PRUEBA-------------

#Cantidad de registros en la tabla operacion
select count(*) from operacion;

#Precio promedio de la sucursal 9-1-688
select round(AVG(o.precio), 2) as Promedio from sucursal s
inner join operacion o ON (s.IdSucursal = o.IdOperacion)
where s.IdSucursal = '9-1-688';

#Precio promedio de la sucursal 10-2-182
select round(AVG(o.precio), 2) as Promedio from sucursal s
inner join operacion o ON (s.IdSucursal = o.IdOperacion)
where s.IdSucursal = '10-2-182';

#Probamos un simple inner join para ver si funciona bien las claves foráneas
select * from sucursal s
inner join operacion o ON (s.IdSucursal = o.IdOperacion)
inner join producto p ON (o.IdProducto = p.Idproducto)
where p.IdProducto = '0000000206143';

#Traemos las sucursales de la localidad de Usuahia, bernal y Corrientes
select * from sucursal where Localidad IN ('Usuahia', 'Bernal', 'Corrientes');

#Select simples para traer los datos
select * from operacion;
select * from sucursal;
select * from producto;

select * from operacion where outlier = 2;

