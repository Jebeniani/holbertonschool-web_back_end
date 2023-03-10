-- creating a table users with specified requirements
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUser (IN p_user_id INT)
BEGIN
    DECLARE total_score FLOAT;
    DECLARE total_weight FLOAT;
    DECLARE avg_score FLOAT;

    SELECT SUM(score * weight) INTO total_score
    FROM corrections
    WHERE user_id = p_user_id;

    SELECT SUM(weight) INTO total_weight
    FROM corrections
    WHERE user_id = p_user_id;

    SET avg_score = total_score / total_weight;

    UPDATE users
    SET avg_weighted_score = avg_score
    WHERE id = p_user_id;
END
$$