-- lists all privileges of the users user_0d_1 and user_od_2
SELECT * FROM mysql.user
WHERE user IN ('user_0d_1', 'user_0d_2')
AND host = 'localhost';
