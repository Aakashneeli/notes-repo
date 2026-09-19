# Deployment runbook
Status: learner-owned draft; not executed

## Preconditions
Backend commit, tests, cost approval by learner, account/region, SSH identity:
Docker/CLI versions and machine architecture:
Exact inventory and rollback image digest:

## Release
Starting machine/directory for each command; build/test/tag/transfer/start:
Config injection (names only):
Health + readiness + authenticated request expected output:

## Investigate
Symptom / first observation / hypothesis / discriminating check / next action:
CloudWatch group/stream, request ID, release, UTC range:
Missing-log diagnosis (driver, role, region, egress, retention):

## Recover
Rollback trigger, commands, data compatibility, verification:

## Evidence
Endpoint record, CI run+commit, logs, measured cost and shutdown record:
