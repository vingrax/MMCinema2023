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
-- Table structure for table `editiontheaters`
--

DROP TABLE IF EXISTS `editiontheaters`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `editiontheaters` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Location` int DEFAULT NULL,
  `Edition` int DEFAULT NULL,
  `Theater` int DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `editiontheaters_edition_edition_ID_idx` (`Edition`),
  KEY `editiontheaters_location_location_ID_idx` (`Location`),
  KEY `editiontheaters_theater_theaters_ID_idx` (`Theater`),
  CONSTRAINT `editiontheaters_edition_edition_ID` FOREIGN KEY (`Edition`) REFERENCES `edition` (`ID`),
  CONSTRAINT `editiontheaters_location_location_ID` FOREIGN KEY (`Location`) REFERENCES `location` (`id`),
  CONSTRAINT `editiontheaters_theater_theaters_ID` FOREIGN KEY (`Theater`) REFERENCES `theaters` (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='Specific theaters that are present in places but not in all related edition';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `editiontheaters`
--

LOCK TABLES `editiontheaters` WRITE;
/*!40000 ALTER TABLE `editiontheaters` DISABLE KEYS */;
INSERT INTO `editiontheaters` VALUES (1,2,17,151),(2,2,19,151),(3,2,17,150),(4,2,19,150),(5,10,69,332),(6,10,69,333),(7,10,69,334),(8,10,93,332),(9,10,93,333),(10,10,93,334),(11,7,73,449),(12,7,76,449);
/*!40000 ALTER TABLE `editiontheaters` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-06-06 14:09:31
