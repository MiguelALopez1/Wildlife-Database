/*!999999\- enable the sandbox mode */ 
-- MariaDB dump 10.19  Distrib 10.6.18-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: 73.171.45.18    Database: wildlife_call_database
-- ------------------------------------------------------
-- Server version	10.11.6-MariaDB-0+deb12u1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Admin`
--

DROP TABLE IF EXISTS `Admin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Admin` (
  `admin_id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(50) DEFAULT NULL,
  `last_name` varchar(50) DEFAULT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(255) NOT NULL COMMENT 'Stores BCrypt hashed passwords',
  `last_login` timestamp NULL DEFAULT NULL,
  `password_reset_token` varchar(255) DEFAULT NULL,
  `password_reset_expires` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`admin_id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Admin`
--

LOCK TABLES `Admin` WRITE;
/*!40000 ALTER TABLE `Admin` DISABLE KEYS */;
INSERT INTO `Admin` VALUES (2,'Admin','User2','AdminUser2','$2b$12$a9087b68a55911ef99d4f7aa7138c32dRESET_REQUIRED_a581e90e-a53a-11ef-99d4-f7aa7138c32d',NULL,NULL,NULL),(3,'Admin','User3','AdminUser3','$2b$12$a90883aaa55911ef99d4f7aa7138c32dRESET_REQUIRED_a581eebd-a53a-11ef-99d4-f7aa7138c32d',NULL,NULL,NULL),(4,'Admin','User4','AdminUser4','$2b$12$a90889bfa55911ef99d4f7aa7138c32dRESET_REQUIRED_a581f3f2-a53a-11ef-99d4-f7aa7138c32d',NULL,NULL,NULL),(5,'Admin','User5','AdminUser5','$2b$12$a9088fd5a55911ef99d4f7aa7138c32dRESET_REQUIRED_a581f925-a53a-11ef-99d4-f7aa7138c32d',NULL,NULL,NULL),(6,'Admin','User','admin1','IY5X5GHpXsAFswxbwu8dpzIly4od+Rx18ySUErQGUM0',NULL,NULL,NULL);
/*!40000 ALTER TABLE `Admin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Audiofiles`
--

DROP TABLE IF EXISTS `Audiofiles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Audiofiles` (
  `audiofiles_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `taxonomy_id` int(11) DEFAULT NULL,
  `file_name` varchar(255) DEFAULT NULL,
  `upload_date` date DEFAULT NULL,
  `rating` int(11) DEFAULT NULL,
  `duration` time DEFAULT NULL,
  `is_certified` tinyint(1) DEFAULT 0,
  PRIMARY KEY (`audiofiles_id`),
  KEY `user_id` (`user_id`),
  KEY `Audiofiles_ibfk_2` (`taxonomy_id`),
  CONSTRAINT `Audiofiles_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `User` (`user_id`),
  CONSTRAINT `Audiofiles_ibfk_2` FOREIGN KEY (`taxonomy_id`) REFERENCES `Taxonomy` (`taxonomy_id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=43 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Audiofiles`
--

LOCK TABLES `Audiofiles` WRITE;
/*!40000 ALTER TABLE `Audiofiles` DISABLE KEYS */;
INSERT INTO `Audiofiles` VALUES (7,1,1,'Zebra.mp3','2024-10-21',5,'00:03:45',1),(8,2,2,'Bison.mp3','2024-10-21',2,'00:02:43',0),(9,3,3,'Dog.mp3','2024-10-21',5,'00:01:23',1),(10,4,4,'Cat.mp3','2024-10-21',4,'00:04:54',1),(11,5,5,'Bird.mp3','2024-10-21',2,'00:01:04',0),(20,1,14,'Homo_sapiens.mp3','2024-10-30',3,'00:03:30',1),(21,2,15,'Ursus_arctos.mp3','2024-10-30',4,'00:04:15',1),(22,4,16,'Haliaeetus_leucocephalus.mp3','2024-10-30',5,'00:02:50',1),(23,3,17,'Tursiops_truncatus.mp3','2024-10-30',4,'00:05:10',1),(24,2,18,'Loxodonta_africana.mp3','2024-10-30',3,'00:06:00',1),(25,2,19,'Boa_constrictor.mp3','2024-10-30',2,'00:04:45',1),(26,2,20,'Cervus_canadensis.mp3','2024-10-30',5,'00:03:15',1),(27,1,21,'Panthera_tigris.mp3','2024-10-30',4,'00:04:00',1),(28,4,22,'Canis_lupus.mp3','2024-10-30',3,'00:03:40',1),(29,2,23,'Falco_peregrinus.mp3','2024-10-30',4,'00:03:25',1),(30,3,24,'Gorilla_gorilla.mp3','2024-10-30',3,'00:05:25',1),(31,1,25,'Chelonia_mydas.mp3','2024-10-30',2,'00:02:55',1),(32,2,26,'Pan_paniscus.mp3','2024-10-30',5,'00:04:50',1),(33,4,27,'Pongo_pygmaeus.mp3','2024-10-30',4,'00:04:35',1),(34,3,28,'Strix_alba.mp3','2024-10-30',4,'00:03:00',1),(35,3,29,'Equus_caballus.mp3','2024-10-30',5,'00:03:45',1),(36,3,30,'Psittacus_erithacus.mp3','2024-10-30',3,'00:04:05',1),(37,4,31,'Phoenicopterus_ruber.mp3','2024-10-30',4,'00:03:20',1),(38,2,32,'Panthera_leo.mp3','2024-10-30',5,'00:03:35',1),(39,1,33,'Vulpes_vulpes.mp3','2024-10-30',3,'00:02:45',1);
/*!40000 ALTER TABLE `Audiofiles` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb3 */ ;
/*!50003 SET character_set_results = utf8mb3 */ ;
/*!50003 SET collation_connection  = utf8mb3_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`remote_user`@`%`*/ /*!50003 TRIGGER after_audiofile_insert
AFTER INSERT ON `Audiofiles`
FOR EACH ROW
BEGIN
    INSERT INTO `AuditLog` (user_id, action, table_name, record_id)
    VALUES (NEW.user_id, 'INSERT', 'Audiofiles', NEW.audiofiles_id);
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb3 */ ;
/*!50003 SET character_set_results = utf8mb3 */ ;
/*!50003 SET collation_connection  = utf8mb3_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`remote_user`@`%`*/ /*!50003 TRIGGER after_audiofile_update
AFTER UPDATE ON `Audiofiles`
FOR EACH ROW
BEGIN
    INSERT INTO `AuditLog` (user_id, action, table_name, record_id)
    VALUES (NEW.user_id, 'UPDATE', 'Audiofiles', NEW.audiofiles_id);
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb3 */ ;
/*!50003 SET character_set_results = utf8mb3 */ ;
/*!50003 SET collation_connection  = utf8mb3_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`remote_user`@`%`*/ /*!50003 TRIGGER after_audiofile_delete
AFTER DELETE ON `Audiofiles`
FOR EACH ROW
BEGIN
    INSERT INTO `AuditLog` (user_id, action, table_name, record_id)
    VALUES (OLD.user_id, 'DELETE', 'Audiofiles', OLD.audiofiles_id);
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `AuditLog`
--

DROP TABLE IF EXISTS `AuditLog`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `AuditLog` (
  `log_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `action` varchar(255) NOT NULL,
  `table_name` varchar(50) DEFAULT NULL,
  `record_id` int(11) DEFAULT NULL,
  `timestamp` timestamp NULL DEFAULT current_timestamp(),
  `ip_address` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`log_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `AuditLog_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `User` (`user_id`) ON DELETE SET NULL
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `AuditLog`
--

LOCK TABLES `AuditLog` WRITE;
/*!40000 ALTER TABLE `AuditLog` DISABLE KEYS */;
INSERT INTO `AuditLog` VALUES (1,1,'LOGIN',NULL,NULL,'2024-11-22 01:01:37','127.0.0.1'),(2,1,'LOGOUT',NULL,NULL,'2024-11-22 01:03:00','127.0.0.1'),(3,1,'LOGIN',NULL,NULL,'2024-11-22 13:59:28','127.0.0.1'),(4,1,'LOGIN',NULL,NULL,'2024-11-22 13:59:34','127.0.0.1'),(5,6,'LOGIN',NULL,NULL,'2024-11-22 14:12:50','127.0.0.1'),(6,6,'LOGIN',NULL,NULL,'2024-11-22 14:35:16','127.0.0.1'),(7,6,'LOGIN',NULL,NULL,'2024-11-22 14:36:35','127.0.0.1'),(8,6,'LOGIN',NULL,NULL,'2024-11-22 16:59:13','127.0.0.1'),(9,6,'LOGOUT',NULL,NULL,'2024-11-22 17:00:21','127.0.0.1'),(10,6,'LOGIN',NULL,NULL,'2024-11-22 17:22:52','127.0.0.1'),(11,6,'LOGIN',NULL,NULL,'2024-11-22 17:26:52','127.0.0.1'),(12,6,'LOGOUT',NULL,NULL,'2024-11-22 17:27:31','127.0.0.1'),(13,6,'LOGIN',NULL,NULL,'2024-11-22 17:37:50','127.0.0.1'),(14,6,'LOGIN',NULL,NULL,'2024-11-22 17:50:55','127.0.0.1'),(15,6,'LOGIN',NULL,NULL,'2024-11-22 18:12:40','127.0.0.1'),(16,6,'LOGIN',NULL,NULL,'2024-11-22 18:21:22','127.0.0.1'),(17,6,'LOGOUT',NULL,NULL,'2024-11-22 18:22:32','127.0.0.1'),(18,6,'LOGIN',NULL,NULL,'2024-11-22 18:23:02','127.0.0.1'),(19,6,'LOGOUT',NULL,NULL,'2024-11-22 18:25:22','127.0.0.1'),(20,6,'LOGIN',NULL,NULL,'2024-11-22 18:32:47','127.0.0.1');
/*!40000 ALTER TABLE `AuditLog` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `LoginAttempts`
--

DROP TABLE IF EXISTS `LoginAttempts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `LoginAttempts` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `ip_address` varchar(45) NOT NULL,
  `attempt_time` timestamp NULL DEFAULT current_timestamp(),
  `success` tinyint(1) DEFAULT 0,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `LoginAttempts`
--

LOCK TABLES `LoginAttempts` WRITE;
/*!40000 ALTER TABLE `LoginAttempts` DISABLE KEYS */;
INSERT INTO `LoginAttempts` VALUES (1,'asmith','127.0.0.1','2024-11-21 21:13:46',0);
/*!40000 ALTER TABLE `LoginAttempts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Sessions`
--

DROP TABLE IF EXISTS `Sessions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Sessions` (
  `session_id` varchar(255) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `user_type` enum('admin','user') NOT NULL,
  `login_time` timestamp NULL DEFAULT current_timestamp(),
  `expiry_time` timestamp NOT NULL,
  `ip_address` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`session_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `Sessions_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `User` (`user_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Sessions`
--

LOCK TABLES `Sessions` WRITE;
/*!40000 ALTER TABLE `Sessions` DISABLE KEYS */;
INSERT INTO `Sessions` VALUES ('0b988f77dfd57e7500dd92940d76714060d52b32d43b2b8a43277394b18bb4c8',1,'user','2024-11-22 13:59:27','2024-11-23 13:59:26','127.0.0.1'),('0c29baf01b4ec66785beb71ea260bc40519eb663f2fe5ed7c3669ab00393b945',6,'user','2024-11-22 14:35:15','2024-11-23 14:35:15','127.0.0.1'),('5a21f1038114e6bea9bca9d890f4e3922b67b514d311bf5c26b6b26342d83992',6,'admin','2024-11-22 17:50:52','2024-11-23 17:50:52','127.0.0.1'),('755ce17c7cc266c38415f52103c2f6958d7e6143813342c1633a3f433bc96f0a',1,'user','2024-11-22 13:59:31','2024-11-23 13:59:31','127.0.0.1'),('91603839dab43b1704e7b05feb4080627e62435231423367c87bc7afa15dc1c9',6,'user','2024-11-22 17:22:50','2024-11-23 17:22:50','127.0.0.1'),('97c7f444cec287916384c16065a4cf8e4f4e21460ce34f6266682afebe59f7dc',6,'user','2024-11-22 14:36:35','2024-11-23 14:36:34','127.0.0.1'),('bf0026f2fa74a47d86d0fd44d60ada291fcf1260df94ee85201ae7306827a92b',6,'admin','2024-11-22 17:37:47','2024-11-23 17:37:46','127.0.0.1'),('bf80023f9f14c10e6ede1a6269d984151e82f1b905662a91a9d7e5ea41f2ecd3',6,'user','2024-11-22 14:12:49','2024-11-23 14:12:50','127.0.0.1'),('c89e6ee17bbf745bcb0f4aaeef84e5372822f21829c0de03b7414e0a87c24a5e',6,'user','2024-11-22 18:32:45','2024-11-23 18:32:43','127.0.0.1'),('fb852b4ab2c88923bed262bac6985083ae4405af518fc4d8bdbbe2dc642fd814',6,'admin','2024-11-22 18:12:37','2024-11-23 18:12:36','127.0.0.1');
/*!40000 ALTER TABLE `Sessions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Taxonomy`
--

DROP TABLE IF EXISTS `Taxonomy`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Taxonomy` (
  `taxonomy_id` int(11) NOT NULL AUTO_INCREMENT,
  `domain` varchar(50) DEFAULT NULL,
  `kingdom` varchar(50) DEFAULT NULL,
  `phylum` varchar(50) DEFAULT NULL,
  `class` varchar(50) DEFAULT NULL,
  `order` varchar(50) DEFAULT NULL,
  `family` varchar(50) DEFAULT NULL,
  `genus` varchar(50) DEFAULT NULL,
  `species` varchar(50) DEFAULT NULL,
  `audiofile_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`taxonomy_id`),
  KEY `fk_audiofile` (`audiofile_id`),
  CONSTRAINT `fk_audiofile` FOREIGN KEY (`audiofile_id`) REFERENCES `Audiofiles` (`audiofiles_id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Taxonomy`
--

LOCK TABLES `Taxonomy` WRITE;
/*!40000 ALTER TABLE `Taxonomy` DISABLE KEYS */;
INSERT INTO `Taxonomy` VALUES (1,'Eukaryota','Animalia','Chordata','Mammalia','Perissodactyla','Equidae','Equus','Equus quagga',7),(2,'Eukaryota','Animalia','Chordata','Mammalia','Artiodactyla','Bovidae','Bison','Bison bison',8),(3,'Eukaryota','Animalia','Chordata','Mammalia','Carnivora','Canidae','Canis','Canis lupus familiaris',9),(4,'Eukaryota','Animalia','Chordata','Mammalia','Carnivora','Felidae','Felis','Felis catus',10),(5,'Eukaryota','Animalia','Chordata','Aves','Sphenisciformes','Spheniscidae','Aptenodytes','Aptenodytes forsteri',11),(14,'Eukaryota','Animalia','Chordata','Mammalia','Primates','Hominidae','Homo','Homo sapiens',20),(15,'Eukaryota','Animalia','Chordata','Mammalia','Carnivora','Ursidae','Ursus','Ursus arctos',21),(16,'Eukaryota','Animalia','Chordata','Aves','Accipitriformes','Accipitridae','Haliaeetus','Haliaeetus leucocephalus',22),(17,'Eukaryota','Animalia','Chordata','Mammalia','Cetacea','Delphinidae','Tursiops','Tursiops truncatus',23),(18,'Eukaryota','Animalia','Chordata','Mammalia','Proboscidea','Elephantidae','Loxodonta','Loxodonta africana',24),(19,'Eukaryota','Animalia','Chordata','Reptilia','Squamata','Boidae','Boa','Boa constrictor',25),(20,'Eukaryota','Animalia','Chordata','Mammalia','Artiodactyla','Cervidae','Cervus','Cervus canadensis',26),(21,'Eukaryota','Animalia','Chordata','Mammalia','Carnivora','Felidae','Panthera','Panthera tigris',27),(22,'Eukaryota','Animalia','Chordata','Mammalia','Carnivora','Canidae','Canis','Canis lupus',28),(23,'Eukaryota','Animalia','Chordata','Aves','Falconiformes','Falconidae','Falco','Falco peregrinus',29),(24,'Eukaryota','Animalia','Chordata','Mammalia','Primates','Hominidae','Gorilla','Gorilla gorilla',30),(25,'Eukaryota','Animalia','Chordata','Reptilia','Testudines','Cheloniidae','Chelonia','Chelonia mydas',31),(26,'Eukaryota','Animalia','Chordata','Mammalia','Primates','Hominidae','Pan','Pan paniscus',32),(27,'Eukaryota','Animalia','Chordata','Mammalia','Primates','Hominidae','Pongo','Pongo pygmaeus',33),(28,'Eukaryota','Animalia','Chordata','Aves','Strigiformes','Strigidae','Strix','Strix alba',34),(29,'Eukaryota','Animalia','Chordata','Mammalia','Perissodactyla','Equidae','Equus','Equus caballus',35),(30,'Eukaryota','Animalia','Chordata','Aves','Psittaciformes','Psittacidae','Psittacus','Psittacus erithacus',36),(31,'Eukaryota','Animalia','Chordata','Aves','Phoenicopteriformes','Phoenicopteridae','Phoenicopterus','Phoenicopterus ruber',37),(32,'Eukaryota','Animalia','Chordata','Mammalia','Carnivora','Felidae','Panthera','Panthera leo',38),(33,'Eukaryota','Animalia','Chordata','Mammalia','Carnivora','Canidae','Vulpes','Vulpes vulpes',39);
/*!40000 ALTER TABLE `Taxonomy` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `User`
--

DROP TABLE IF EXISTS `User`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `User` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(50) NOT NULL,
  `last_name` varchar(50) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(255) NOT NULL COMMENT 'Stores BCrypt hashed passwords',
  `is_certified` tinyint(1) DEFAULT 0,
  `last_login` timestamp NULL DEFAULT NULL,
  `password_reset_token` varchar(255) DEFAULT NULL,
  `password_reset_expires` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`user_id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `User`
--

LOCK TABLES `User` WRITE;
/*!40000 ALTER TABLE `User` DISABLE KEYS */;
INSERT INTO `User` VALUES (1,'Research','Lead','researcher_lead','89cdgpHSaBHvv2sNCWnZqwVW9jIRA1mJQyD8ZxfcYK4',1,NULL,NULL,NULL),(2,'Field','Scientist','field_sci1','$2b$12$a90a1322a55911ef99d4f7aa7138c32dRESET_REQUIRED_a5ac8a15-a53a-11ef-99d4-f7aa7138c32d',0,NULL,NULL,NULL),(3,'Lab','Technician','lab_tech1','$2b$12$a90a19afa55911ef99d4f7aa7138c32dRESET_REQUIRED_a5ac9065-a53a-11ef-99d4-f7aa7138c32d',1,NULL,NULL,NULL),(4,'Data','Analyst','data_analyst1','$2b$12$a90a1fdfa55911ef99d4f7aa7138c32dRESET_REQUIRED_a5ac9620-a53a-11ef-99d4-f7aa7138c32d',1,NULL,NULL,NULL),(5,'Wildlife','Observer','wildlife_obs1','$2b$12$a90a2609a55911ef99d4f7aa7138c32dRESET_REQUIRED_a5ac9b9c-a53a-11ef-99d4-f7aa7138c32d',0,NULL,NULL,NULL),(6,'Miguel','Lopez','mlopez','5RFVmneyvwtVYUyYnHHrq6WHRtV0pNldExzPvQNJW+A',1,NULL,NULL,NULL);
/*!40000 ALTER TABLE `User` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-11-22 13:37:14
