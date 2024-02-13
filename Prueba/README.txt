//Se necesita un cliente para vizalizacion en PHP (para esta aplicacion se uso XAMPP & MySQL para la BD)
//Entro a la BD con  usuario root, password = ""
port: 3306
host: localhost

//Creacion de la BD
CREATE TABLE `prueba_bd`; 

CREATE TABLE `prueba_bd`.`usuarios`(
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nom` varchar(150) DEFAULT NULL,
  `email` varchar(150) DEFAULT NULL,
  `cumple` varchar(45) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `suscripcion` varchar(45) DEFAULT NULL,
  `telphone` varchar(20) DEFAULT NULL,
  `oficio` varchar(50) DEFAULT NULL,
  `location` varchar(45) DEFAULT NULL,
  `telphone` varchar(20) DEFAULT NULL,
  `oficio` varchar(50) DEFAULT NULL,
  `location` varchar(100) DEFAULT NULL,
  
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
