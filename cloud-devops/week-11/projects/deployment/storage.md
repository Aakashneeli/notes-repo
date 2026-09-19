# Storage decision
Status: conditional lab pending

Does the chosen app upload or retain artifacts? Evidence:
If no: mark S3 integration not applicable; still explain S3 vs RDS.
If yes: private bucket, prefix, role actions/resources, encryption and lifecycle:
Round-trip object byte comparison and unauthorized request result:
App integration path and test (CLI round-trip alone is not app integration):
Metadata schema/object key relationship:
RDS vs external PostgreSQL vs no DB: cost, TLS, region/latency, backup/restore, retention:
Persistent data and migrations relevant to rollback:
