-- averages temperatures from july to august by city. shows top 3
-- group by `city` and average records
SELECT city, AVG(value) as avg_temp from temperatures WHERE month BETWEEN 7 AND 8 GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
