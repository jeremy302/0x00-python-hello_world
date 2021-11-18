-- queries db
SELECT title FROM tv_shows WHERE id NOT IN
(SELECT DISTINCT(tv_shows.id) AS id FROM tv_shows, tv_show_genres, tv_genres
WHERE tv_shows.id = tv_show_genres.show_id
AND tv_show_genres.genre_id = tv_genres.id AND tv_genres.name = 'Comedy')
ORDER BY title ASC;
