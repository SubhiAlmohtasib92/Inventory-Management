-- phpMyAdmin SQL Dump
-- version 5.0.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 07, 2021 at 09:46 AM
-- Server version: 10.4.14-MariaDB
-- PHP Version: 7.2.34

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `inventory_management`
--

DELIMITER $$
--
-- Procedures
--
CREATE DEFINER=`root`@`localhost` PROCEDURE `GetTotals` ()  BEGIN
   
   CREATE TEMPORARY TABLE tempvalues as 
select
   * 
from
   (
      SELECT
(
         select
            productname 
         from
            product p 
         where
            p.product_id = pm.productiD) as 'ProductName',
            ifnull( (
            select
               locationname 
            from
               location l 
            where
               l.location_id = pm.from_location), 'None') 'Locationname',
               cast(ifnull(sum(qty),0) as int) as 'val' 
            from
               productmovement pm 
            GROUP by
               productiD,
               from_location
   )
   A;
SET
   @sql = NULL;
SELECT
   GROUP_CONCAT(DISTINCT CONCAT( 'ifnull(max(case when Locationname = ''', Locationname, ''' then ifnull(val,0) end),0)  ' , Locationname)) INTO @sql 
FROM
   tempvalues;
SET
   @sql = CONCAT('SELECT productname as ProductName, ', @sql, ' FROM tempvalues GROUP BY productname');
PREPARE stmt 
FROM
   @sql;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;
DROP TABLE if EXISTS tempvalues;
END$$

DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `location`
--

CREATE TABLE `location` (
  `Location_id` varchar(200) NOT NULL,
  `LocationName` varchar(100) NOT NULL,
  `AddDate` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `location`
--

INSERT INTO `location` (`Location_id`, `LocationName`, `AddDate`) VALUES
('284a38b6-1878-41fd-b6c6-d830d7249f36', 'Jordan', '2021-01-04 09:12:16'),
('3f44b858-9e21-4291-934d-1472fa8b996c', 'Palestine', '2021-01-04 09:11:39'),
('5f4345fa-6809-44f6-91d9-5130620c75f1', 'Canada', '2021-01-04 09:12:26'),
('7efc2b92-b899-46f1-80cc-e158227fc854', 'USA', '2021-01-04 09:12:20');

-- --------------------------------------------------------

--
-- Table structure for table `product`
--

CREATE TABLE `product` (
  `product_id` varchar(200) NOT NULL,
  `ProductName` varchar(100) NOT NULL,
  `Quantity` int(11) NOT NULL,
  `AddDate` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `product`
--

INSERT INTO `product` (`product_id`, `ProductName`, `Quantity`, `AddDate`) VALUES
('34e31687-9bc9-479a-9319-509c55d7aba3', 'Tablet', 5, '2021-01-06 11:15:11'),
('5004bb5a-5e81-4451-81c7-93da1655d278', 'Dell', 20, '2021-01-04 09:10:22'),
('6a0eb88e-46bc-4680-b1df-e29d74fb6a1b', 'Toshiba', 30, '2021-01-04 09:10:33'),
('cf504895-5997-4968-8a32-2f81332730db', 'IPhone', 10, '2021-01-04 09:09:17'),
('dfa093ba-1f70-46a7-9b58-96789be0cd74', 'Nokia', 15, '2021-01-04 09:10:10');

-- --------------------------------------------------------

--
-- Table structure for table `productmovement`
--

CREATE TABLE `productmovement` (
  `MovementId` varchar(200) NOT NULL,
  `timestamp` timestamp NOT NULL DEFAULT current_timestamp(),
  `from_location` varchar(200) NOT NULL,
  `to_location` varchar(200) NOT NULL,
  `productiD` varchar(200) NOT NULL,
  `qty` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `productmovement`
--

INSERT INTO `productmovement` (`MovementId`, `timestamp`, `from_location`, `to_location`, `productiD`, `qty`) VALUES
('37d20733-cb1a-4fab-9e7a-5bf50c7aaf6c', '2021-01-07 06:10:44', '5f4345fa-6809-44f6-91d9-5130620c75f1', '3f44b858-9e21-4291-934d-1472fa8b996c', '5004bb5a-5e81-4451-81c7-93da1655d278', 3),
('46a15e39-d335-44ff-9ae4-b7140efacab6', '2021-01-07 08:15:28', '284a38b6-1878-41fd-b6c6-d830d7249f36', '3f44b858-9e21-4291-934d-1472fa8b996c', '5004bb5a-5e81-4451-81c7-93da1655d278', 1),
('53c5c681-097a-4bc8-ab57-270fcddae846', '2021-01-07 05:15:03', '7efc2b92-b899-46f1-80cc-e158227fc854', '3f44b858-9e21-4291-934d-1472fa8b996c', '5004bb5a-5e81-4451-81c7-93da1655d278', 10),
('73cd0323-558c-4cd2-97a6-b47dbcf3d5f2', '2021-01-06 11:12:05', '3f44b858-9e21-4291-934d-1472fa8b996c', '284a38b6-1878-41fd-b6c6-d830d7249f36', '34e31687-9bc9-479a-9319-509c55d7aba3', 1),
('7b46b12b-7702-492e-a4f3-4493dd5da0e0', '2021-01-07 05:15:13', '5f4345fa-6809-44f6-91d9-5130620c75f1', '3f44b858-9e21-4291-934d-1472fa8b996c', '5004bb5a-5e81-4451-81c7-93da1655d278', 20);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `location`
--
ALTER TABLE `location`
  ADD PRIMARY KEY (`Location_id`);

--
-- Indexes for table `product`
--
ALTER TABLE `product`
  ADD PRIMARY KEY (`product_id`);

--
-- Indexes for table `productmovement`
--
ALTER TABLE `productmovement`
  ADD PRIMARY KEY (`MovementId`),
  ADD KEY `FK_Movement_Location2` (`to_location`),
  ADD KEY `FK_Movement_Product` (`productiD`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `productmovement`
--
ALTER TABLE `productmovement`
  ADD CONSTRAINT `FK_Movement_Location2` FOREIGN KEY (`to_location`) REFERENCES `location` (`Location_id`),
  ADD CONSTRAINT `FK_Movement_Product` FOREIGN KEY (`productiD`) REFERENCES `product` (`product_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
