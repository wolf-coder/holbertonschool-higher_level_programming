-- Write a script that lists all Comedy shows in the database hbtn_0d_tvshows.

    -- The tv_genres table contains only one record where name = Comedy (but the id can be different)
    -- Each record should display: tv_shows.title
    -- Results must be sorted in ascending order by the show title
    -- You can use only one SELECT statement
    -- The database name will be passed as an argument of the mysql command

SELECT title FROM tv_show_genres tvg
INNER JOIN tv_genres tg
ON tvg.genre_id = tg.id
   INNER JOIN tv_shows ts
   ON tvg.show_id = ts.id
WHERE name = 'Comedy'
ORDER BY title ASC;
