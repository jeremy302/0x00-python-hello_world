-- query db
SELECT title, name FROM tv_shows LEFT JOIN tv_show_genres
ON show_id = tv_shows.id LEFT JOIN tv_genres ON tv_genres.id = genre_id
ORDER BY title ASC, name ASC;
