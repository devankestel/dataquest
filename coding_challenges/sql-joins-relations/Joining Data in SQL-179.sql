## 1. Introducing Joins ##

SELECT * 
FROM facts
INNER JOIN cities ON cities.facts_id = facts.id
LIMIT 10;

## 2. Understanding Inner Joins ##

SELECT c.*, f.name AS country_name 
FROM facts f
INNER JOIN cities c ON f.id = c.facts_id
LIMIT 5;

## 3. Practicing Inner Joins ##

SELECT f.name AS country, c.name AS capital_city 
FROM facts f
INNER JOIN cities c ON f.id = c.facts_id
WHERE c.capital = 1;

## 4. Left Joins ##

SELECT f.name as country,
f.population
FROM facts f
LEFT JOIN cities c on c.facts_id = f.id
WHERE c.facts_id IS NULL;

## 6. Finding the Most Populous Capital Cities ##

SELECT c.name as capital_city, f.name as country, 
c.population
FROM cities c
INNER JOIN facts f on f.id = c.facts_id
WHERE c.capital = 1
ORDER BY c.population DESC
LIMIT 10;

## 7. Combining Joins with Subqueries ##

SELECT c.name as capital_city,
f.name as country,
c.population
FROM facts f 
INNER JOIN (
    SELECT * FROM cities
    WHERE population > 10000000
    AND capital = 1
) c ON c.facts_id = f.id 
ORDER BY c.population DESC;

## 8. Challenge: Complex Query with Joins and Subqueries ##

SELECT f.name AS country,
c.urban_pop,
f.population as total_pop,
(c.urban_pop / CAST(f.population AS FLOAT)) urban_pct
FROM facts f
INNER JOIN 
(SELECT SUM(population) urban_pop,
 facts_id
 FROM cities
 GROUP BY facts_id) c ON c.facts_id = f.id
 WHERE urban_pct > 0.5
 ORDER BY urban_pct ASC;