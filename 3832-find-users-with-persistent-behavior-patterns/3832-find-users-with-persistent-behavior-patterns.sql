WITH numbered AS (
    SELECT
        user_id,
        action,
        action_date,
        ROW_NUMBER() OVER (
            PARTITION BY user_id, action
            ORDER BY action_date
        ) AS rn
    FROM activity
),

grouped AS (
    SELECT
        user_id,
        action,
        action_date,
        DATE_SUB(action_date, INTERVAL rn DAY) AS grp
    FROM numbered
),

streaks AS (
    SELECT
        user_id,
        action,
        COUNT(*) AS streak_length,
        MIN(action_date) AS start_date,
        MAX(action_date) AS end_date
    FROM grouped
    GROUP BY user_id, action, grp
    HAVING COUNT(*) >= 5
),

ranked AS (
    SELECT *,
           ROW_NUMBER() OVER (
               PARTITION BY user_id
               ORDER BY streak_length DESC
           ) AS rnk
    FROM streaks
)

SELECT
    user_id,
    action,
    streak_length,
    start_date,
    end_date
FROM ranked
WHERE rnk = 1
ORDER BY streak_length DESC, user_id ASC;