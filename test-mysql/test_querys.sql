/* 
Teniendo en cuenta los archivos:
- softpymes_test.png
- softpymes_test.sql
Generar scripts que realicen las siguientes consultas:
*/

/* 1. Consultar los items que pertenezcan a la compañia con ID #3 (debe utilizar INNER JOIN), 
   en donde dicha compañia contenga una 'A' en su nombre */
SELECT * FROM `items` INNER JOIN companies ON companies.id=items.companyId WHERE companyId= 3 AND companies.name LIKE "%a%"

/* 2. Mostrar los items para los cuales su precio se encuentre en el rango 70000 a */
 SELECT * FROM `items` WHERE price BETWEEN 70000 AND 90000

/* 3. Mostrar los items que en el nombre inicien con la letra "A" */
SELECT * FROM `items` WHERE name LIKE "a%"

/* 4. Mostrar los items que tengan relacionado el color Rojo */
SELECT i.name,c.name FROM items i INNER JOIN colors c on i.colorId = c.id WHERE c.name = "ROJO

/* 5. Se requiere asignar un precio a los items cuyo precio sea NULL, 
el precio a agregar debe ser calculado de la siguiente forma: costo del item + 10.000*/
update items set price= cost + 0000  WHERE price = 0

/* 6. Incrementar el precio de los items en un 20% */
UPDATE items SET price = ROUND( price * 1.20, 2 );


/* 7. Consultar los items que terminen en la letra "A" en el nombre, y anteponer la 
palabra "Nuevo" */
SELECT CONCAT("nuevo"," ",name) FROM `items` WHERE name LIKE "%a" 

/* 8. Eliminar los items que pertenezcan a la compañía con ID #1 */
DELETE * FROM `items` WHERE companyId = 1

/* 9. Eliminar los items que tengan el costo menor a 10.000 */
DELETE * FROM `items` WHERE cost < 10000

/* 10. Cree una función que permita insertar registros en la tabla colores*/
INSERT INTO `colors`( `code`, `name`) VALUES ('[value-2]','[value-3]')

/* 11. Eliminar todos los datos de la tabla colores */
DELETE * FROM `colors` 

/* 12. Agregar un campo llamado "description" en la tabla items, que permita ser NULL, 
y que tenga un máximo de 200 caracteres */
ALTER TABLE items ADD description VARCHAR(200) NULL; 
