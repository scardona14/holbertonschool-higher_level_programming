-- Script that list all records with a score >= 10 in a table
SELECT score, name FROM second_table HAVING score>=10 ORDER BY score DESC;
```