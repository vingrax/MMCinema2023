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
-- Table structure for table `location_access`
--

DROP TABLE IF EXISTS `location_access`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `location_access` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int DEFAULT NULL,
  `locations` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_loc_id_idx` (`user_id`),
  CONSTRAINT `user_loc_id` FOREIGN KEY (`user_id`) REFERENCES `userlogin` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=72 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `location_access`
--

LOCK TABLES `location_access` WRITE;
/*!40000 ALTER TABLE `location_access` DISABLE KEYS */;
INSERT INTO `location_access` VALUES (1,1,'1'),(2,1,'2'),(3,1,'3'),(4,1,'4'),(5,1,'5'),(6,1,'6'),(7,1,'7'),(8,1,'8'),(9,1,'9'),(10,1,'10'),(11,1,'11'),(12,6,'1'),(13,6,'2'),(14,6,'3'),(15,6,'4'),(16,6,'5'),(17,6,'6'),(18,6,'7'),(19,6,'8'),(20,6,'9'),(21,6,'10'),(22,6,'11'),(23,9,'2'),(24,9,'7'),(25,9,'4'),(26,10,'2'),(27,10,'7'),(28,11,'2'),(29,11,'7'),(30,12,'2'),(31,12,'7'),(32,13,'2'),(33,13,'7'),(34,14,'2'),(35,14,'7'),(36,22,'2'),(37,22,'7'),(38,15,'6'),(39,16,'6'),(40,17,'6'),(41,18,'6'),(42,19,'6'),(43,20,'6'),(44,21,'6'),(45,15,'9'),(46,15,'1'),(47,16,'1'),(48,16,'9'),(49,17,'1'),(50,17,'9'),(51,23,'8'),(52,24,'8'),(53,25,'8'),(54,26,'8'),(55,27,'8'),(56,28,'8'),(57,29,'8'),(58,30,'4'),(59,15,'5'),(60,16,'5'),(61,17,'5'),(62,18,'5'),(63,19,'5'),(64,20,'5'),(65,21,'5'),(66,31,'5'),(67,32,'3'),(68,33,'10'),(69,34,'5'),(70,18,'1'),(71,18,'9');
/*!40000 ALTER TABLE `location_access` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-06-06 14:09:32
