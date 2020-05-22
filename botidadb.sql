-- MySQL dump 10.13  Distrib 8.0.11, for macos10.13 (x86_64)
--
-- Host: localhost    Database: botica
-- ------------------------------------------------------
-- Server version	8.0.11

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8mb4 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Carrito`
--

DROP TABLE IF EXISTS `Carrito`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `Carrito` (
  `idCarrito` int(11) NOT NULL AUTO_INCREMENT,
  `Total` decimal(11,1) DEFAULT NULL,
  `Cantidad_productos` int(11) DEFAULT NULL,
  `Timestap` datetime DEFAULT NULL,
  PRIMARY KEY (`idCarrito`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Carrito`
--

LOCK TABLES `Carrito` WRITE;
/*!40000 ALTER TABLE `Carrito` DISABLE KEYS */;
/*!40000 ALTER TABLE `Carrito` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Carrito_has_Producto`
--

DROP TABLE IF EXISTS `Carrito_has_Producto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `Carrito_has_Producto` (
  `id_has` int(11) NOT NULL AUTO_INCREMENT,
  `Carrito_idCarrito` int(11) NOT NULL,
  `Cantidad` decimal(11,1) DEFAULT NULL,
  `Subtotal` decimal(11,1) DEFAULT NULL,
  `Presentacion` int(11) NOT NULL,
  `Producto` int(11) NOT NULL,
  PRIMARY KEY (`id_has`,`Carrito_idCarrito`,`Presentacion`,`Producto`),
  KEY `fk_Carrito_has_Productos_Carrito1_idx` (`Carrito_idCarrito`),
  KEY `fk_Carrito_has_Producto_Presentacion1_idx` (`Presentacion`,`Producto`),
  CONSTRAINT `fk_Carrito_has_Producto_Presentacion1` FOREIGN KEY (`Presentacion`, `Producto`) REFERENCES `presentacion` (`idpresentacion`, `producto`),
  CONSTRAINT `fk_Carrito_has_Productos_Carrito1` FOREIGN KEY (`Carrito_idCarrito`) REFERENCES `carrito` (`idcarrito`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Carrito_has_Producto`
--

LOCK TABLES `Carrito_has_Producto` WRITE;
/*!40000 ALTER TABLE `Carrito_has_Producto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Cliente`
--

DROP TABLE IF EXISTS `Cliente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `Cliente` (
  `idCliente` int(11) NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(45) COLLATE utf8_spanish_ci DEFAULT NULL,
  `Apellido` varchar(45) COLLATE utf8_spanish_ci DEFAULT NULL,
  `Contrasena` varchar(45) COLLATE utf8_spanish_ci DEFAULT NULL,
  `Email` varchar(100) COLLATE utf8_spanish_ci DEFAULT NULL,
  `Telefono` varchar(45) COLLATE utf8_spanish_ci DEFAULT NULL,
  `user` varchar(100) COLLATE utf8_spanish_ci DEFAULT NULL,
  PRIMARY KEY (`idCliente`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Cliente`
--

LOCK TABLES `Cliente` WRITE;
/*!40000 ALTER TABLE `Cliente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Compra`
--

DROP TABLE IF EXISTS `Compra`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `Compra` (
  `idCompra` int(11) NOT NULL AUTO_INCREMENT,
  `Direccion` varchar(45) COLLATE utf8_spanish_ci DEFAULT NULL,
  `Precio delivery` varchar(45) COLLATE utf8_spanish_ci DEFAULT NULL,
  `Tipo direccion` varchar(45) COLLATE utf8_spanish_ci DEFAULT NULL,
  `Fecha` date DEFAULT NULL,
  `Estado` varchar(45) COLLATE utf8_spanish_ci DEFAULT NULL,
  `Distrito` varchar(45) COLLATE utf8_spanish_ci DEFAULT NULL,
  `Cliente_idCliente` int(11) NOT NULL,
  `Comprado` longtext COLLATE utf8_spanish_ci,
  `Entregado` tinyint(1) DEFAULT NULL,
  `Total` decimal(11,1) DEFAULT NULL,
  PRIMARY KEY (`idCompra`,`Cliente_idCliente`),
  KEY `fk_Compra_Cliente1_idx` (`Cliente_idCliente`),
  CONSTRAINT `fk_Compra_Cliente1` FOREIGN KEY (`Cliente_idCliente`) REFERENCES `cliente` (`idcliente`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Compra`
--

LOCK TABLES `Compra` WRITE;
/*!40000 ALTER TABLE `Compra` DISABLE KEYS */;
/*!40000 ALTER TABLE `Compra` ENABLE KEYS */;
UNLOCK TABLES;


--
-- Table structure for table `Presentacion`
--

DROP TABLE IF EXISTS `Presentacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `Presentacion` (
  `idPresentacion` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) COLLATE utf8_spanish_ci DEFAULT NULL,
  `precio` decimal(11,1) DEFAULT NULL,
  `Producto` int(11) NOT NULL,
  PRIMARY KEY (`idPresentacion`,`Producto`),
  KEY `fk_Presentacion_Producto1_idx` (`Producto`),
  CONSTRAINT `fk_Presentacion_Producto1` FOREIGN KEY (`Producto`) REFERENCES `producto` (`idproductos`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Presentacion`
--

LOCK TABLES `Presentacion` WRITE;
/*!40000 ALTER TABLE `Presentacion` DISABLE KEYS */;
INSERT INTO `Presentacion` VALUES (1,'Caja',20.0,1),(2,'unidad',2.5,1),(3,'caja',15.8,2),(4,'caja',17.5,3),(5,'unidad',3.2,3),(6,'caja',13.0,4),(7,'caja',10.0,5);
/*!40000 ALTER TABLE `Presentacion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Producto`
--

DROP TABLE IF EXISTS `Producto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `Producto` (
  `idProductos` int(11) NOT NULL AUTO_INCREMENT,
  `Descripcion` varchar(400) COLLATE utf8_spanish_ci NOT NULL,
  `id_interno` int(11) NOT NULL,
  `Last_update` datetime DEFAULT NULL,
  `Stock` varchar(45) COLLATE utf8_spanish_ci DEFAULT NULL,
  PRIMARY KEY (`idProductos`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Producto`
--

LOCK TABLES `Producto` WRITE;
/*!40000 ALTER TABLE `Producto` DISABLE KEYS */;
INSERT INTO `Producto` VALUES (1,'Producto 1',13,NULL,NULL),(2,'producto 2',12,NULL,NULL),(3,'producto 3',4,NULL,NULL),(4,'producto 4',1,NULL,NULL),(5,'producto 5',19,NULL,NULL);
/*!40000 ALTER TABLE `Producto` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-05-22  7:34:11
