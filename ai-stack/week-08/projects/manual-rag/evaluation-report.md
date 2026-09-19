# Retrieval evaluation — learner-owned, not run
## Configuration
Commit; corpus/version; embedding model/revision/dimension; generation provider/model;
chunk size/overlap; filter; k; context budget; date; offline versus semantic/live.
## Golden set
Start with data/golden-seeds.json (20 supplied examples). Independently verify every expected
source against the corpus and rewrite/add at least five questions. Keep 15–25 total.
Save your set as data/golden.json; do not overwrite seeds. Record why each change matters.
## Results
For every ID record expected docs, retrieved chunk IDs/scores, selected context IDs,
answer, cited IDs, support judgement, abstention, failure label and latency.
Use templates/evaluation-row.md at the weekly root for a row format.
No measurements yet. Report hit@k on answerable cases separately from abstention behaviour.
## Diagnosis and controlled change
Baseline; one failure; retrieval-only rerun; oracle-context rerun; proposed cause; one change;
rerun same set; held-out variations; regressions. Distinguish mock from real-model evidence.
## Limits
This small fictional corpus cannot establish production quality or privacy guarantees.
