# Safety Checklist

Learner checks only with cited code/test evidence.

- [ ] Only the read-only document lookup can execute
- [ ] Arguments validated before dispatch; no paths/SQL/shell from model text
- [ ] Tenant identity supplied by trusted backend and enforced during access
- [ ] Retrieval/tool results treated as untrusted data
- [ ] Call count, timeout and failure behavior bounded
- [ ] No writes, credentials or broad service objects in graph state
- [ ] Trace data reviewed; no private information or secrets uploaded
- [ ] Citation membership and factual support distinguished
- [ ] Unknown actions rejected, not interpreted

Evidence and residual risks:
