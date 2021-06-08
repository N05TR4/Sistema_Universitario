create database bd_universidad;
use bd_universidad;

create table login(
Usuario varchar(30) not null,
Contraseña varchar(30) not null,
fecha TIMESTAMP
)

select * from login;

create table Estudiante(
nombre varchar(50) not null,
apellido varchar(50) not null,
direccion varchar(100) not null,
fecha_nacimiento varchar(100) not null,
telefono varchar(20) not null,
matricula varchar(50) not null,
carrera varchar(50) not null,
primary key(matricula)
)engine=InnoDB;


create table carrera(
nombre varchar(50) not null,
primary key(nombre)
);

alter table Estudiante add foreign key(carrera) references carrera(nombre);

create table materia(
nombre varchar(50) not null,
horario varchar(50) not null,
profesor varchar(50) not null,
estudiante varchar(50) not null,
primary key(nombre)
);


create table seccion(
seccion varchar(20) not null,
primary key(seccion)
);

create table profesor(
nombre varchar(50) not null,
apellido varchar(50) not null,
direccion varchar(100) not null,
fecha_nacimiento varchar(100) not null,
telefono varchar(20) not null,
seccion varchar(20) not null,
materia varchar(50) not null,
primary key(nombre)
);

alter table materia add foreign key(profesor) references profesor(nombre);
alter table materia add foreign key(estudiante) references Estudiante(matricula);
alter table profesor add foreign key(seccion) references seccion(seccion);

select *from carrera;
select *from Estudiante;
select *from profesor;
select *from seccion;
select *from materia;
