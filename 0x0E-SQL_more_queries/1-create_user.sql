-- This script creates a SQL server called user_0d_1
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT ALL PRIVILEGES ON * . * TO 'user_0d_1'@'localhost';
GRANT ALL PRIVILEGES ON * . * TO 'user_0d_2'@'localhost';
