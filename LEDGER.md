# Provenance ledger

Use exactly this format for every entry. Write each entry when the work is done, one entry per reviewable change.

```text
## Entry <n>
artifact:  what this entry covers: a file, a commit SHA, a document, or an experiment
tool:      product name, model name, model version, and the date of use
prompts:   one-line summary each; the verbatim prompts live in prompts/ and are
           referenced here by file path
review:    what you read, what you changed, what you rejected, and why
checks:    the commands you ran and their results
evidence:  the requirement, test, or evidence ID this traces to
risk:      what remains unverified after this change

For an experiment, add three fields:
dataset:   task set identifier and its commit SHA or version
result:    metric, N, and the result table or its file path
changed:   what you did differently as a result
```

Add your entries below this line, starting with Entry 1.

---

## Entry 1
artifact:  report/REPORT.md, Part 1 evidence log (E-1 to E-6, A-1, Q-1 to Q-3) and Part 2 evidence audit
tool:      Claude (claude.ai), Claude Opus 5.5, 2026-10-15
prompts:   asked the assistant to draft the evidence log and seven-row audit from INT-01; prompts/drafting_assist_prompt.txt
review:    checked every E entry against the exact paragraph it cites in transcripts/interview.txt; rejected logging "15 minutes" or "20 minutes" as an E fact because P06 and P12 conflict, and logged the conflict only as Q-1; recorded P15 as assumption A-1 instead of evidence because it is a prediction; confirmed no entry cites SYN-01; chose P13 over P04 as the strongest past event because it has a full timed sequence and an observed cost
checks:    manual check of each Source cell against the paragraph IDs P01-P21; count = 10 entries, IDs all start with E-, A- or Q-
evidence:  E-1, E-2, E-3, E-4, E-5, E-6, A-1, Q-1, Q-2, Q-3
risk:      the grace value (Q-1), the technician readiness signal (Q-2) and the message recipient (Q-3) remain unanswered; only one interview exists, so no claim is checked against a second borrower or the technicians

