USE whatabook;

DROP USER if EXISTS 'whatabook_user'@'localhost';

CREATE user 'whatabook_user'@'localhost' IDENTIFIED with mysql_native_password by 'MySQL8IsGreat!';

GRANT ALL PRIVILEGES ON whatabook.* TO 'whatabook_user'@'localhost';