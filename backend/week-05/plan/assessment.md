# Completion requires independent evidence
Use after lesson 14. No tutor-prepared artifact proves learning.
- Implement model/repository/migrations; explain SQL emitted by each endpoint.
- Run all beginner and project tests against their stated targets; record outputs/versions.
- Add a test that fails when event insertion fails after task insertion; explain rollback.
- Add two concurrent sessions competing for the same unique title; only one commits.
- Reproduce a real bug, write regression, show failing-before/passing-after.
- Write all 20 SQL queries yourself with predictions and a changed input.
- Draw actual PK/FK/cardinality/nullability/delete policy in draw.io or Excalidraw.
- Apply migration on fresh DB and with existing rows; inspect data and version.
- Explain downgrade information loss before any destructive rollback.
- Compare a selective filter plan with/without chosen index and interpret actual rows.
- Recreate an API process and show the same stored task through another connection.
- Explain: Why these tables/relationships? What happens with concurrent writes?
  What query does each endpoint execute? What breaks without an index vs constraint?
- After a delay: add optional due_date yourself with migration, API validation and tests;
  demonstrate old rows remain valid. Explain what was reused and what changed.
This last variation is a small transfer test, not required finished scaffolding.
Record gaps honestly; no timed score or page-count requirement.
