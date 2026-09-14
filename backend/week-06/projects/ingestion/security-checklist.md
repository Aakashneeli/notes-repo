# Security evidence — learner owned
For each row write implemented/tested/design-only, evidence link and remaining risk.
- Auth on upload AND status; absent/invalid key; empty server key fail closed.
- Validation: required field, names, type, exact size/overflow, empty/NUL/invalid UTF-8.
- Secrets: ignored local config, no keys in URL/logs/export; rotation plan if exposed.
- File safety: private trusted root, server keys, exclusive writes, compensation.
- Logging: job ID/state/error code only; no content, credentials or raw exception messages.
- SQL: bound values and allowed identifiers; no raw concatenation.
- CORS: allowed preflight, disallowed origin; explain non-browser behavior.
- Rate limiting: ingress/body limits, authenticated quota, shared counts, outage policy.
- Limits: parser spooling/resource bounds, no malware certification, single-tenant, no durable dispatch.

Own observations and remaining risks:
