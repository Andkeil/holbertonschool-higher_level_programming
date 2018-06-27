-- Script display number of shows by genre
SELECT tv_genres.name AS genre, COUNT(tv_show_genres.genre_id) AS number_shows
FROM tv_genres JOIN tv_show_genres WHERE tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_show_genres.genre_id ORDER BY number_shows DESC;
