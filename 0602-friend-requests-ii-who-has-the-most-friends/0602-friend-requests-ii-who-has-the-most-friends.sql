WITH AccepterRequesterStat AS (
    SELECT 
        accepter_id AS id,
        COUNT(DISTINCT requester_id) AS num
    FROM RequestAccepted
    GROUP BY accepter_id
),

RequesterAccepterStat AS (
    SELECT 
        requester_id AS id,
        COUNT(DISTINCT accepter_id) AS num
    FROM RequestAccepted
    GROUP BY requester_id
),

FriendsStat AS (
    SELECT id, SUM(num) AS num
    FROM (
        SELECT id, num FROM AccepterRequesterStat
        UNION ALL
        SELECT id, num FROM RequesterAccepterStat
    ) AS combined
    GROUP BY id
)

SELECT id, num
FROM FriendsStat
WHERE num = (
    SELECT MAX(num)
    FROM FriendsStat
);
