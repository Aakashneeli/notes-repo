# Shutdown and billing inventory
Status: pending; never delete data without checking retention needs.

Resource ID | Region | Owner | Cost while stopped? | Keep/stop/delete | Backup decision | Verification/time
--- | --- | --- | --- | --- | --- | ---

Account-wide review: EC2, EBS volumes/snapshots, public/Elastic IPs, ECR images,
CloudWatch log groups, S3 objects/versions/multipart uploads, RDS/backups,
NAT/load balancers if any, external DB/model provider and GitHub usage.
Stop vs terminate decision:
Deletion protection/retention and exact resource confirmation:
Temporary credentials and CI access revoked if no longer needed:
Next-day and later billing review dates/results:
