SELECT 
	c.name AS country,
    region,
    life_expectancy AS life_exp
FROM countries AS c
-- Join to populations (alias as p) using an appropriate join
CROSS JOIN populations AS p 
ON c.code = p.country_code
-- Filter for only results in the year 2010
WHERE year IN 2010
-- Sort by life_exp
ORDER BY life_exp ASC
-- Limit to five records
LIMIT 5;