-- creating a table users with specified requirements
CREATE VIEW need_meeting AS
SELECT name FROM students WHERE score < 80 AND last_meeting IS NULL OR last_meeting < date_sub(now(), interval 1 month)
