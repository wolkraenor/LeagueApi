USE `League`;

DROP TABLE IF EXISTS

Users;

CREATE TABLE `Users` (
`id` int(100) NOT NULL,
`fullname` varchar(100) NOT NULL,
`username` varchar(100) NOT NULL,
`country` varchar(100) NOT NULL,
`password` int(16) NOT NULL,
PRIMARY KEY (`id`),
KEY `idx_fullname` (`fullname`),
KEY `idx_username` (`username`),
KEY `idx_country` (`country`),
KEY `idx_password` (`password`),
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
