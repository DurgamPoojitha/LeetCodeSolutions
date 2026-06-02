# Write your MySQL query statement below
WITH ranked AS (
    SELECT
        student_id,
        subject,
        score,
        exam_date,
        ROW_NUMBER() OVER (
            PARTITION BY student_id, subject
            ORDER BY exam_date
        ) AS rn_first,
        ROW_NUMBER() OVER (
            PARTITION BY student_id, subject
            ORDER BY exam_date DESC
        ) AS rn_last,
        COUNT(*) OVER (
            PARTITION BY student_id, subject
        ) AS exam_count
    FROM Scores
),
scores_cte AS (
    SELECT
        student_id,
        subject,
        MAX(CASE WHEN rn_first = 1 THEN score END) AS first_score,
        MAX(CASE WHEN rn_last = 1 THEN score END) AS latest_score,
        MAX(exam_count) AS exam_count
    FROM ranked
    GROUP BY student_id, subject
)
SELECT
    student_id,
    subject,
    first_score,
    latest_score
FROM scores_cte
WHERE exam_count >= 2
  AND latest_score > first_score
ORDER BY student_id, subject;