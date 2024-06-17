-- a sql script that create a procedure that computer the average score for a student
-- Drop the procedure if it already exists
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;

-- Change the delimiter to $$
DELIMITER $$

-- Create the stored procedure
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    DECLARE average_score FLOAT;
    
    -- Compute the average for a student
    SET average_score = (SELECT AVG(score) FROM corrections WHERE corrections.user_id = user_id);
    
    -- Update user's average score
    UPDATE users SET average_score = average_score WHERE id = user_id;
END$$

-- Reset the delimiter back to ;
DELIMITER ;
