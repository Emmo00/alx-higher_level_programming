-- list all comedy shows
SELECT tv_shows.title
FROM tv_show_genres
JOIN tv_genres
ON tv_genres.id = tv_show_genres.genre_id
JOIN tv_shows on tv_show_genres.show_id = tv_shows.id
WHERE tv_genres.name  = 'Comedy'
ORDER BY tv_shows.title ASC;
