-- query db
SELECT tv_shows.title AS tile, tv_genres.name AS name FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = show_id
LEFT JOIN tv_genres ON tv_genres.id = genre_id
ORDER BY tv_shows.title ASC, tv_genres.name ASC;
