-- Write a script that lists all shows without the genre Comedy in the database hbtn_0d_tvshows.

    -- The tv_genres table contains only one record where name = Comedy (but the id can be different)
    -- Each record should display: tv_shows.title
    -- Results must be sorted in ascending order by the show title
    -- You can use a maximum of two SELECT statement
    -- The database name will be passed as an argument of the mysql command.

SELECT DISTINCT  title FROM tv_show_genres tsg
RIGHT JOIN tv_shows ts
ON tsg.show_id = ts.id

WHERE show_id NOT IN (
 SELECT t1.show_id FROM tv_show_genres t1
  INNER JOIN tv_genres tg
  ON t1.genre_id = tg.id
  WHERE name = 'Comedy'
)
OR show_id IS NULL
ORDER BY title ASC;
