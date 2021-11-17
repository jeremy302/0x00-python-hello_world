-- queries db
SELECT tv_genres.name, sum(rate) AS rating FROM tv_genres
INNER JOIN tv_show_genres ON genre_id = tv_genres.id
INNER JOIN tv_show_ratings ON
tv_show_genres.show_id = tv_show_ratings.show_id
group by tv_genres.id
ORDER BY rating DESC;
