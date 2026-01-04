/*
Navicat MySQL Data Transfer

Source Server         : admin
Source Server Version : 50721
Source Host           : localhost:3306
Source Database       : mydata

Target Server Type    : MYSQL
Target Server Version : 50721
File Encoding         : 65001

Date: 2019-12-25 16:49:39
*/

SET FOREIGN_KEY_CHECKS=0;
-- ----------------------------
-- Table structure for `admin_basic`
-- ----------------------------
DROP TABLE IF EXISTS `admin_basic`;
CREATE TABLE `admin_basic` (
  `name` varchar(255) NOT NULL,
  `birthday` date NOT NULL,
  `sex` varchar(255) NOT NULL,
  `mail` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  PRIMARY KEY (`mail`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of admin_basic
-- ----------------------------
INSERT INTO admin_basic VALUES ('王樺立', '1999-09-30', '男', '4444@gmail.com', '0000');
INSERT INTO admin_basic VALUES ('tt', '2019-12-01', '女', 'girls@gir.com', '1234');
INSERT INTO admin_basic VALUES ('HTHT', '2019-12-25', '女', 'THTH@GRTH.com', '1256');
INSERT INTO admin_basic VALUES ('Lu Liang Chin', '1999-10-25', '男', 'ttsmcpe@gmail.com', '123');

-- ----------------------------
-- Table structure for `collect_good`
-- ----------------------------
DROP TABLE IF EXISTS `collect_good`;
CREATE TABLE `collect_good` (
  `admin_mail` varchar(225) NOT NULL,
  `good_id` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of collect_good
-- ----------------------------
INSERT INTO collect_good VALUES ('ttsmcpe@gmail.com', '2');

-- ----------------------------
-- Table structure for `goods`
-- ----------------------------
DROP TABLE IF EXISTS `goods`;
CREATE TABLE `goods` (
  `name` varchar(255) DEFAULT NULL,
  `en_name` varchar(255) DEFAULT NULL,
  `image` varchar(255) DEFAULT NULL,
  `weblink` varchar(255) DEFAULT NULL,
  `id_number` int(11) NOT NULL,
  PRIMARY KEY (`id_number`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of goods
-- ----------------------------
INSERT INTO goods VALUES ('姍姍', 'ShanShan', 'g1.jpg', 'person1.jsp', '1');
INSERT INTO goods VALUES ('酥酥', 'SuSu', 'g2.jpg', 'person2.jsp', '2');
INSERT INTO goods VALUES ('亞亞', 'YaYa', 'g3.jpg', 'person3.jsp', '3');
INSERT INTO goods VALUES ('小明', 'Min', 'b1.jpg', 'person4.jsp', '4');
INSERT INTO goods VALUES ('阿翰', 'Han', 'b2.jpg', 'person5.jsp', '5');
INSERT INTO goods VALUES ('小暉', 'Hui', 'b3.jpg', 'person6.jsp', '6');

-- ----------------------------
-- Table structure for `manage_broad`
-- ----------------------------
DROP TABLE IF EXISTS `manage_broad`;
CREATE TABLE `manage_broad` (
  `name` varchar(255) DEFAULT NULL,
  `phone` varchar(255) DEFAULT NULL,
  `mail` varchar(255) DEFAULT NULL,
  `msg` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of manage_broad
-- ----------------------------
INSERT INTO manage_broad VALUES ('tt', '0939741089', '8888@dfgg.com', '你好');

-- ----------------------------
-- Table structure for `mannger_id`
-- ----------------------------
DROP TABLE IF EXISTS `mannger_id`;
CREATE TABLE `mannger_id` (
  `user_id` varchar(255) NOT NULL,
  `password` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of mannger_id
-- ----------------------------

-- ----------------------------
-- Table structure for `msg_broad`
-- ----------------------------
DROP TABLE IF EXISTS `msg_broad`;
CREATE TABLE `msg_broad` (
  `user_mail` varchar(255) NOT NULL,
  `msg` varchar(255) DEFAULT NULL,
  `good_id` varchar(11) DEFAULT NULL,
  `star` int(11) DEFAULT NULL,
  `time` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of msg_broad
-- ----------------------------
INSERT INTO msg_broad VALUES ('ttsmcpe@gmail.com', 'OK', '5', '5', '2019-12-21');
INSERT INTO msg_broad VALUES ('ttsmcpe@gmail.com', 'AWSOME', '6', '3', '2019-12-21');
INSERT INTO msg_broad VALUES ('ttsmcpe@gmail.com', 'NICE', '2', '4', '2019-12-21');
INSERT INTO msg_broad VALUES ('ttsmcpe@gmail.com', 'I LIKE ', '3', '5', '2019-12-21');
INSERT INTO msg_broad VALUES ('ttsmcpe@gmail.com', 'Love U', '4', '5', '2019-12-21');
INSERT INTO msg_broad VALUES ('ttsmcpe@gmail.com', 'GOOD', '1', '4', '2019-12-21');
INSERT INTO msg_broad VALUES ('ttsmcpe@gmail.com', 'Hight', '1', '5', '2019-12-21');

-- ----------------------------
-- Table structure for `record`
-- ----------------------------
DROP TABLE IF EXISTS `record`;
CREATE TABLE `record` (
  `admin_id` varchar(255) DEFAULT NULL,
  `good_id` varchar(255) DEFAULT NULL,
  `time` date DEFAULT NULL,
  `other_thing` varchar(255) DEFAULT NULL,
  `buy_msg` varchar(255) DEFAULT NULL,
  `bank_book` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of record
-- ----------------------------
INSERT INTO record VALUES ('ttsmcpe@gmail.com', '1', '2019-12-25', ' <br>開車接送 1km <br>送束花 幾隻玫瑰  1份 <br>自送禮物 多少錢 1份(一份100元)', '55353', '1234567898');
INSERT INTO record VALUES ('ttsmcpe@gmail.com', '1', '2019-12-19', '', '123123', '1234567898');
INSERT INTO record VALUES ('ttsmcpe@gmail.com', '3', '2019-12-25', '', '', '1234567898');
INSERT INTO record VALUES ('ttsmcpe@gmail.com', '3', '2019-12-25', '', '', '1234567898');
INSERT INTO record VALUES ('ttsmcpe@gmail.com', '1', '2019-12-25', ' <br>送束花 幾隻玫瑰  2份', '', '1234567898');
INSERT INTO record VALUES ('ttsmcpe@gmail.com', '1', '2019-12-25', '', '', '1234567898');
INSERT INTO record VALUES ('ttsmcpe@gmail.com', '1', '2019-12-25', '', '', '1234567898');
INSERT INTO record VALUES ('ttsmcpe@gmail.com', '1', '2019-12-25', ' <br>自送禮物 多少錢 1份(一份100元)', '', '1234567898');
INSERT INTO record VALUES ('ttsmcpe@gmail.com', '1', '2019-12-26', ' <br>自送禮物 多少錢 5份(一份100元)', '456', '1234567898');

-- ----------------------------
-- Table structure for `shoppingcart`
-- ----------------------------
DROP TABLE IF EXISTS `shoppingcart`;
CREATE TABLE `shoppingcart` (
  `user_mail` varchar(255) DEFAULT NULL,
  `good_id` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of shoppingcart
-- ----------------------------
