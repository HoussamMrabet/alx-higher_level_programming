-- Lists all privileges of the users user_0d_1 and user_0d_2.
SELECT CONCAT("Grants for ", QUOTE(user), "@", QUOTE(host)) AS Grants FROM mysql.user WHERE user IN ('user_0d_1', 'user_0d_2');
