---
name: review-practice-ticket
description: Review completed practice ticket solutions for correctness, test quality, edge-case coverage, algorithmic approach, and learning value. Use when the user says a practice problem, ticket, challenge, kata, LeetCode-style exercise, stats/math/finance/AI/ML basics exercise, or solution folder is done and wants a critical review.
---

# Review Practice Ticket

## Overview

Review the user's completed practice ticket like a rigorous programming coach
and code reviewer. Verify the implementation, tests, stated assumptions, and
problem-solving approach before accepting the ticket as done.

Do not edit implementation or test files during review unless the user
explicitly asks for edits. Explain failures and suggest fixes instead.

## Review Workflow

1. Locate the language project, implementation, and tests.
2. Read the original ticket from `practice-tickets.md` when available.
3. Identify the language, test command, and project layout.
4. Run the existing tests when feasible.
5. Inspect the solution for correctness, simplicity, and edge behavior.
6. Inspect the tests for meaningful coverage, not just passing examples.
7. Add temporary adversarial checks mentally or with local commands when useful.
8. Report findings before praise or summary.

Do not rewrite the solution or tests by default. Suggest targeted changes unless
the user explicitly asks for a reference implementation, direct code edits, or
test edits.

## Review Checklist

Check correctness:

- Does the implementation satisfy the ticket exactly?
- If multiple tickets share one topic file, did this change avoid breaking
  earlier ticket behavior?
- Are input/output shapes consistent with the ticket and tests?
- Are empty, invalid, tied, repeated, zero, negative, and decimal cases handled
  where relevant?
- Are domain rules correct for stats, math, finance, or ML terminology?
- Are floating-point comparisons handled with tolerance when needed?

Check tests:

- Is there at least one normal example test?
- Is there at least one minimal or single-value test?
- Is there at least one edge case?
- Is there at least one case involving repeated values, ties, zeros, missing
  values, negatives, or decimals if relevant?
- Is invalid input behavior tested if the ticket requires a decision?
- Would an obviously wrong solution still pass these tests?
- If helpers are shared across tickets, do tests cover the public ticket
  behavior rather than only the helper details?

Check approach:

- Is the solution simple enough for the ticket scope?
- Is the algorithm appropriate for the expected input size?
- Are names readable and domain concepts clear?
- Is there unnecessary abstraction?
- Is the user relying on library behavior without understanding the basic logic?

Check learning:

- Identify one concept the user seems to understand.
- Identify one gap, missed assumption, or habit to improve.
- Suggest at most one small follow-up exercise unless the user asks for more.

## Useful Properties

Use property-style checks when applicable:

- The mean of `[x]` is `x`.
- A range is never negative.
- Distances from the mean sum to approximately zero.
- Daily price changes have length `len(prices) - 1`.
- Accuracy is between `0` and `1`.
- A top-N function returns no more than `N` items.
- Missing-data counters should not count numeric zero unless explicitly chosen.
- A majority-class predictor must define tie and empty-input behavior.

## Response Format

Lead with findings, ordered by severity:

```txt
Findings
- High: ...
- Medium: ...
- Low: ...

Test Gaps
- ...

Verdict
- Not done yet / Accepted with caveats / Accepted

Next Rep
- ...
```

If there are no issues, say that clearly and mention any residual risk or
untested behavior. Keep the review concise but specific, with file and line
references when possible.
