"""Student acceptance tests for CS 690 Assignment 3.

Exactly three tests, one per acceptance criterion (AC-1, AC-2, AC-3).
Expected results come from the acceptance criteria in the report, not from
reading the reference code.

Chain (test -> AC -> requirement -> evidence):
- test_ac1_... -> AC-1 -> R-1 -> E-3; E-2
- test_ac2_... -> AC-2 -> R-2 -> E-4
- test_ac3_... -> AC-3 -> R-3 -> E-6; E-2
"""

from reference import can_offer_to_waitlist, reservation_disposition

# CONFIGURED VALUE for these tests only. This is NOT the lab's grace policy.
# The interview gives two conflicting values (15 minutes in INT-01:P06,
# 20 minutes in INT-01:P12), which is open question Q-1. The criteria are
# written in terms of the configured value G, so any G works here.
CONFIGURED_GRACE_MINUTES = 12


# AC-1 (R-1): after the configured grace period, with no check-in and no
# staff hold, the reservation becomes releasable.
def test_ac1_unchecked_reservation_without_hold_is_releasable_after_configured_grace() -> None:
    state = reservation_disposition(
        minutes_after_start=CONFIGURED_GRACE_MINUTES + 5,
        grace_minutes=CONFIGURED_GRACE_MINUTES,
        checked_in=False,
        staff_hold_until=None,
    )
    assert state == "releasable"


# AC-2 (R-2): a checked-in reservation stays active after the grace period.
def test_ac2_checked_in_reservation_stays_active_after_configured_grace() -> None:
    state = reservation_disposition(
        minutes_after_start=CONFIGURED_GRACE_MINUTES + 10,
        grace_minutes=CONFIGURED_GRACE_MINUTES,
        checked_in=True,
        staff_hold_until=None,
    )
    assert state == "active"


# AC-3 (R-3): a releasable kit whose preparation is not complete must not be
# offered to the waitlist.
def test_ac3_releasable_kit_not_offered_to_waitlist_before_preparation_complete() -> None:
    offerable = can_offer_to_waitlist(
        disposition="releasable",
        preparation_complete=False,
    )
    assert offerable is False
