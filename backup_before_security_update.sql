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
  `password` varchar(255) NOT NULL,
  PRIMARY KEY (`admin_id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Admin`
--

LOCK TABLES `Admin` WRITE;
/*!40000 ALTER TABLE `Admin` DISABLE KEYS */;
INSERT INTO `Admin` VALUES (1,'Admin','User1','AdminUser1','password1'),(2,'Admin','User2','AdminUser2','password2'),(3,'Admin','User3','AdminUser3','password3'),(4,'Admin','User4','AdminUser4','password4'),(5,'Admin','User5','AdminUser5','password5');
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
  `password` varchar(255) NOT NULL,
  `is_certified` tinyint(1) DEFAULT 0,
  PRIMARY KEY (`user_id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `User`
--

LOCK TABLES `User` WRITE;
/*!40000 ALTER TABLE `User` DISABLE KEYS */;
INSERT INTO `User` VALUES (1,'Alice','Smith','asmith','password1',1),(2,'Bob','Ross','bross','password2',0),(3,'Charlie','Brown','cbrown','password3',1),(4,'Dana','White','dwhite','password4',1),(5,'P','Diddy','pdiddy','password5',0);
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

-- Dump completed on 2024-11-21 15:51:24
