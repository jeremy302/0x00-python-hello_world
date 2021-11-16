-- queries for max temperatures by state, ordered by state
-- max temperatures by states
SELECT state, MAX(value) AS max_temp FROM temperatures GROUP BY state ORDER BY state ASC;
