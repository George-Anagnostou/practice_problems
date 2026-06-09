# Ticket 001: Mean Calculator

## Approach

Loop through the values, accumulate the total, then divide by the number of
values.

## Behavior Choices

- Empty input: raise `ValueError`.
- Decimal values: supported.

## Complexity

- Time: O(n)
- Space: O(1)

## Follow-Ups

- Compare this manual implementation with Python's standard library tools after
  the fundamentals version is reviewed.
