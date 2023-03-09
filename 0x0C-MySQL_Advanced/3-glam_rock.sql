-- creating a table users with specified requirements
-- is it possible to
SELECT `band_name`, IFNULL(`split`, 2020) - IFNULL(formed, 0) as `lifespan`
FROM `metal_bands` WHERE FIND_IN_SET('Glam rock', style);