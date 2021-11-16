-- queries for max temperatures by state, ordered by state
-- max temperatures by states
SELECT state, MAX(value) as max_temp from temperatures GROUP BY state ORDER BY state ASC;
