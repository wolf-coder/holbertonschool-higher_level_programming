-- Write a script that lists all genres in the database hbtn_0d_tvshows_rate by their rating.

    -- Each record should display: tv_genres.name - rating sum
    -- Results must be sorted in descending order by their rating
    -- You can use only one SELECT statement
    -- The database name will be passed as an argument of the mysql command


SELECT title ,SUM(rate) AS 'rating' FROM tv_show_ratings
INNER JOIN tv_shows
ON tv_show_ratings.show_id = tv_shows.id
GROUP BY show_id
ORDER BY rating DESC;
