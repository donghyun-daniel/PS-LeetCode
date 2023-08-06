# Write your MySQL query statement below
WITH daily_amount AS (
    SELECT
        visited_on,
        SUM(amount) AS amount
    FROM customer
    GROUP BY visited_on
)

SELECT 
    t1.visited_on,
    ROUND(SUM(t2.amount), 2) AS amount,
    ROUND((SUM(t2.amount) / 7), 2) AS average_amount
FROM daily_amount t1
JOIN daily_amount t2 ON DATEDIFF(t1.visited_on, t2.visited_on) BETWEEN 0 AND 6
WHERE DATE_SUB(t1.visited_on, INTERVAL 6 DAY) >= (
    SELECT MIN(visited_on) FROM daily_amount
)
GROUP BY t1.visited_on
ORDER BY t1.visited_on;
