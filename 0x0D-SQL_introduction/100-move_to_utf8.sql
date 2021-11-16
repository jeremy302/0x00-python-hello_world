-- converts database to utf 8
-- convert db
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
-- switch db
USE hbtn_0c_0;
-- converts table
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
