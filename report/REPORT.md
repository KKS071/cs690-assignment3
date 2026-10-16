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

## Part 3. Requirements, INVEST, and acceptance criteria

### Four requirement slices

**R-1. Release only after the configured grace period**

- User story: As a checkout coordinator, I want a reservation with no check-in and no staff hold to become releasable only once the lab's configured grace period has passed, so that late students keep their kit during the grace period and the manager can change the policy without a code change.
- Structured requirement: When a reservation is not checked in and has no staff hold in effect, the system shall show its status as "held" while the minutes after the reservation start are less than the configured grace period G, and as "releasable" once the minutes after the start reach G. G is read from the lab's configuration; the system shall not contain a built-in grace value.
- Trace: E-3, E-2. The value of G is not settled (Q-1).

**R-2. Check-in and staff holds protect the reservation**

- User story: As a student borrower, I want my reservation to stay mine once I have checked in at the desk or staff have recorded a hold for me, so that it does not disappear just because the clock passed the grace window.
- Structured requirement: The system shall show a checked-in reservation as "active" at any time after its start, regardless of the grace period. For a reservation that is not checked in but has a recorded staff hold, the system shall show it as "held" while the current time is before the hold's recorded end time.
- Trace: E-4, E-5, E-1.

**R-3. Offer to the waitlist only when the kit is ready**

- User story: As a waitlisted student, I want to be offered a kit only when it is actually ready to hand out, so that I am not sent to the desk while the technicians are still checking or repacking it.
- Structured requirement: The system shall offer a kit to the waitlist only when its reservation status is "releasable" and the equipment technicians have recorded that its preparation is complete. A releasable kit without recorded preparation shall not be shown to the waitlist.
- Trace: E-6, E-2. How preparation is recorded is not settled (Q-2).

**R-4. Message before a kit goes to the waitlist**

- User story: As a student borrower who is running late, I want to receive a message before my kit is offered to the waitlist, so that I know whether I still have the reservation before I cross campus.
- Structured requirement: Before a kit is offered to the waitlist, the system shall send a message about the pending release to the configured recipient or recipients through the configured channel.
- Trace: **Assumption.** P10 says "they should get a message" but does not say who. Clarifying question (Q-3): In P10, who are "they" (the late borrower, the waitlisted student, or both), through which channel should the message go, and how long before the waitlist offer?

No requirement hard-codes 15 or 20 minutes; R-1 uses the configured value G.

### INVEST check

| Requirement | I | N | V | E | S | T | Named problem for any fail |
| --- | --- | --- | --- | --- | --- | --- | --- |
| R-1 | Pass | Pass | Pass | Pass | Pass | Pass | None |
| R-2 | Pass | Pass | Pass | Pass | Pass | Pass | None |
| R-3 | Fail | Pass | Pass | Pass | Pass | Pass | I: couples the waitlist offer to a technician preparation-marking workflow that has not been designed or discussed with the technicians (Q-2). |
| R-4 | Fail | Pass | Pass | Fail | Pass | Fail | I: couples the message to R-3's waitlist-offer event, so it cannot ship before R-3. E: recipient, channel and lead time are unknown (Q-3), so the work cannot be sized. T: with no recipient or lead time defined, there is no pass/fail threshold to test against. |

### Three acceptance criteria

**AC-1 (R-1)**
- Given the lab's configured grace period is G minutes, the borrower has not checked in, and no staff hold is recorded,
- When the desk checks the reservation's status at G + 5 minutes after the reservation start,
- Then the status is "releasable".

**AC-2 (R-2)**
- Given the lab's configured grace period is G minutes, the borrower has checked in at the desk, and no staff hold is recorded,
- When the desk checks the reservation's status at G + 10 minutes after the reservation start,
- Then the status is "active".

**AC-3 (R-3)**
- Given a reservation whose status is "releasable" and the equipment technicians have not recorded that the kit's preparation is complete,
- When the desk checks whether the kit can be offered to the waitlist,
- Then the kit is not offered to the waitlist (the check returns false).

None of the criteria picks a grace value, decides exactly when a staff hold ends, or decides how technicians mark preparation. AC-1 and AC-2 use the configured value G, and both check times stay away from the exact grace boundary.

---

## Part 4. Implementation-ready specification

(Same content as `spec/spec_template.md` in the repository.)

### Selected requirement

Requirement ID: R-3 (offer a kit to the waitlist only when it is releasable and preparation is complete)
Evidence trace: E-6 (INT-01:P09, INT-01:P21), E-2 (INT-01:P13); related open questions Q-1, Q-2, Q-3

### Behavior and scope

Given a reservation's release status and whether the equipment technicians have recorded that the kit's preparation is complete, decide whether the kit may be offered to the waitlist. The kit may be offered only when the reservation is `"releasable"` and preparation is recorded complete. A release decision alone is never enough. This specification covers only that yes/no decision. It does not compute the release status (R-1, R-2), notify anyone (R-4), or pick a waitlisted student.

### Typed interface or function signature

```python
from typing import Literal

Disposition = Literal["active", "held", "releasable"]


def can_offer_to_waitlist(
    *,
    disposition: Disposition,
    preparation_complete: bool,
) -> bool:
    """Return True only if this kit may be offered to the waitlist now."""
    ...
```

### Preconditions

1. `disposition` is exactly one of `"active"`, `"held"`, or `"releasable"`, and was computed for this reservation under R-1 and R-2 using the lab's configured grace value, not a value chosen by the caller.
2. `preparation_complete` is `True` only if the equipment technicians have recorded that preparation of this specific kit is complete for the next checkout. The caller must not infer it from elapsed time, from the release itself, or from the kit's shelf location.
3. Both arguments are passed by name.

### Postconditions

1. The return value is a `bool`.
2. It returns `True` if and only if `disposition == "releasable"` and `preparation_complete is True`.
3. It returns `False` whenever `disposition` is `"active"` or `"held"`, whatever the value of `preparation_complete`.
4. It returns `False` when `disposition` is `"releasable"` and `preparation_complete` is `False`.
5. A `disposition` outside the three allowed values raises `ValueError` and returns nothing.
6. The call has no side effects: it does not change the reservation's status, record or clear preparation, send a message, or select a waitlisted student.

### Invariant

At every moment, the kits visible to the waitlist are only kits whose reservation is currently `"releasable"` and whose preparation is currently recorded complete; if either condition stops being true (for example, the original borrower checks in or staff record a hold), the kit stops being offerable on the next evaluation.

### Edge cases

1. The reservation is releasable but the technicians are still checking the kit while a waitlisted student is already at the counter (INT-01:P09, INT-01:P13). The result must be `False`.
2. The technicians packed the kit early, so preparation is complete, but the reservation is still `"held"` within the grace period or under a staff hold (INT-01:P04). The result must be `False`.
3. The original borrower arrives after the reservation became releasable but before the kit is handed out (INT-01:P13), and is then checked in or given a staff hold. The new status is no longer `"releasable"`, so the result must be `False`; the caller must re-evaluate rather than reuse an earlier `True`.
4. The caller passes the word the desk uses on paper, `"released"` (INT-01:P09), which is not one of the three statuses. This must raise `ValueError`, not be treated as `"releasable"`.

### Non-goal

This specification does not choose which waitlisted student receives the kit or the order of the waitlist.

### Settled decisions

1. A release decision alone does not make a kit available; the waitlist may only see equipment that is actually ready to hand out (E-6: INT-01:P09, INT-01:P21; observed in E-2: INT-01:P13).
2. A checked-in reservation stays active, so its kit is never offered to the waitlist (E-4: INT-01:P17, INT-01:P21).
3. A reservation under a recorded staff hold is not released, so its kit is not offered (E-5: INT-01:P04, INT-01:P06, INT-01:P19).
4. The grace value is a configured input decided by the lab; this function never chooses or assumes one (E-3: INT-01:P06, INT-01:P21).

### Open questions the implementation agent may not answer

The implementation agent must not answer any of these by guessing, by picking a "reasonable default", or by encoding an example value. Each one is passed to the named owner, and until it is answered the code takes the value as an input or leaves the behavior out.

1. Q-2 (equipment technicians): How do technicians record that preparation is complete, who may record or undo it, and what does "ready" cover (battery, accessories matching the reservation, moving the kit from the pickup shelf; INT-01:P09, INT-01:P19)? The technicians were never interviewed (INT-01:P19, INT-01:P21).
2. Q-1 (lab manager): Is the grace period 15 minutes (INT-01:P06) or 20 minutes (INT-01:P12)? It affects when a status becomes `"releasable"` and must stay a configured value.
3. Q-3 (checkout coordinator / lab manager): Must a message be sent before a kit is offered to the waitlist, to whom, through which channel, and how long before (INT-01:P10)? This function must not wait for, send, or assume such a message.
4. Lab manager: If the original borrower arrives after the reservation became releasable but before the kit is handed out, does the borrower have priority over the waitlisted student (INT-01:P13, INT-01:P17)?
5. Lab manager: What status does a reservation enter at the exact moment a staff hold ends, and is there a maximum hold length (INT-01:P04, INT-01:P21)?

---

## Part 5. Tests

All three tests are in `tests/test_student_acceptance.py`. They call only `reservation_disposition` and `can_offer_to_waitlist` with named arguments. The grace period is in the named constant `CONFIGURED_GRACE_MINUTES = 12`, marked in the file as a configured value for the tests and not the lab's policy (see Q-1). Expected values come from the criteria above, not from the reference code. `reference/` and `tests/test_reference_smoke.py` were not edited.

| Test name | AC ID | Requirement ID | Evidence ID |
| --- | --- | --- | --- |
| test_ac1_unchecked_reservation_without_hold_is_releasable_after_configured_grace | AC-1 | R-1 | E-3; E-2 |
| test_ac2_checked_in_reservation_stays_active_after_configured_grace | AC-2 | R-2 | E-4 |
| test_ac3_releasable_kit_not_offered_to_waitlist_before_preparation_complete | AC-3 | R-3 | E-6; E-2 |

How each test maps to its criterion:

- AC-1: Given G = `CONFIGURED_GRACE_MINUTES`, `checked_in=False`, `staff_hold_until=None`; When `minutes_after_start = G + 5`; Then asserts the result is `"releasable"`.
- AC-2: Given G = `CONFIGURED_GRACE_MINUTES`, `checked_in=True`, `staff_hold_until=None`; When `minutes_after_start = G + 10`; Then asserts the result is `"active"`.
- AC-3: Given `disposition="releasable"`, `preparation_complete=False`; When `can_offer_to_waitlist` is called; Then asserts the result `is False`.

All three tests passed on the first run, so no criterion or expected value was changed.

Final `python -m pytest -q` output:

```text
....                                                                     [100%]
4 passed in 0.02s
```

(Four tests: the provided smoke test plus my three acceptance tests.)

---

