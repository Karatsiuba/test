SELECT 
    DAY(date_column) AS day_of_month,
    COUNT(*) AS total_count,
    AVG(value_column) AS average_value
FROM 
    your_table_name
GROUP BY 
    DAY(date_column)
ORDER BY 
    day_of_month;