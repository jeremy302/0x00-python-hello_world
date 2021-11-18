-- queries db
SELECT name FROM tv_genres WHERE id NOT IN
(SELECT genre_id FROM tv_shows
INNER JOIN tv_show_genres ON tv_shows.title = 'Dexter'
AND tv_shows.id = tv_show_genres.show_id)
ORDER BY  name ASC;
