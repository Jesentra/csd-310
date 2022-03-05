-- Set database to whatabook
USE whatabook;

-- Dropping Tables if they exist
DROP TABLE IF EXISTS user, wishlist, book, store;

-- Creating user table
CREATE TABLE user (
    user_id     INT             NOT NULL    AUTO_INCREMENT,
    first_name  VARCHAR(75)     NOT NULL,
    last_name   VARCHAR(75)     NOT NULL,
    PRIMARY KEY(user_id)
);

-- Creating book table
CREATE TABLE book (
    book_id     INT             NOT NULL    AUTO_INCREMENT,
    book_name   VARCHAR(200)    NOT NULL,
    details     VARCHAR(500),
    author      VARCHAR(200)    NOT NULL,
    PRIMARY KEY(book_id)
);

-- Creating wishlist table
CREATE TABLE wishlist(
    wishlist_id INT     NOT NULL    AUTO_INCREMENT,
    user_id     INT     NOT NULL,
    book_id     INT     NOT NULL,
    PRIMARY KEY(wishlist_id),
    CONSTRAINT fk_user_wish
        FOREIGN KEY(user_id) REFERENCES user(user_id),
    CONSTRAINT fk_wish_book
        FOREIGN KEY(book_id) REFERENCES book(book_id)
);

-- Creating store table
CREATE TABLE store(
    store_id    INT             NOT NULL,
    locale      VARCHAR(500)    NOT NULL
);