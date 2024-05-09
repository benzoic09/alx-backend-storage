-- SQL script to create a stored procedure ComputeAverageWeightedScoreForUser
DELIMITER $$

DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;
CREATE PROCEDURE ComputeAverageWeightedScoreForUser (IN user_id INT)
BEGIN
	-- Compute the average weighted score for the user
	UPDATE users SET average_score = (SELECT
	SELECT SUM(corrections.score * projects.weight) / SUM(projects.weight)
	FROM corrections
	INNER JOIN projects
	ON projects.id = corrections.project_id
	WHERE corrections.user_id = user_id)
	WHERE users.id = user_id;
END $$
DELIMITER ;

