# Write your MySQL query statement below
WITH ranked_reviews AS (
    SELECT
        employee_id,
        review_date,
        rating,
        ROW_NUMBER() OVER (
            PARTITION BY employee_id
            ORDER BY review_date DESC
        ) AS rn
    FROM performance_reviews
),
last_three AS (
    SELECT
        employee_id,
        review_date,
        rating
    FROM ranked_reviews
    WHERE rn <= 3
),
review_stats AS (
    SELECT
        employee_id,
        COUNT(*) AS review_count,
        MAX(CASE WHEN review_date = latest_date THEN rating END) AS latest_rating,
        MAX(CASE WHEN review_date = middle_date THEN rating END) AS middle_rating,
        MAX(CASE WHEN review_date = earliest_date THEN rating END) AS earliest_rating
    FROM (
        SELECT
            employee_id,
            review_date,
            rating,
            MAX(review_date) OVER (PARTITION BY employee_id) AS latest_date,
            MIN(review_date) OVER (PARTITION BY employee_id) AS earliest_date,
            (
                SELECT review_date
                FROM last_three l2
                WHERE l2.employee_id = l1.employee_id
                ORDER BY review_date
                LIMIT 1 OFFSET 1
            ) AS middle_date
        FROM last_three l1
    ) t
    GROUP BY employee_id
)
SELECT
    e.employee_id,
    e.name,
    (rs.latest_rating - rs.earliest_rating) AS improvement_score
FROM review_stats rs
JOIN employees e
    ON e.employee_id = rs.employee_id
WHERE rs.review_count = 3
  AND rs.earliest_rating < rs.middle_rating
  AND rs.middle_rating < rs.latest_rating
ORDER BY improvement_score DESC, e.name ASC; 