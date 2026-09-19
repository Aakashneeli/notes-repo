# Week 11 Resources

## Knowledge

Source roadmap: `/home/an10/Downloads/ai-backend-roadmap.html#week-11`; mapping and hash in README.
Official pages inspected 2026-09-19. Recheck prices and action versions before live use.

- [AWS Budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html) — Alerts, forecast thresholds and notification delay; read before choosing a spend limit.
- [IAM best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) — Human federation, temporary workload roles and least privilege.
- [EC2 security groups](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-security-groups.html) — Allowed traffic, stateful replies and instance network boundaries.
- [Docker image practices](https://docs.docker.com/build/building/best-practices/) — Small build contexts, image construction and deliberate dependency updates.
- [FastAPI containers](https://fastapi.tiangolo.com/deployment/docker/) — Container process, bind address and deployment concerns.
- [Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html) — Managed configuration and SecureString option.
- [GitHub secrets](https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/use-secrets) — Secret scopes, passing secrets and limitations of masking.
- [S3 security](https://docs.aws.amazon.com/AmazonS3/latest/userguide/security-best-practices.html) — Private objects, access boundaries and storage protection.
- [RDS overview](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html) — Managed relational database responsibilities.
- [S3 copy command](https://docs.aws.amazon.com/cli/latest/reference/s3/cp.html) — File/object round-trip command options.
- [Push images to ECR](https://docs.aws.amazon.com/AmazonECR/latest/userguide/docker-push-ecr-image.html) — Registry authentication, tagging and pushing.
- [ECS overview](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html) — Tasks, services and capacity choices.
- [Lambda timeout](https://docs.aws.amazon.com/lambda/latest/dg/configuration-timeout.html) — Timeout ceiling and workload-duration decisions.
- [Actions workflow syntax](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax) — Triggers, permissions, job order and working directories.
- [GitHub OIDC to AWS](https://docs.github.com/en/actions/how-tos/secure-your-work/security-harden-deployments/oidc-in-aws) — Temporary cloud identity and audience/subject restrictions.
- [EC2 getting started](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html) — Launch settings, instance state and connection prerequisites.
- [EC2 SSH access](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/connect-to-linux-instance.html) — Key and SSH connection prerequisites.
- [Docker on Ubuntu](https://docs.docker.com/engine/install/ubuntu/) — Official repository installation for the selected Ubuntu host.
- [Docker awslogs driver](https://docs.docker.com/engine/logging/drivers/awslogs/) — Log-group/stream options, daemon credentials and permissions.
- [CloudWatch CLI tail](https://docs.aws.amazon.com/cli/latest/reference/logs/tail.html) — Recent events, stream filters and following logs.
- [EC2 pricing](https://aws.amazon.com/ec2/pricing/on-demand/) — Region/type billing inputs; verify before spending.
- [VPC pricing](https://aws.amazon.com/vpc/pricing/) — Public IPv4 and optional networking charges.
- [RDS stop behavior](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_StopInstance.html) — Storage billing and automatic restart after a temporary stop.

- [AWS Pricing Calculator](https://calculator.aws/) — Save your region-specific usage assumptions before launch; no fixed price promise is made here.
- [GitHub checkout](https://github.com/actions/checkout) and [setup-python](https://github.com/actions/setup-python) — Review supported releases and pin reviewed SHAs before activating a workflow.

## Wisdom (Communities)

- [AWS re:Post](https://repost.aws/) — Optional operational questions with redacted symptoms, region and relevant configuration; evaluate answers against official docs.
- [FastAPI discussions](https://github.com/fastapi/fastapi/discussions) — Optional application deployment questions with a minimal reproduction.

No community contact or account action was performed. No preference to join is assumed.

## Limits
Live account pricing/eligibility, IAM and network behavior cannot be established from local
tests. The local fixture has no file storage need; S3 integration is conditional, not silently
claimed complete. Sources support the explanations; worked exercises are original teaching examples.
