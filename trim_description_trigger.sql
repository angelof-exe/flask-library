DELIMITER //

CREATE TRIGGER before_insert_example_table
BEFORE INSERT ON library.book
FOR EACH ROW
BEGIN
    IF CHAR_LENGTH(NEW.`bookdescription`) > 500 THEN
        SET NEW.`bookdescription` = LEFT(NEW.`bookdescription`, 500);
    END IF;
END //

DELIMITER ;
