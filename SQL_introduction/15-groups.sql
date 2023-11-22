-- Number by score
SELECT score AS "n_score",
COUNT(score) AS "times_scored"
FROM second_table
GROUP BY score;
