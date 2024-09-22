/*Borrando y creando una base de datos*/
DROP DATABASE IF EXISTS base_clase_m1a;
CREATE DATABASE base_clase_m1a;

USE base_clase_m1a;

/*Creación de tablas*/ 
DROP TABLE IF EXISTS provincia;
CREATE TABLE provincia(
	id_provincia INT AUTO_INCREMENT NOT NULL COMMENT 'Campo clave de la tabla provincia',
    nombre VARCHAR(50) NOT NULL,
    PRIMARY KEY (id_provincia)
);

DROP TABLE IF EXISTS ciudad;
CREATE TABLE ciudad(
	id_ciudad INT AUTO_INCREMENT NOT NULL,
    nombre VARCHAR(50),
    id_provincia INT,
    PRIMARY KEY(id_ciudad),
    FOREIGN KEY(id_provincia) REFERENCES provincia(id_provincia)
);

/*Insertando datos*/
INSERT INTO provincia(nombre) VALUES('Azuay');
INSERT INTO provincia(nombre) VALUES('Cañar');
INSERT INTO provincia(nombre) VALUES('Guayas');
INSERT INTO provincia(nombre) VALUES('El Oro');
INSERT INTO provincia(nombre) VALUES('Manabi');
INSERT INTO provincia(nombre) VALUES('Loja');
INSERT INTO provincia(nombre) VALUES('Rios');

INSERT INTO ciudad(nombre, id_provincia) VALUES('Cuenca', 1);
INSERT INTO ciudad(nombre, id_provincia) VALUES('Paute', 1);
INSERT INTO ciudad(nombre, id_provincia) VALUES('Gualaceo', 1);
INSERT INTO ciudad(nombre, id_provincia) VALUES('Azogues', 2);
INSERT INTO ciudad(nombre, id_provincia) VALUES('Guayaqui', 3);
INSERT INTO ciudad(nombre, id_provincia) VALUES('Duran', 3);

/*Haciendo consultas*/
SELECT * FROM ciudad;
SELECT p.id_provincia, p.nombre, c.id_ciudad, c.nombre  FROM ciudad AS c INNER JOIN provincia AS p WHERE p.id_provincia = c.id_provincia AND p.id_provincia = 1;
SELECT * FROM ciudad WHERE ciudad.nombre LIKE '%a%';

/*Actualizando datos*/
UPDATE provincia SET nombre = 'Los Rios' WHERE provincia.nombre = 'Rios';
UPDATE ciudad SET nombre = 'Santa ana de los cuatro Rios de Cuenca' WHERE ciudad.nombre = 'Cuenca';

/*Eliminar datos*/
DELETE FROM ciudad WHERE ciudad.nombre NOT LIKE('%a%');


