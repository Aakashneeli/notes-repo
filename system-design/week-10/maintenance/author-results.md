# Author fixture observations

Executed 2026-09-19 with Python 3.14.7, Linux 7.2.3-arch1-3 x86_64/glibc 2.44. These measurements are tutor QA, not learner evidence. Shared-machine load is uncontrolled; these are scheduling demonstrations, not hardware benchmarks.

Each row uses 20 requests submitted as a burst. Every tenth request deliberately times out during simulated retrieval: error rate is 0.10 in all nine runs. Latency begins at common burst submission, so event-loop scheduling delay is included. No network or provider is involved.

| Mode | Concurrency | Repetition | p50 ms | p95 ms | requests/s |
|---|---:|---:|---:|---:|---:|
| cooperative | 1 | 1 | 293.91 | 568.35 | 33.98 |
| cooperative | 1 | 2 | 294.71 | 569.44 | 33.91 |
| cooperative | 1 | 3 | 294.15 | 568.75 | 33.95 |
| cooperative | 4 | 1 | 91.96 | 153.53 | 130.22 |
| cooperative | 4 | 2 | 91.86 | 153.61 | 130.17 |
| cooperative | 4 | 3 | 91.68 | 153.38 | 130.34 |
| blocking | 4 | 1 | 222.76 | 405.66 | 49.30 |
| blocking | 4 | 2 | 223.19 | 405.65 | 49.30 |
| blocking | 4 | 3 | 223.00 | 405.28 | 49.35 |

Interpretation: cooperative waits overlap; time.sleep inside async work blocks other tasks. Increasing concurrency helps the waiting fixture; it does not prove a real dependency can accept that load. p95 includes waiting behind other requests in this burst, not just the 20+10 ms service waits. Low counts and artificial delays limit generalization.

The nine observations were executed through the harness's measure() function; the public CLI was also run and checked. Reproduce the configurations with Lesson 10's commands; timing varies. Initial measurement code started the clock after each task was scheduled; author review corrected this before these final observations, because that omitted part of the blocking delay.
