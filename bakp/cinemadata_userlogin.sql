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
-- Table structure for table `userlogin`
--

DROP TABLE IF EXISTS `userlogin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `userlogin` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_name` varchar(100) NOT NULL,
  `passw` text NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  `Privilege` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `userlogin`
--

LOCK TABLES `userlogin` WRITE;
/*!40000 ALTER TABLE `userlogin` DISABLE KEYS */;
INSERT INTO `userlogin` VALUES (1,'admin','sysadmin','administrator','user'),(6,'gireesh','Gireesh','Gireesh','user'),(8,'administrator','sysadmin','administrator','user'),(9,'9101dal','D@l1234','Dajan Lukose','user'),(10,'2158mkp','Mk@2158','Mohammedkutty P','user'),(11,'7977anm','An*7977','Anoop M','user'),(12,'0976RKA','Rka@976','Roy K A','user'),(13,'0999RKD','Rkd#999','Rajesh Kumar D K','user'),(14,'0994SUK','Suk$994','Sunil K','user'),(15,'5426ALJ','Alj%5426','Aleena Joseph','user'),(16,'5425VIM','V!m*5425','Vijaya Manu','user'),(17,'0846MIM','M!m@0846','Manoj I Mathew','user'),(18,'5439SSZ','Ssz#5439','Sajith Sunny','user'),(19,'7759ABM','Abm&7759','Abeymon Mathew','user'),(20,'7760JUJ','Juj$7760','Julia John','user'),(21,'2107CKJ','c&j#2107','Jacob C K','user'),(22,'7593BAC','Bac!7593','Balasubramannian C','user'),(23,'6047MKK','Mmk$6047','ManojKumar K','user'),(24,'1154SRM','Srm@1154','Sreekumar M','user'),(25,'7935SHT','Sht%7935','Shyma Thomas','user'),(26,'7579NOM','Nom$7579','Noushad M','user'),(27,'3036SVV','Svv#3036','Saju V V','user'),(28,'7910JKA','Jka@7910','Johnson K A','user'),(29,'9179SKK','Skk!9179','Sadeesh Kumar K P','user'),(30,'3725var','varun@123','Varun','user'),(31,'obituser','obituser','obit user','user'),(32,'chnuser','chnuser','chnuser','user'),(33,'tcruser','tcruser','tcr user','user'),(34,'mktklm','klmmkt','mkt klm','user');
/*!40000 ALTER TABLE `userlogin` ENABLE KEYS */;
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
