# Week 11 source coverage

TARGET_WEEK=11 → source article#week-11:
**AWS Deployment, CI/CD, Secrets, Cloud Logs, Runbooks, and Cost Control**.
Workspace: cloud-devops/week-11. Exact mapping, no exception.
Source path/hash/date in [README](../README.md); numbered section is authoritative.

| In-scope source requirement | Lessons | Practice / artifacts (under projects/deployment unless stated) | Demonstrated ability |
| --- | --- | --- | --- |
| Rationale: operate the designed, containerized backend within $20/month | 1–2 | selection.md; cost-plan.md | Explain prior state and measured resource needs |
| IAM hygiene, budgets, users/roles, least privilege | 2–3 | access-plan.md; exercises monthly_total/rule_allows | Estimate all categories; distinguish IAM and networking; real budget confirmation pending |
| Networking: SG, inbound/outbound, ports, SSH | 3,5,9 | architecture.mmd; access-plan.md | Trace tunnel; diagnose timeout vs 401; demonstrate access if live |
| EC2 low-cost path; ECR/ECS basics | 4,7–9 | Dockerfile; runbook.md; endpoint.md | Build and test image; identify registry vs scheduler vs VM |
| S3 uploaded files/artifacts (conditional); RDS/external DB tradeoff | 7 | data/sample.txt; storage.md | Defend applicability; if applicable real app object round-trip and private denial |
| GitHub Actions test/build/push/deploy/secrets | 6,8,11 | ci/workflow.yml; secrets.md; runbook.md | Local gates; optional ECR push; documented deploy; hosted run evidence separate |
| CloudWatch, health, environment variables, rollback | 4,6,9–11 | fixture; practice events; release.py; rollback.md | Trace 200/401/500/503; match cloud request ID; reject bad release |
| Lambda awareness and long-running AI job fit | 7 | storage.md; session log | Compare short event and 20-minute job, state and retry needs |
| Lab 1: Dockerized FastAPI on AWS | 4,9 | Dockerfile; endpoint.md | Live private endpoint with dated release/status observations; pending learner action |
| Lab 2: S3 if upload/storage needed | 7 | storage.md | Fixture: documented N/A; real ingestion: app integration required |
| Lab 3: environment/secrets not committed | 6,9 | secrets.md; .env.example; .gitignore | Ignore/rotation evidence; host permissions; no real values committed |
| Lab 4: lint/test/build and documented deploy | 8,11 | workflow.yml; runbook.md | Meaningful failing check blocks release; hosted CI not inferred |
| Lab 5: deployed logs/debug flow | 10 | runbook.md; weekly log | CloudWatch group/stream/request ID evidence or pending |
| Lab 6: shutdown checklist | 2,12 | shutdown.md | Resource-specific keep/remove decision and delayed billing recheck |
| Deliverables: endpoint; diagram/runbook; workflow/secrets; costs/rollback | 5–12 | all deployment records | Assessment independently reviewed; no pre-filled deployment claims |
| Explain: traffic from internet; secrets source/injection | 5–6,12 | weekly-logs/week-11.md | Own-word diagram and rotated-key observation |
| Explain: production logs/health; successful deploy returns 500 | 10–12 | runbook.md; rollback.md; weekly log | Request-correlated diagnosis, alternative hypothesis and recovery |
| Resources: AWS IAM/EC2/S3/RDS/ECR/ECS/CloudWatch; Docker; Actions | all | RESOURCES.md; reading-log.md | Read one source to resolve an actual question |

## Scope and evidence limits
DSA mixed review, old algorithm misses and top-10 DSA mistakes are explicitly excluded.
No detailed Week 12 material or reconstructed earlier weeks.
All syllabus topics have teaching and an evidence route. Live endpoint, hosted CI,
CloudWatch delivery, actual billing and conditional real S3 integration are not verified
by preparation; these remain learner actions. A draft private endpoint is not a deployment.
