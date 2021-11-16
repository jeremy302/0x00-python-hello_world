-- tallies `score` of rows
-- group query
SELECT score, count(*) as number FROM second_table GROUP BY score ORDER BY number DESC;
