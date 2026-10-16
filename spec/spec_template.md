# Implementation-ready specification

## Selected requirement

Requirement ID: R-3 (offer a kit to the waitlist only when it is releasable and preparation is complete)
Evidence trace: E-6 (INT-01:P09, INT-01:P21), E-2 (INT-01:P13); related open questions Q-1, Q-2, Q-3

## Behavior and scope

Given a reservation's release status and whether the equipment technicians have recorded that the kit's preparation is complete, decide whether the kit may be offered to the waitlist. The kit may be offered only when the reservation is `"releasable"` and preparation is recorded complete. A release decision alone is never enough. This specification covers only that yes/no decision. It does not compute the release status (R-1, R-2), notify anyone (R-4), or pick a waitlisted student.

## Typed interface or function signature

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

## Preconditions

1. `disposition` is exactly one of `"active"`, `"held"`, or `"releasable"`, and was computed for this reservation under R-1 and R-2 using the lab's configured grace value, not a value chosen by the caller.
2. `preparation_complete` is `True` only if the equipment technicians have recorded that preparation of this specific kit is complete for the next checkout. The caller must not infer it from elapsed time, from the release itself, or from the kit's shelf location.
3. Both arguments are passed by name.

## Postconditions

1. The return value is a `bool`.
2. It returns `True` if and only if `disposition == "releasable"` and `preparation_complete is True`.
3. It returns `False` whenever `disposition` is `"active"` or `"held"`, whatever the value of `preparation_complete`.
4. It returns `False` when `disposition` is `"releasable"` and `preparation_complete` is `False`.
5. A `disposition` outside the three allowed values raises `ValueError` and returns nothing.
6. The call has no side effects: it does not change the reservation's status, record or clear preparation, send a message, or select a waitlisted student.

## Invariant

At every moment, the kits visible to the waitlist are only kits whose reservation is currently `"releasable"` and whose preparation is currently recorded complete; if either condition stops being true (for example, the original borrower checks in or staff record a hold), the kit stops being offerable on the next evaluation.

## Edge cases

1. The reservation is releasable but the technicians are still checking the kit while a waitlisted student is already at the counter (INT-01:P09, INT-01:P13). The result must be `False`.
2. The technicians packed the kit early, so preparation is complete, but the reservation is still `"held"` within the grace period or under a staff hold (INT-01:P04). The result must be `False`.
3. The original borrower arrives after the reservation became releasable but before the kit is handed out (INT-01:P13), and is then checked in or given a staff hold. The new status is no longer `"releasable"`, so the result must be `False`; the caller must re-evaluate rather than reuse an earlier `True`.
4. The caller passes the word the desk uses on paper, `"released"` (INT-01:P09), which is not one of the three statuses. This must raise `ValueError`, not be treated as `"releasable"`.

## Non-goal

This specification does not choose which waitlisted student receives the kit or the order of the waitlist.

## Settled decisions

1. A release decision alone does not make a kit available; the waitlist may only see equipment that is actually ready to hand out (E-6: INT-01:P09, INT-01:P21; observed in E-2: INT-01:P13).
2. A checked-in reservation stays active, so its kit is never offered to the waitlist (E-4: INT-01:P17, INT-01:P21).
3. A reservation under a recorded staff hold is not released, so its kit is not offered (E-5: INT-01:P04, INT-01:P06, INT-01:P19).
4. The grace value is a configured input decided by the lab; this function never chooses or assumes one (E-3: INT-01:P06, INT-01:P21).

## Open questions the implementation agent may not answer

The implementation agent must not answer any of these by guessing, by picking a "reasonable default", or by encoding an example value. Each one is passed to the named owner, and until it is answered the code takes the value as an input or leaves the behavior out.

1. Q-2 (equipment technicians): How do technicians record that preparation is complete, who may record or undo it, and what does "ready" cover (battery, accessories matching the reservation, moving the kit from the pickup shelf; INT-01:P09, INT-01:P19)? The technicians were never interviewed (INT-01:P19, INT-01:P21).
2. Q-1 (lab manager): Is the grace period 15 minutes (INT-01:P06) or 20 minutes (INT-01:P12)? It affects when a status becomes `"releasable"` and must stay a configured value.
3. Q-3 (checkout coordinator / lab manager): Must a message be sent before a kit is offered to the waitlist, to whom, through which channel, and how long before (INT-01:P10)? This function must not wait for, send, or assume such a message.
4. Lab manager: If the original borrower arrives after the reservation became releasable but before the kit is handed out, does the borrower have priority over the waitlisted student (INT-01:P13, INT-01:P17)?
5. Lab manager: What status does a reservation enter at the exact moment a staff hold ends, and is there a maximum hold length (INT-01:P04, INT-01:P21)?
