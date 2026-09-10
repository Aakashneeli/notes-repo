# Coverage — exact source Week 03

Source `/home/an10/Downloads/ai-backend-roadmap.html#week-3`: **03 — Pro Python**,
**Professional Python Structure, Pydantic, Logging, and Practical LLD**.
Chosen workspace: **python/week-03/**. Main deliverables: text-processing package with
validation/settings/logging/tests, codebase-reading note, module diagram.
No Week 3 conflict/naming exception. Historical Week 2 Foundation is preserved and
not silently selected. See [source mapping](../roadmap/source-week-03.md).

| In-scope source requirement | Lessons | Practice and demonstrated-ability evidence |
|---|---|---|
| Package layout: src/tests/modules/imports/public and internal helpers | [2](../lessons/0002-package-and-environment.html) | Installed import-path experiment; public boundary explanation |
| Typed unions/optionals/collections/returns | [4](../lessons/0004-typed-contracts.html) | label practice and typed project signatures; missing-versus-None explanation |
| Dataclasses versus Pydantic | [5](../lessons/0005-models-and-validation.html) | Badge/Booking experiment; own Ticket; model-choice rationale |
| Environment/settings/.env.example | [6](../lessons/0006-settings.html) | read_limit practice; settings tests and command-scoped setting evidence |
| Logging levels/message structure/no secrets | [7](../lessons/0007-structured-logging.html) | formatter/handler tests; safe stdout/stderr demonstration |
| Practical LLD: functions/classes/service/dependency direction | [8](../lessons/0008-service-boundaries.html), [11](../lessons/0011-codebase-and-diagram.html) | describe practice; injected reader tests; own module diagram and tradeoff |
| Async I/O/blocking/FastAPI rationale | [9](../lessons/0009-async-basics.html) | both async traces plus sequential-await variation and explanation |
| Lab: text package split/normalize/metadata | [3](../lessons/0003-functions-and-tests.html), [8](../lessons/0008-service-boundaries.html), [10](../lessons/0010-integration-and-debugging.html) | core/service implementation and exact sample output |
| Lab: Pydantic config and output validation | [5](../lessons/0005-models-and-validation.html), [6](../lessons/0006-settings.html) | Config/Record invalid-case checks and explanation |
| Lab: structured logs/settings module | [6](../lessons/0006-settings.html), [7](../lessons/0007-structured-logging.html), [8](../lessons/0008-service-boundaries.html) | settings/logging/service tests; code and startup trace |
| Lab: tests normal/invalid/empty/large | [3](../lessons/0003-functions-and-tests.html), [10](../lessons/0010-integration-and-debugging.html) | unit, real-file and CLI checks; generated large/exact-limit cases |
| Lab: read small Python repo and architecture note | [11](../lessons/0011-codebase-and-diagram.html) | pinned PyPA sampleproject local execution; codebase-reading/week-03.md |
| Deliverable: professional src package repo | [2](../lessons/0002-package-and-environment.html), [12](../lessons/0012-ownership-and-review.html) | projects/text-workbench independent packaging inside notes repo; reviewed local commits |
| Deliverable: .env.example/README/tests/Ruff/typed signatures | [2](../lessons/0002-package-and-environment.html), [4](../lessons/0004-typed-contracts.html), [10](../lessons/0010-integration-and-debugging.html), [12](../lessons/0012-ownership-and-review.html) | completed project README; pytest/Ruff outputs; explain scaffold |
| Deliverable: note covering entrypoints/modules/tests/config | [11](../lessons/0011-codebase-and-diagram.html) | completed codebase-reading/week-03.md with path/line evidence |
| Deliverable: draw.io/Excalidraw module diagram | [11](../lessons/0011-codebase-and-diagram.html) | learner projects/text-workbench/module-diagram.drawio, actual arrows and rationale |
| Explain why modules split | [8](../lessons/0008-service-boundaries.html), [12](../lessons/0012-ownership-and-review.html) | weekly log: benefit, cost, alternative |
| Explain pure functions and side effects | [3](../lessons/0003-functions-and-tests.html), [8](../lessons/0008-service-boundaries.html), [12](../lessons/0012-ownership-and-review.html) | weekly log: concrete functions and call paths |
| Explain where config loads and why | [6](../lessons/0006-settings.html), [12](../lessons/0012-ownership-and-review.html) | weekly log: startup boundary and test replacement |
| Explain test difficulty from wrong layer | [8](../lessons/0008-service-boundaries.html), [12](../lessons/0012-ownership-and-review.html) | weekly log: one bad dependency move and its consequence |
| Resources: Pydantic/logging/design book | [5](../lessons/0005-models-and-validation.html), [7](../lessons/0007-structured-logging.html), [8](../lessons/0008-service-boundaries.html), [11](../lessons/0011-codebase-and-diagram.html) | RESOURCES.md; docs experiment; optional owned/library book, no purchase requirement |

## Exclusions and scope adjustments

All DSA/NeetCode, algorithm interview exercises, complexity drills and associated
logs are excluded, including the source's Week 3 pointer/window drills. Text collections
remain as product tasks. No detailed future weeks or full prior-week reconstruction.
The source's separate repo convention is adapted to an independent package directory
inside the current repository. No nested repo, publishing or remote workflow required.
Specific text rules and CLI are teaching choices implementing the source text-package lab.

## Gaps versus unfinished learner work

Teaching coverage is supplied for all in-scope items. Models, transforms, settings,
logging and orchestration intentionally await learner implementation. The architecture
note, module diagram, assessed decisions, README completion, real debugging evidence
and delayed explanations also remain learner work. This is not an authoring gap or
claimed mastery. The book is optional supplemental reading; its full chapters were
not accessed. Local checks do not prove production behavior or live deployment.
