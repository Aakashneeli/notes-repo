# Twenty queries you write
First use: lessons 3–5; revisit lesson 13. Work from backend/week-05.
Read seed.sql; edit queries.sql; run:
`psql "$W5_PSQL_URL" -X -f practice/queries.sql`.
The seed creates connection-local TEMP tables, so rerunning doesn't reset any project data.
Write all queries yourself. Keep Q labels and add a prediction comment BEFORE each query.
Record output, explanation and help used in sql-notes.md; supplied examples don't count.

All read queries run before mutations; add ORDER BY id (or author id) for deterministic rows.
1. Select all article IDs/titles. Expected IDs 1,2,3,4.
2. Select published article IDs. Expected 1,3.
3. Select unpublished titles ordered by id. API notes, Draft.
4. Select articles with views > 5. SQL notes.
5. Select views from 0 through 5 inclusive. IDs 2,3,4.
6. Select title starting with SQL using LIKE. SQL notes.
7. Order by views descending, id ascending. IDs 1,3,2,4.
8. Take two rows after offset one in ascending id. IDs 2,3.
9. Find unassigned articles with IS NULL. Draft.
10. Find assigned articles with IS NOT NULL. IDs 1,2,3.
11. Inner join author name with article title. Asha twice, Ben once; no Draft.
12. Left join all authors to article title. Same plus Chen with NULL.
13. Count all articles. 4.
14. Group articles by published and count. false:2; true:2.
15. Count articles per author including zero. Asha:2, Ben:1, Chen:0.
16. Keep only authors with at least two articles using HAVING. Asha:2.
17. INSERT article id 5, author 3, title New, published false, views 0;
    RETURNING id,title must show 5,New.
18. UPDATE only article 5 to published true, RETURNING id,published => 5,t.
19. Increment article 1's views by 2 using its stored value; RETURNING views => 12.
20. DELETE only article 5 RETURNING id => 5.
Final supplied ROLLBACK undoes 17–20. A zero-row write is valid SQL but may mean a wrong ID.

## Progressive help
First retry: identify source tables, filter rows, choose output columns, then ordering.
Second hint: SQL uses single quotes for text, = for equality, IS NULL for missing values.
Joins use ON articles.author_id=authors.id. WHERE acts before grouping; HAVING after it.
Read lesson 5's worked zero-count example only if Q15 blocks you; then close it and vary it.
Don't replace these 20 queries with a generated answer sheet.
