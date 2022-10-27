#Creamos la base de datos
create database data01;
use data01;

#drop table sucursal;
#drop table producto;
#drop table operacion;

#Creamos las tablas
create table sucursal (
	IdSucursal varchar(15),
	IdComercio varchar(5),
	IdBandera varchar(5),
	BanderaDesc varchar(70),
	ComercioRazonSocial varchar(150),
	Provincia varchar(30),
	Localidad varchar(70),
	Domicilio varchar(70),
	Latitud varchar(20),
	Longitud varchar(20),
	SucursalNombre varchar(70),
	SucursalTipo varchar(50),
	primary key(IdSucursal)
)engine=InnoDB default charset=utf8mb4 collate=utf8mb4_spanish_ci
;

create table producto (
	IdProducto varchar(30),
	marca varchar(50),
	nombre varchar(150),
	presentacion varchar(30),
	primary key(IdProducto)
)engine=InnoDB default charset=utf8mb4 collate=utf8mb4_spanish_ci
;

#En esta tabla el precio es muy grande debido a los outliers
create table operacion (
	IdOperacion int auto_increment not null,
	IdProducto varchar(30) not null,
	IdSucursal varchar(15) not null,
	precio decimal(30,2),
	fecha date,
	outlier tinyint default 0 not null,
	primary key(IdOperacion),
	foreign Key(IdProducto) references producto(IdProducto),
	foreign key(IdSucursal) references sucursal(IdSucursal)
)engine=InnoDB default charset=utf8mb4 collate=utf8mb4_spanish_ci
;
