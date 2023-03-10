-- creating a table users with specified requirements
CREATE INDEX idx_name_first_score ON names (name(1), score);