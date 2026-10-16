# CS 690 Assignment 3 Report: Evidence to Executable Specification

Name: Kundan Singh
Repository: https://github.com/KKS071/cs690-assignment3
Commit SHA: given in the submitted PDF (a file cannot contain the SHA of the commit that adds it)

---

## Part 1. Evidence log

| ID | Source | Claim | Status | Owner |
| --- | --- | --- | --- | --- |
| E-1 | INT-01:P04 | Yesterday a student with a 2:00 camera kit called at 2:08; Jordan wrote "hold until 2:25" on the paper slip, the packed kit stayed on the pickup shelf, and the student arrived at 2:22 and completed pickup. | Observed | Jordan Lee (checkout coordinator) |
| E-2 | INT-01:P13 | Last Thursday Priya's 3:00 lighting kit was already released when she reached the desk at 3:16; a waitlisted student was waiting but the kit was still behind the counter while technicians checked a light stand; she waited until 3:38 for another kit and her interview started about ten minutes late. | Observed | Priya Shah (student borrower) |
| E-3 | INT-01:P06, INT-01:P21 | The grace period is a lab policy that the manager has changed before, and the system should use whatever grace value the lab has configured. | Stated | Lab manager |
| E-4 | INT-01:P17, INT-01:P21 | A reservation that has been checked in should remain active and should not disappear when the clock passes the grace window. | Stated | Jordan Lee |
| E-5 | INT-01:P04, INT-01:P06, INT-01:P19 | Staff can record a temporary hold with an end time; a reservation with a recorded hold is not released, and the hold, its end time and its reason should be preserved. | Stated | Jordan Lee |
| E-6 | INT-01:P09, INT-01:P21 | A released kit is not always ready for the next person; the desk does not promise it until the technicians finish their check, and the waitlist should only see equipment that is actually ready to hand out. | Stated | Jordan Lee / equipment technicians |
| A-1 | INT-01:P15 | Assumption: students would use a self-service "running late" action instead of calling the desk. This is Priya's prediction about future use, not an observed behavior. | Assumption | Student borrowers |
| Q-1 | INT-01:P06, INT-01:P12 | What is the current grace period? Jordan states 15 minutes; Priya states 20 minutes is the rule students hear. Not decided here. | Open | Lab manager |
| Q-2 | INT-01:P09, INT-01:P19, INT-01:P21 | How do the equipment technicians record that a kit's preparation is complete, and what does "ready" include? | Open | Equipment technicians |
| Q-3 | INT-01:P10 | Who must get a message before a kit goes to the waitlist ("they"), through which channel, and how long before? | Open | Jordan Lee / lab manager |

The conflicting grace value is logged only as Q-1. Neither 15 nor 20 appears as a settled E fact. No entry cites SYN-01.

---

## Part 2. Evidence audit

| # | Item | Location | Classification | Why it matters to requirements quality |
| --- | --- | --- | --- | --- |
| 1 | Direct factual contradiction: "The current policy is 15 minutes" vs. "The desk's rule is 20 minutes" | INT-01:P06, INT-01:P12 | Direct factual contradiction between two stakeholders (grace period value) | The two speakers give different values for the same rule, and I do not decide which is right; it goes to the lab manager as Q-1. A requirement that hard-coded either number would build one person's belief into the system, so the value must stay a configured setting. |
| 2 | Ambiguous statement 1: "If someone is only a little late, we try not to give the kit away." | INT-01:P07 | Ambiguity: vague amount of time | "A little late" has no number and may mean extra informal tolerance beyond the grace period. A developer could turn it into an invented extra buffer or ignore it, and neither choice comes from the interview. |
| 3 | Ambiguous statement 2: "They should get a message before it goes to the waitlist." | INT-01:P10 | Ambiguity: unclear who ("they") and unclear when ("before") | "They" could be the late borrower, the waitlisted student, or both, and the lead time is unstated. A notification requirement cannot be tested until the recipient and timing are named (Q-3). |
| 4 | Missing stakeholder: the equipment technicians | INT-01:P02, INT-01:P04, INT-01:P09, INT-01:P13, INT-01:P17, INT-01:P19, INT-01:P21 | Missing stakeholder (mentioned repeatedly, never interviewed) | The waitlist requirement depends on the technicians' preparation check, yet Jordan says "We have not asked them yet" (P19). Any design of how readiness is marked would be invented until they are interviewed (Q-2). |
| 5 | Compliment: "a reservation dashboard that fixed all of this would be amazing." | INT-01:P14 | Compliment (not evidence) | Praise for a hypothetical dashboard says nothing about what Priya actually does or needs. Treating it as demand would justify building a dashboard no evidence supports. |
| 6 | Prediction: "If there were a 'running late' button, I would probably use it every time I was delayed." | INT-01:P15 | Prediction about future use (not evidence of current behavior) | It describes what Priya thinks she would do, not what she has done, so it is recorded only as assumption A-1. Building a feature on it risks low real use. |
| 7 | Strongest past event: Priya's late pickup "last Thursday" | INT-01:P13 | Specific past event (strong evidence) | It gives a timed sequence (3:00 booking, 3:11 class end, 3:13 busy line, 3:16 arrival, 3:38 replacement kit) and a real cost, a late interview. It shows directly that release and readiness are different states and that the original borrower can arrive after release but before handoff. |

---

