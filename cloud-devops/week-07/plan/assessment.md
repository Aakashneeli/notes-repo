# Independent completion contract

Use your own code and runbook, then close lessons for explain-backs. Ask for review rather than a finished implementation.

- Implement: Dockerfile, five-service Compose topology, operations.py, observability.py and workflow.yml satisfy their contracts without modifying supplied assertions.
- Test: full default pytest and Ruff pass. Run the real job smoke and vector probe; link outputs and versions. Test no-ID/bad-ID requests, independent request IDs and confidential bodies yourself.
- Debug: reproduce a local Docker failure, choose a discriminating probe, repair it, and preserve regression evidence. A daemon permission block is valid evidence of a blocker, not completed runtime debugging.
- Explain: answer all four source prompts in L13; trace one request and queued job, and say precisely what every check fails to prove.
- Vary: change host port, fail Redis, stop worker, recreate services without deleting volumes. Predict before observing. Demonstrate retained completed job and no secret leakage.
- Document: finished architecture diagram, runbook, bridge limits, real debugging note and CI evidence with local/hosted distinction.
- Reproduce: after committing intended work, use an isolated fresh local clone/project to verify the one Compose command. No remote push required.
- Retain: repeat closed-book explanation after roughly two days and a week, recording actual dates and help.

A blocked live environment means partial completion, even if local tests pass. A passing hosted Actions run is recorded only with its URL and commit; creating a draft workflow does not establish that. No author-supplied record is proof of learner understanding.
