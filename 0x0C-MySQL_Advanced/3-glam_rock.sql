-- creating a table users with specified requirements
SELECT band_name, IFNULL(split, 2020) - formed as lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%';
