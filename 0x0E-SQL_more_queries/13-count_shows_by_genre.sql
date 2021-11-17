-- queries db
SELECT name AS genre, COUNT(*) AS number_of_shows FROM tv_genres
INNER JOIN tv_show_genres ON tv_genres.id = genre_id
GROUP BY tv_genres.id
ORDER BY number_of_shows DESC;
