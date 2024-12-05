-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 05, 2024 at 01:45 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `db_pekerjaan`
--

-- --------------------------------------------------------

--
-- Table structure for table `daftar_pelamar`
--

CREATE TABLE `daftar_pelamar` (
  `id` int(11) NOT NULL,
  `nama` varchar(256) NOT NULL,
  `email` varchar(256) NOT NULL,
  `pendidikan` text NOT NULL,
  `pekerjaan_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `daftar_pelamar`
--

INSERT INTO `daftar_pelamar` (`id`, `nama`, `email`, `pendidikan`, `pekerjaan_id`) VALUES
(1, 'andi', 'akun@mail.com', 'S1 Informatika', 1),
(2, 'rizky', 'admin@123.com', 'S2 informatika', 2);

-- --------------------------------------------------------

--
-- Table structure for table `pekerjaan`
--

CREATE TABLE `pekerjaan` (
  `id` int(11) NOT NULL,
  `Perusahaan` varchar(256) NOT NULL,
  `description` text NOT NULL,
  `requirement` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `pekerjaan`
--

INSERT INTO `pekerjaan` (`id`, `Perusahaan`, `description`, `requirement`) VALUES
(1, 'Perusahaan a', 'perusahaan tentang restoran', 'koki , memasak'),
(2, 'Perusahaan B', 'Perusahaan tentang software', 'software enginerr , programmer'),
(3, 'Perusahaan C', 'Perusahaan tentang Otomotif', 'bengkel , otomotif  '),
(4, 'Perusahaan D', 'ini perusahaan transportasi', 'dibutuhkan supir yang berpengalaman');

-- --------------------------------------------------------

--
-- Table structure for table `user_data`
--

CREATE TABLE `user_data` (
  `id` int(11) NOT NULL,
  `name` varchar(256) NOT NULL,
  `experience` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `user_data`
--

INSERT INTO `user_data` (`id`, `name`, `experience`) VALUES
(14, 'ZUHAIRAHNAF', 'programmer'),
(15, 'ZUHAIRAHNAF', 'koki');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `daftar_pelamar`
--
ALTER TABLE `daftar_pelamar`
  ADD PRIMARY KEY (`id`),
  ADD KEY `pekerjaan_id` (`pekerjaan_id`);

--
-- Indexes for table `pekerjaan`
--
ALTER TABLE `pekerjaan`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user_data`
--
ALTER TABLE `user_data`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `daftar_pelamar`
--
ALTER TABLE `daftar_pelamar`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `pekerjaan`
--
ALTER TABLE `pekerjaan`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `user_data`
--
ALTER TABLE `user_data`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `daftar_pelamar`
--
ALTER TABLE `daftar_pelamar`
  ADD CONSTRAINT `daftar_pelamar_ibfk_1` FOREIGN KEY (`pekerjaan_id`) REFERENCES `pekerjaan` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
