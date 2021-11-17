-- queries db
SELECT tv_genres.name AS name FROM tv_shows
INNER JOIN tv_show_genres ON tv_shows.title='Dexter' AND show_id = tv_shows.id
INNER JOIN tv_genres ON tv_genres.id=genre_id
ORDER BY tv_genres.name ASC;
