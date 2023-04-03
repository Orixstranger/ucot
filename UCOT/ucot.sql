-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 03-04-2023 a las 04:30:55
-- Versión del servidor: 10.4.25-MariaDB
-- Versión de PHP: 7.4.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `ucot`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `empleado`
--

CREATE TABLE `empleado` (
  `id` int(11) NOT NULL,
  `codigo` int(10) NOT NULL,
  `nombre` varchar(30) NOT NULL,
  `apellido` varchar(30) NOT NULL,
  `cedula` varchar(10) NOT NULL,
  `edad` varchar(3) NOT NULL,
  `telefono` varchar(10) NOT NULL,
  `correo_electronico` varchar(30) NOT NULL,
  `localidad` varchar(60) NOT NULL,
  `estado` varchar(60) NOT NULL,
  `reconocimientos` varchar(60) NOT NULL,
  `sanciones` varchar(60) NOT NULL,
  `c1` varchar(60) NOT NULL,
  `c2` varchar(60) NOT NULL,
  `fotografia` varchar(5000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `empleado`
--

INSERT INTO `empleado` (`id`, `codigo`, `nombre`, `apellido`, `cedula`, `edad`, `telefono`, `correo_electronico`, `localidad`, `estado`, `reconocimientos`, `sanciones`, `c1`, `c2`, `fotografia`) VALUES
(8, 1, 'Victoria', 'Torres', '1111111112', '23', '0900000000', 'victoria.torres@loja.gob.ec', 'Loja', 'Pasivo', 'si', 'si', 'asd', 'asd', '20220848051663766682231.jpeg'),
(9, 2, 'Juan', 'Idrobo', '1111111110', '22', '0999999999', 'juan.idrobo@loja.gob.ec', 'Loja', 'Activo', 'si', 'no', 'asd', 'asd', '20220851251663766682126.jpg'),
(10, 3, 'Alex', 'Abad', '1111111111', '25', '0900000000', 'alex.abad@loja.gob.ec', 'Loja', 'Activo', 'si', 'no', 'asd', 'asd', '2022085539LOJA CIUDAD A0 2_page-0001.jpg'),
(11, 4, 'Ana', 'Lojan', '1111111113', '22', '0900000000', 'ana.lojan@loja.gob.ec', 'Loja', 'Pasivo', 'si', 'no', 'asd', 'asd', '2022090718WhatsApp Image 2022-04-21 at 7.19.42 AM.jpeg');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `user`
--

CREATE TABLE `user` (
  `id` smallint(3) UNSIGNED NOT NULL,
  `username` varchar(20) NOT NULL,
  `password` char(102) NOT NULL,
  `fullname` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `user`
--

INSERT INTO `user` (`id`, `username`, `password`, `fullname`) VALUES
(1, 'pbenitez', 'pbkdf2:sha256:260000$yXOgHVwlb1ilfn1N$8e96ca55576aeb04ec02ee20d90fb6463cbea5de13798eed2caadb9ac159662c', 'PATRICIO BOLIVAR BENITEZ LANCHE'),
(2, 'byron', 'pbkdf2:sha256:260000$nGhuRnTHhoxfaWtv$38ea9ba2787a6d7a47824beb1eb3b0e751a1dbe4b2e2c6e26f1064f7adfa8f5f', 'BYRON MONTAÑO');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `empleado`
--
ALTER TABLE `empleado`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `empleado`
--
ALTER TABLE `empleado`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT de la tabla `user`
--
ALTER TABLE `user`
  MODIFY `id` smallint(3) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
