SELECT ROUND(SUM(tiv_2016), 2) AS tiv_2016
FROM (
    SELECT
        tiv_2016,
        COUNT(*) OVER (PARTITION BY tiv_2015) AS cnt_2015,
        COUNT(*) OVER (PARTITION BY lat, lon) AS loc
    FROM insurance
) AS i_cnt
WHERE loc = 1 AND cnt_2015 > 1