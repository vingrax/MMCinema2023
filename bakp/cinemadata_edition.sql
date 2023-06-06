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
-- Table structure for table `edition`
--

DROP TABLE IF EXISTS `edition`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `edition` (
  `Location` int DEFAULT NULL,
  `Name` varchar(20) DEFAULT NULL,
  `ID` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=98 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `edition`
--

LOCK TABLES `edition` WRITE;
/*!40000 ALTER TABLE `edition` DISABLE KEYS */;
INSERT INTO `edition` VALUES (6,'IT',1),(6,'KK',2),(6,'IK',3),(6,'IM',4),(6,'KC',5),(6,'KL',6),(6,'KV',7),(6,'KE',8),(6,'KR',9),(6,'KY',10),(11,'V2',11),(11,'S2',12),(11,'N2',13),(11,'T2',14),(6,'KP',15),(2,'WYD',16),(2,'VK',17),(2,'T',19),(2,'CITY',21),(3,'EM',27),(3,'EN',28),(3,'EU',29),(3,'EE',30),(3,'EK',31),(3,'EP',32),(3,'EF',33),(3,'ER',34),(4,'CP',35),(4,'CT',36),(4,'GA',37),(4,'GB',38),(5,'QC',39),(5,'QL',40),(5,'QL1',41),(5,'QK',42),(5,'QP',43),(8,'B',53),(8,'T',54),(8,'M',55),(8,'O',56),(8,'G',57),(8,'K',58),(8,'P',59),(10,'T1',64),(10,'T1A',65),(10,'T3A',66),(10,'T2',67),(10,'T3',68),(10,'T4',69),(7,'PRU',72),(7,'M1',73),(7,'M2MC',74),(7,'Nilambur',76),(1,'AM',79),(1,'AC',80),(1,'AH',81),(1,'AA',82),(1,'AK',83),(1,'AS',84),(9,'PC1',85),(9,'PM',86),(9,'PA',87),(9,'PC',88),(9,'PR',89),(9,'PY',90),(9,'PK',91),(10,'T4A',93),(4,'N',94),(4,'TC',95),(4,'TD',96),(5,'QS',97);
/*!40000 ALTER TABLE `edition` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-06-06 14:09:29
