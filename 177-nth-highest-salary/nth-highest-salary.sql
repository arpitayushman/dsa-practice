CREATE OR REPLACE FUNCTION NthHighestSalary(N INT) RETURNS TABLE (Salary INT) AS $$
BEGIN
 IF N <= 0 THEN
    RETURN QUERY SELECT NULL::INT;
    RETURN;
  END IF;
  RETURN QUERY (
    -- Write your PostgreSQL query statement below.
    SELECT DISTINCT e.salary
    FROM Employee e
    ORDER BY salary DESC
    OFFSET GREATEST(N - 1, 0)
    LIMIT 1
      
  );
END;
$$ LANGUAGE plpgsql;
