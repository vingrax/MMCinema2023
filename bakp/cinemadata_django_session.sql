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
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('d9o5fx16xup92idnwywt2dcoumi6i2ed','.eJxVjEEOwiAQRe_C2hDAAoNL9z0DmRlAqoYmpV0Z765NutDtf-_9l4i4rTVuPS9xSuIitDj9boT8yG0H6Y7tNkue27pMJHdFHrTLcU75eT3cv4OKvX5rIPBZeUpeZ6sZtMbBgLIWOISz8wGzNd4FKIZtweSIPBedkNQAhpV4fwDOMzew:1q1PID:4biSyugqFe36H2vqN6CYMAc1Nt_WDfgTj_Ah2cELj6c','2023-06-06 10:31:01.984255'),('kq9bop4gekab4326qr20ibvtkl7k8mqi','.eJxVjEEOwiAQRe_C2hDAAoNL9z0DmRlAqoYmpV0Z765NutDtf-_9l4i4rTVuPS9xSuIitDj9boT8yG0H6Y7tNkue27pMJHdFHrTLcU75eT3cv4OKvX5rIPBZeUpeZ6sZtMbBgLIWOISz8wGzNd4FKIZtweSIPBedkNQAhpV4fwDOMzew:1psGnI:BpjkY3T3hAbEg2cQOjuV_5TNUPWm5duv4RLPXP5OyAo','2023-05-12 05:37:20.962431'),('rkyb52ants7i7c7e223iofaki7z7vcm1','.eJxVjEEOwiAQRe_C2hDAAoNL9z0DmRlAqoYmpV0Z765NutDtf-_9l4i4rTVuPS9xSuIitDj9boT8yG0H6Y7tNkue27pMJHdFHrTLcU75eT3cv4OKvX5rIPBZeUpeZ6sZtMbBgLIWOISz8wGzNd4FKIZtweSIPBedkNQAhpV4fwDOMzew:1pd617:l0J1SJJXTwPwiD0YUoJIIhvBSV1nRZDF8vV4XSRobfM','2023-03-31 09:04:53.785085');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
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
