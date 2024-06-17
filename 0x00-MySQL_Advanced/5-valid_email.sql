-- a triggger that resets the attribute
DELIMITER $$
CREATE TRIGGER reset_valid_email
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    If New.email <> OLD.email then
        SET NEW.valid_email = 0;
    END IF;
END$$

DELIMITER ;