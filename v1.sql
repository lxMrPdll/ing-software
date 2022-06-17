-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 02, 2022 at 08:51 AM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `v1`
--

-- --------------------------------------------------------

--
-- Table structure for table `tbl_pacientes`
--

CREATE TABLE `tbl_pacientes` (
  `id` int(11) NOT NULL,
  `nombre` varchar(30) NOT NULL,
  `paterno` varchar(30) NOT NULL,
  `materno` varchar(30) NOT NULL,
  `nacimiento` date NOT NULL,
  `sexo` varchar(10) NOT NULL,
  `telefono` varchar(30) NOT NULL,
  `email` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tbl_pacientes`
--

INSERT INTO `tbl_pacientes` (`id`, `nombre`, `paterno`, `materno`, `nacimiento`, `sexo`, `telefono`, `email`) VALUES
(1, 'Alejandro', 'Mora', 'Padilla', '2000-02-25', 'Hombre', '666', 'alejandroomora@gmail.com'),
(2, 'Juan', 'Pacheco', 'Melendez', '2005-10-31', 'Hombre', 'Esto debe ser un numero', 'aogweoutgwoeiu@gmail.com'),
(13, 'Mario', 'el Money', 'Castañeda', '1962-06-29', 'Hombre', '663-327-1864', 'aogweoutgwoeiu@gmail.com'),
(25, 'Alejandro', 'Mora', 'Padilla', '2000-02-25', 'Hombre', '663-327-1863', 'alejandroomora@gmail.com');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_rol`
--

CREATE TABLE `tbl_rol` (
  `id` int(11) NOT NULL,
  `rol` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `tbl_rol`
--

INSERT INTO `tbl_rol` (`id`, `rol`) VALUES
(1, 'admin'),
(2, 'dentista');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_usuarios`
--

CREATE TABLE `tbl_usuarios` (
  `id` int(11) NOT NULL,
  `nombre` varchar(20) NOT NULL,
  `paterno` varchar(20) NOT NULL,
  `materno` varchar(20) NOT NULL,
  `nacimiento` date NOT NULL,
  `sexo` varchar(50) NOT NULL,
  `telefono` varchar(20) NOT NULL,
  `email` varchar(30) NOT NULL,
  `id_rol` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `tbl_usuarios`
--

INSERT INTO `tbl_usuarios` (`id`, `nombre`, `paterno`, `materno`, `nacimiento`, `sexo`, `telefono`, `email`, `id_rol`) VALUES
(2, 'Alejandro', 'Mora', 'Padilla', '2000-02-25', 'Hombre', 'Esto debe ser un num', 'alejandroomora@gmail.com', 2),
(3, 'Alejandro', 'Mora', 'Padilla', '2000-02-25', 'Hombre', '663-327-1863', 'alejandroomora@gmail.com', 2),
(4, 'Alejandro', 'Mora', 'Padilla', '2000-02-25', 'Hombre', '663-327-1864', 'alejandroomora@gmail.com', 2),
(8, 'Alejandro', 'Mora', 'Padilla', '2000-02-25', 'Hombre', 'Esto debe ser un num', 'alejandroomora@gmail.com', 2);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `tbl_pacientes`
--
ALTER TABLE `tbl_pacientes`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `tbl_rol`
--
ALTER TABLE `tbl_rol`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `tbl_usuarios`
--
ALTER TABLE `tbl_usuarios`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_rol` (`id_rol`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `tbl_pacientes`
--
ALTER TABLE `tbl_pacientes`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- AUTO_INCREMENT for table `tbl_rol`
--
ALTER TABLE `tbl_rol`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `tbl_usuarios`
--
ALTER TABLE `tbl_usuarios`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `tbl_usuarios`
--
ALTER TABLE `tbl_usuarios`
  ADD CONSTRAINT `tbl_usuarios_ibfk_1` FOREIGN KEY (`id_rol`) REFERENCES `tbl_rol` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
