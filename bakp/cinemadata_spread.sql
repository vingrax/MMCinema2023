-- MySQL dump 10.13  Distrib 8.0.32, for Win64 (x86_64)
--
-- Host: localhost    Database: cinemadata
-- ------------------------------------------------------
-- Server version	8.0.32

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `spread`
--

DROP TABLE IF EXISTS `spread`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `spread` (
  `id` int NOT NULL AUTO_INCREMENT,
  `location` int DEFAULT NULL,
  `Edt_id` int NOT NULL,
  `Theater` varchar(100) DEFAULT NULL,
  `spread` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `Edt_id_idx` (`id`),
  CONSTRAINT `Edt_id` FOREIGN KEY (`id`) REFERENCES `edition` (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `spread`
--

LOCK TABLES `spread` WRITE;
/*!40000 ALTER TABLE `spread` DISABLE KEYS */;
INSERT INTO `spread` VALUES (1,2,16,'മിന്റ് സിനിമാസ്','True'),(2,2,21,'RP AASHIRVAD CINEPLEX','True'),(3,2,21,'റീഗൽ സിനിമാസ്','True'),(4,2,21,'E-MAX CINEMAS','True'),(5,2,21,'സുരഭി സിനിമാസ്','True'),(6,2,21,'മല്ലിക പ്ലക്സ്','True'),(7,2,21,'MAGIC FRAMES രാധ','True'),(8,2,17,'MAGIC FRAMES രാധ','True'),(9,2,19,'MAGIC FRAMES രാധ','True'),(10,2,17,'E-MAX CINEMAS','True'),(11,2,19,'E-MAX CINEMAS','True'),(12,2,21,'ARC കോറണേഷൻ','True'),(13,2,17,'ARC കോറണേഷൻ','True'),(14,2,19,'ARC കോറണേഷൻ','True');
/*!40000 ALTER TABLE `spread` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-06-06 14:09:30
