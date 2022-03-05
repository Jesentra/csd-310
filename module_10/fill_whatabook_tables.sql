-- Setting database
USE whatabook;

-- Filling book table
INSERT INTO book(book_id, book_name, author, details)
    VALUES
        (0001, 'The Scarlet Letter', 'Nathaniel Hawthorne'),
        (0002, 'The Hobbit', 'J.R.R. Tolkien'),
        (0003, 'Animal Farm', 'George Orwell'),
        (0004, 'Her Majesty''s Wizard', 'Christopher Stasheff'),
        (0005, 'The Silmarillion', 'J.R.R. Tolkien'),
        (0006, 'Learn German with Paul Noble', 'Paul Noble'),
        (0007, 'Cujo', 'Stephen King'),
        (0008, 'Goosebumps: Night of the Living Dummy', 'R.L. Stine'),
        (0009, 'Sherlock Holmes and the Hound of the Baskervilles', 'Arthur Conan Doyle');


-- Filling user table
INSERT INTO user(user_id, first_name, last_name)
    VALUES
        (0001, 'Sarah', 'Williams'),
        (0002, 'Michael', 'Smith'),
        (0003, 'Carrie', 'Tyson');

--Filling store table
INSERT INTO store(store_id, locale)
    VALUES(0001, '1234 East Street, Missoula, MT 59801');

-- Filling wishlist table
INSERT INTO wishlist(wishlist_id, user_id, book_id)
    VALUES 
        (0001, 0001, 0004),
        (0002, 0003, 0007),
        (0003, 0002, 0002);