# Completion by demonstrated ability

Use these criteria after implementing, not as a page-reading tally. All are pending.

## Independent evidence

- From the project manifest/lock, reproduce installation and start the local API.
- Implement all five operations, schemas, memory, pagination/filtering and auth without a finished generated implementation.
- Pass supplied contract checks, add a meaningful regression and explain what each case proves.
- Show one failure before its fix and success after; demonstrate no mutation after rejected input/auth/conflict.
- Run happy path and negative cases in curl and Postman. Export your collection, inspect for keys, re-import and rerun. A supplied starter export is not your work.
- Complete README, lifecycle note/sequence diagram and a source-reading note with actual paths/lines.
- Vary a requirement independently (e.g. a title prefix filter); predict affected schemas/service/routes/tests/docs, preserve baseline and add evidence.
- After a delay, reconstruct a negative test and request trace without looking at answers. Disclose assistance and remaining uncertainty.

## Exact source explain-back prompts

1. What happens from the moment a request hits a route until a response is returned?
2. Where does validation happen?
3. Why does this endpoint return this status code?
4. How do your tests differ from your Postman checks?

Answer in weekly-logs/week-04.md using one concrete request, then a failure variation.
A strong explanation names input source, dependency/schema boundary, operation,
state effect, response encoding and corresponding evidence. A fluent definition
without being able to alter/debug the code is not independent ownership.

## Review decision

For each criterion: independent / with hints / not yet; link evidence and next review.
Use templates/review.md. Keep prior attempts. No fixed hours or minimum invented logs.
