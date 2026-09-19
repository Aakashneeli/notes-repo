# Author validation

Verified 2026-09-19. Author verification does not mark learner material learned.

## Source and preservation
- Read the numbered source #week-10, exact title and all requirement blocks; read roadmap goal/baseline/sequence and adjacent weeks to establish prerequisites and purpose.
- Inspected organization rules, existing topic directories, shared style, Week 2 baseline, Week 9 mission/progress and actual unfinished Week 8/9 code. No same-number mismatch was found.
- Changes are limited to the new system-design topic README/index and Week 10 workspace, plus its entry in WORKSPACE-STRUCTURE.md. Earlier implementations, progress, sample data and Git history are preserved. No commit/publish/provisioning action was performed.

## Runnable and structural checks
- Python 3.14.7 on local Linux; no installed third-party dependencies needed for practice/project checks. Python >=3.11 is the stated compatibility target; 3.11 itself was not executed.
- maintenance/validate.py: 63 supplied weekly files mapped to first lessons, 375 local links/anchors resolved, 13 lesson structure checks, Python AST syntax, shared CSS import and five named draw.io XML pages.
- Eight instructor infrastructure tests pass: example/failure behavior, bounded retries, timeout event, fixture success/fault, measurements/errors, beginner answers, JSON samples and six malformed-event mutations.
- Seven project contract tests accepted a disposable in-memory correct behavior oracle. Four meaningful mutations were rejected (zero cost, sensitive extra content, fixed request ID, copied result). The oracle was never saved in learner files or scaffolding. The tests also cover partial/unknown versus zero usage, result/error identity, one call/event, varied rates and millisecond duration.
- Unfinished learner suite: four beginner test methods expose nine NotImplementedError subcase errors; seven project test methods expose seven NotImplementedError errors. run_observed.py exposes its intended unfinished observe() error. These are expected, not infrastructure defects or passing learner evidence.
- Completed practice/examples.py prints FIELD GUIDE, a variable positive timeout duration, and available attempts 2.
- Nine final fixture experiment runs (three configurations, three repetitions) recorded in maintenance/author-results.md; CLI output also checked. No learner performance/progress note was filled with author results.

## Teaching sufficiency review, separate from test results
- Reviewed each topic's explanation → worked trace → failure case → guided task/check → independent variation path. Required concepts remain in lessons; sources supplement them.
- Added an explicit callback/lambda trace and interactive miniature before the main async wrapper, shape/connector/save instructions before the diagram lab, and hand-worked cursor/batch examples to bridge performance concepts.
- The file map is exhaustive; each supplied learning item has a first-use section stating its role and action. Commands start at the weekly root or explicitly return there. Earlier-week links are targeted refreshers, not assumed completion.
- Lesson length is bounded by one main outcome; dense file and evidence instructions are grouped at first use. Progress is initially unassessed. Main implementation, diagram contents, ADR choices and learner evidence remain unfinished intentionally.

## Browser and print
- Local Chromium/Playwright: 32 page/viewport checks (desk, 13 lessons, two references at 390 and 1280 px). Shared local CSS loaded, one H1 per page, no horizontal document overflow, no browser page/resource errors; hint disclosures open.
- Visually inspected full-page desktop/mobile study-desk screenshots and the desktop instrumentation lesson. Layout uses shared course typography, focus styling, skip links and natural reading order.
- Print media checked at both widths; white background/no overflow. A sample instrumentation-lesson print PDF was generated. Full page-by-page PDF pagination, physical printing, screen-reader testing and every mobile screenshot were not manually inspected.
- Screenshots/sample print output are generated, ignored runtime/browser/ artifacts, not source or learning evidence. Browser automation requires an already installed Playwright plus Chromium; no dependency was downloaded. The first sandboxed Chromium launch failed at a restricted socket operation; the permitted local unsandboxed QA run succeeded.
- Attempted to open Lesson 1 with xdg-open; its browser launch hit the same sandbox socket restriction, so automatic opening was not confirmed. Use the delivered study-desk/lesson link.

## Remaining limits
- The draw.io starter XML/page structure was validated; opening, editing and saving it in the draw.io editor was not automated. Those actions are explicitly taught as learner checks.
- No live Redis, database, vector store, provider, CloudWatch, LangSmith, HTTP load test or deployment was exercised. Cache/rate limiting uses the roadmap's documented-design option; CloudWatch/LangSmith mappings are conceptual here.
- The in-process fixture is not an integrated backend. Actual Week 8/9 integration is pending their unfinished prerequisites. This is stated in the contract, progress, lessons and coverage map.
- Official documentation/author pages were consulted; full books were not accessed. No provider pricing is asserted: sample rates are fictional.
- Local behavioral and static checks cannot establish production reliability, security or learner mastery.

Re-run from system-design/week-10: python maintenance/validate.py. Follow Lesson 13 for separate learner assessment checks.
