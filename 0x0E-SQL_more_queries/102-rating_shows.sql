-- queries db
SELECT title, SUM(rate) AS rating FROM tv_show_ratings
INNER JOIN tv_shows ON show_id = tv_shows.id
GROUP BY show_id
ORDER BY rating DESC;
