\set ON_ERROR_STOP on
\ir seed.sql
SELECT id,title FROM articles WHERE published ORDER BY id LIMIT 1;
SELECT a.name, count(b.id) AS articles
FROM authors AS a LEFT JOIN articles AS b ON b.author_id=a.id
GROUP BY a.id,a.name ORDER BY a.id;
BEGIN;
UPDATE articles SET views=views+1 WHERE id=1;
SELECT views FROM articles WHERE id=1;
ROLLBACK;
SELECT views FROM articles WHERE id=1;
