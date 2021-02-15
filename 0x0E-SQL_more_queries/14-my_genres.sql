-- Write a script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.

    -- The tv_shows table contains only one record where title = Dexter (but the id can be different)
    -- Each record should display: tv_genres.name
    -- Results must be sorted in ascending order by the genre name
    -- You can use only one SELECT statement
    -- The database name will be passed as an argument of the mysql command

SELECT name FROM tv_show_genres
INNER JOIN tv_genres
ON tv_show_genres.genre_id = tv_genres.id
WHERE show_id =
(
SELECT id FROM tv_shows
WHERE title = "Dexter"
)
ORDER BY name ASC;
