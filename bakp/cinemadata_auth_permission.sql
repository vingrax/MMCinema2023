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
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=72 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add input table',9,'add_inputtable'),(26,'Can change input table',9,'change_inputtable'),(27,'Can delete input table',9,'delete_inputtable'),(28,'Can view input table',9,'view_inputtable'),(29,'Can add spread',7,'add_spread'),(30,'Can change spread',7,'change_spread'),(31,'Can delete spread',7,'delete_spread'),(32,'Can view spread',7,'view_spread'),(33,'Can add edition',8,'add_edition'),(34,'Can change edition',8,'change_edition'),(35,'Can delete edition',8,'delete_edition'),(36,'Can view edition',8,'view_edition'),(37,'Can add editionplaces',10,'add_editionplaces'),(38,'Can change editionplaces',10,'change_editionplaces'),(39,'Can delete editionplaces',10,'delete_editionplaces'),(40,'Can view editionplaces',10,'view_editionplaces'),(41,'Can add location',12,'add_location'),(42,'Can change location',12,'change_location'),(43,'Can delete location',12,'delete_location'),(44,'Can view location',12,'view_location'),(45,'Can add places',13,'add_places'),(46,'Can change places',13,'change_places'),(47,'Can delete places',13,'delete_places'),(48,'Can view places',13,'view_places'),(49,'Can add theater',11,'add_theater'),(50,'Can change theater',11,'change_theater'),(51,'Can delete theater',11,'delete_theater'),(52,'Can view theater',11,'view_theater'),(53,'Can edit location Alappuzha',12,'editALP'),(54,'Can edit location Calicut',12,'editCLT'),(55,'Can edit location Cochin',12,'editCHN'),(56,'Can edit location Kannur',12,'editKNR'),(57,'Can edit location Kollam',12,'editQLN'),(58,'Can edit location Kottayam',12,'editKTM'),(59,'Can edit location Malappuram',12,'editMPM'),(60,'Can edit location Palakkad',12,'editPKD'),(61,'Can edit location Pathanamthitta',12,'editPTA'),(62,'Can edit location Thrissur',12,'editTCR'),(63,'Can edit location Trivandrum',12,'editTVM'),(64,'Can add daily inputs',14,'add_dailyinputs'),(65,'Can change daily inputs',14,'change_dailyinputs'),(66,'Can delete daily inputs',14,'delete_dailyinputs'),(67,'Can view daily inputs',14,'view_dailyinputs'),(68,'Can add screen',15,'add_screen'),(69,'Can change screen',15,'change_screen'),(70,'Can delete screen',15,'delete_screen'),(71,'Can view screen',15,'view_screen');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
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
