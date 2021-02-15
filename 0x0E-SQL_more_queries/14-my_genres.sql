-- Write a script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
    -- The tv_shows table contains only one record where title = Dexter (but the id can be different)
    -- Each record should display: tv_genres.name
    -- Results must be sorted in ascending order by the genre name
    -- You can use only one SELECT statement
    -- The database name will be passed as an argument of the mysql command

SELECT name FROM tv_show_genres tsg
INNER JOIN tv_genres tg
ON tsg.genre_id = tg.id
   INNER JOIN tv_shows ts
   ON tsg.show_id = ts.id
WHERE title = 'Dexter'
ORDER BY name ASC;
