-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1:3306
-- Tiempo de generación: 22-12-2024 a las 23:03:33
-- Versión del servidor: 9.1.0
-- Versión de PHP: 8.3.14

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: acme
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla caja
--

DROP TABLE IF EXISTS caja;
CREATE TABLE IF NOT EXISTS caja (
  id int NOT NULL AUTO_INCREMENT,
  nombre varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish2_ci NOT NULL,
  estado int DEFAULT NULL,
  disponibilidad_pesos int NOT NULL,
  PRIMARY KEY (id)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish2_ci;

--
-- Volcado de datos para la tabla caja
--

INSERT INTO caja (id, nombre, estado, disponibilidad_pesos) VALUES
(3, 'Caja A', 0, 75000),
(2, 'Caja D', 1, 15000),
(4, 'Caja B', 1, 35000);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla moneda
--

DROP TABLE IF EXISTS moneda;
CREATE TABLE IF NOT EXISTS moneda (
  id int NOT NULL AUTO_INCREMENT,
  nombre varchar(50) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish2_ci NOT NULL,
  simbolo varchar(5) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish2_ci NOT NULL,
  tasa_conversion_id int NOT NULL,
  PRIMARY KEY (id),
  KEY fk_tasa_conversion (tasa_conversion_id)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish2_ci;

--
-- Volcado de datos para la tabla moneda
--

INSERT INTO moneda (id, nombre, simbolo, tasa_conversion_id) VALUES
(1, 'Dólar Estadounidense', '$', 1),
(2, 'Euro', '€', 2),
(3, 'Libra Esterlina', '£', 3),
(4, 'Yen Japonés', '¥', 4);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla tasa_conversion
--

DROP TABLE IF EXISTS tasa_conversion;
CREATE TABLE IF NOT EXISTS tasa_conversion (
  id int NOT NULL AUTO_INCREMENT,
  tipo_cambio int NOT NULL,
  PRIMARY KEY (id)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish2_ci;

--
-- Volcado de datos para la tabla tasa_conversion
--

INSERT INTO tasa_conversion (id, tipo_cambio) VALUES
(1, 850),
(2, 900),
(3, 1000),
(4, 7);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla transaccion
--

DROP TABLE IF EXISTS transaccion;
CREATE TABLE IF NOT EXISTS transaccion (
  id int NOT NULL AUTO_INCREMENT,
  cantidad int NOT NULL,
  monto_total float NOT NULL,
  ganancia float DEFAULT '0',
  moneda_id int NOT NULL,
  PRIMARY KEY (id),
  KEY fk_moneda (moneda_id)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish2_ci;

--
-- Volcado de datos para la tabla transaccion
--

INSERT INTO transaccion (id, cantidad, monto_total, ganancia, moneda_id) VALUES
(1, 100, 85000, 0, 1),
(2, 200, 17000, -163000, 2),
(3, 300, 25500, -274500, 3),
(4, 150, 12750, 11700, 4);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla usuario
--

DROP TABLE IF EXISTS usuario;
CREATE TABLE IF NOT EXISTS usuario (
  id int NOT NULL AUTO_INCREMENT,
  username varchar(50) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish2_ci DEFAULT NULL,
  password varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish2_ci DEFAULT NULL,
  rol enum('usuario','gerente') COLLATE utf8mb3_spanish2_ci NOT NULL,
  PRIMARY KEY (id)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish2_ci;

--
-- Volcado de datos para la tabla usuario
--

INSERT INTO usuario (id, username, password, rol) VALUES
(2, 'arn', '123', 'usuario'),
(3, 'anaguirv', '123', 'usuario'),
(4, 'gali', 'gali', 'gerente');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;