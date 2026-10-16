# Ambiguity audit result

Tool: Claude (claude.ai), model Claude Opus 5.5, run once on 2026-10-15.
Prompt: `prompts/ambiguity_audit_prompt.txt`, used verbatim, with `transcripts/interview.txt` attached.

The complete model response follows, unedited.

---

**Requirements audit of INT-01 (8 findings)**

**1. Conflicting grace period value**
- Paragraphs: P06, P12
- Excerpt: "The current policy is 15 minutes after the reservation start." / "The desk's rule is 20 minutes."
- Defect type: Direct contradiction
- Unsafe decision: Any default or example grace value an implementer picks would silently choose one speaker's fact over the other.

**2. "Only a little late"**
- Paragraphs: P07
- Excerpt: "If someone is only a little late, we try not to give the kit away."
- Defect type: Ambiguity (vague quantity of time)
- Unsafe decision: It is unclear whether this describes extra informal tolerance beyond the grace period, so an implementer could not tell whether release at the grace boundary should be automatic, discretionary, or delayed.

**3. Unclear recipient of the pre-waitlist message**
- Paragraphs: P10
- Excerpt: "They should get a message before it goes to the waitlist."
- Defect type: Ambiguity (unclear referent)
- Unsafe decision: "They" could mean the late borrower, the waitlisted student, or both, and the message timing and channel are not given, so who is notified and when cannot be implemented safely.

**4. Equipment-technician readiness signal is undefined**
- Paragraphs: P09, P17, P19, P21
- Excerpt: "The equipment technicians need some way to mark the preparation step, but I cannot tell you what screen or workflow would work for them. We have not asked them yet."
- Defect type: Incompleteness (missing stakeholder input)
- Unsafe decision: How and when a kit becomes "ready" for the waitlist would have to be invented, because the people who perform the check were not consulted.

**5. Staff hold rules are incomplete**
- Paragraphs: P04, P19, P21
- Excerpt: "I wrote 'hold until 2:25' on the paper slip" / "Staff sometimes extend a reservation after a student contacts us"
- Defect type: Incompleteness
- Unsafe decision: The transcript does not say who may enter a hold, whether there is a maximum length, or what state the reservation enters exactly when the hold time is reached.

**6. "Release" as an automatic event or a staff action**
- Paragraphs: P06, P09
- Excerpt: "we can release the kit" / "We mark the reservation as released"
- Defect type: Ambiguity (unclear actor)
- Unsafe decision: It is unclear whether the system should release a reservation automatically when the grace period passes or only mark it as eligible for a staff member to release.

**7. Original borrower arriving after release but before handoff**
- Paragraphs: P13, P17
- Excerpt: "The reservation had already been released. A waitlisted student was there, but the kit was still behind the counter"
- Defect type: Incompleteness (missing rule for an observed case)
- Unsafe decision: There is no stated priority between the original borrower who arrives late and the waitlisted student when the released kit has not yet been handed out.

**8. "Checked in" versus "picked up"**
- Paragraphs: P02, P17, P21
- Excerpt: "mark the reservation picked up" / "If I have already checked in at the desk" / "a checked-in reservation should remain active"
- Defect type: Ambiguity (undefined term)
- Unsafe decision: It is not stated whether check-in is the same event as pickup or a separate earlier step, so an implementer could not tell when the "checked in" protection begins.
