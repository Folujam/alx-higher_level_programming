--script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending
SELECT city, AVG(values) as average_temperature
FROM temperatures
GROUP BY city
ORDER BY average_temperature DESC;
