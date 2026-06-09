# Practice Tickets

Small programming challenges for fundamentals practice. These are language-agnostic and intentionally scoped for roughly 30-60 minutes each. For every ticket, write a small solution and at least 3-5 tests before moving on.

## Suggested Workflow

1. Restate the problem in your own words.
2. Write down 2-3 example inputs and expected outputs by hand.
3. Implement the simplest version that solves only those examples.
4. Add edge-case tests.
5. Refactor only after the tests pass.
6. Write a short note explaining the approach and any assumptions.

## Testing Checklist

For each ticket, try to include:

- One normal case.
- One small/minimal case.
- One edge case.
- One case with repeated values, missing values, ties, or zeros if relevant.
- One case that should fail or return an empty result if relevant.

## Statistics Basics

### Ticket 1: Mean Calculator

Given a list of numbers, calculate the average.

Example:

```txt
input:  [2, 4, 6, 8]
output: 5
```

Practice: loops, sums, division.

Tests to consider:

- Multiple positive numbers.
- A single number.
- Numbers including zero.
- Negative numbers.
- Empty list behavior: decide whether to return null, throw an error, or print a message.

Stretch: support decimal numbers.

### Ticket 2: Above Average Counter

Given a list of numbers, count how many are above the average.

Example:

```txt
input:  [10, 20, 30, 40]
output: 2
```

Practice: helper functions, comparisons, loops.

Tests to consider:

- Some numbers above average.
- No numbers above average.
- Repeated values.
- Negative values.
- Single-value list.

Stretch: return both the average and the count.

### Ticket 3: Min, Max, and Range

Given a list of numbers, find the minimum, maximum, and range.

Example:

```txt
input:  [3, 10, 17, 8]
output: min: 3, max: 17, range: 14
```

Practice: tracking values while looping.

Tests to consider:

- Unsorted numbers.
- Already sorted numbers.
- All values equal.
- Negative numbers.
- Single-value list.

Stretch: do it in one pass through the list.

### Ticket 4: Distance From Mean

Given a list of numbers, calculate how far each number is from the mean.

Example:

```txt
input:  [8, 10, 12]
output: [-2, 0, 2]
```

Practice: basic variability, list transformation.

Tests to consider:

- Symmetric numbers.
- Decimal mean.
- Negative numbers.
- All values equal.
- Single-value list.

Stretch: calculate absolute distance from the mean too.

### Ticket 5: Most Common Value

Given a list, return the most common item.

Example:

```txt
input:  ["A", "B", "A", "C", "A"]
output: "A"
```

Practice: dictionaries/maps, counting, tie behavior.

Tests to consider:

- Clear most common value.
- Tie between values.
- One item.
- Empty list.
- Case sensitivity, such as `"A"` versus `"a"`.

Stretch: return all tied values.

## Finance Basics

### Ticket 6: Profit or Loss

Given a buy price and sell price, calculate profit/loss and percentage return.

Example:

```txt
buy:    100
sell:   115
output: profit: 15, return: 15%
```

Practice: arithmetic, percentages, formatting.

Tests to consider:

- Positive return.
- Negative return.
- Zero return.
- Decimal prices.
- Buy price of zero: decide how to handle invalid input.

Stretch: include quantity of shares.

### Ticket 7: Portfolio Value

Given share counts and current prices, calculate total portfolio value.

Example:

```txt
AAPL: 2 shares at 200
MSFT: 1 share at 300
output: 700
```

Practice: structured data, loops, multiplication, aggregation.

Tests to consider:

- Multiple holdings.
- One holding.
- Zero shares.
- Decimal share counts.
- Empty portfolio.

Stretch: return each holding's percentage of the portfolio.

### Ticket 8: Daily Price Changes

Given prices over time, calculate day-to-day price changes.

Example:

```txt
input:  [100, 105, 103, 110]
output: [5, -2, 7]
```

Practice: indexing adjacent values.

Tests to consider:

- Increasing prices.
- Decreasing prices.
- Mixed changes.
- Repeated prices.
- One price or no prices.

Stretch: calculate percentage changes.

### Ticket 9: Best and Worst Day

Given daily returns, find the best and worst return.

Example:

```txt
input:  [0.01, -0.03, 0.02, 0.005]
output: best: 0.02, worst: -0.03
```

Practice: min/max with finance meaning.

Tests to consider:

- Mixed positive and negative returns.
- All positive returns.
- All negative returns.
- All returns equal.
- Single return.

Stretch: return the index or date of the best and worst day.

### Ticket 10: Simple Savings Growth

Given starting money, monthly contribution, and number of months, calculate final savings without interest.

Example:

```txt
start:   100
monthly: 50
months:  6
output:  400
```

Practice: loops or formulas, multiplication, validation.

Tests to consider:

- Normal savings growth.
- Zero months.
- Zero monthly contribution.
- Negative starting value.
- Decimal contribution.

Stretch: add fixed monthly interest.

## AI and ML Basics

### Ticket 11: Class Count

Given labeled examples, count how many examples belong to each class.

Example:

```txt
input:  ["spam", "not_spam", "spam", "spam"]
output: spam: 3, not_spam: 1
```

Practice: labels, dictionaries/maps, counting.

Tests to consider:

- Two classes.
- More than two classes.
- One class.
- Empty input.
- Case sensitivity.

Stretch: return class percentages.

### Ticket 12: Majority Class Predictor

Given training labels, always predict the most common label.

Example:

```txt
training: ["cat", "dog", "cat", "cat"]
output:   "cat"
```

Practice: baseline models, reuse of counting logic.

Tests to consider:

- Clear majority.
- Tie.
- One label.
- Empty labels.
- Non-string labels if your language supports them.

Stretch: use the predictor to classify a list of unknown examples.

### Ticket 13: Prediction Accuracy

Given true labels and predicted labels, calculate how many were correct.

Example:

```txt
true:      ["cat", "dog", "cat"]
predicted: ["cat", "cat", "cat"]
output:    accuracy: 2/3
```

Practice: comparing two lists, counting, ratios.

Tests to consider:

- Some correct predictions.
- All correct predictions.
- No correct predictions.
- Empty lists.
- Lists of different lengths: decide whether this is invalid input.

Stretch: return both fraction and decimal accuracy.

### Ticket 14: Keyword Classifier

Classify a message as `"finance"` if it contains words like `"stock"`, `"price"`, or `"market"`.

Example:

```txt
input:  "the stock price went up"
output: "finance"
```

Practice: strings, simple rules, classification.

Tests to consider:

- Message with one keyword.
- Message with multiple keywords.
- Message with no keywords.
- Different capitalization.
- Keyword embedded in another word, such as `"stockpile"`.

Stretch: support multiple categories with different keyword lists.

### Ticket 15: Closest Number

Given a target number and a list, find the closest number.

Example:

```txt
target: 10
values: [3, 8, 12, 20]
output: 8 or 12
```

Practice: distance, absolute value, tie behavior.

Tests to consider:

- Clear closest number.
- Tie between two values.
- Negative numbers.
- Exact match.
- Empty list.

Stretch: return the distance too.

## Research and Data Basics

### Ticket 16: Word Counter

Given a short paragraph, count how many times each word appears.

Example:

```txt
input: "markets move when markets expect change"
output: markets: 2, move: 1, when: 1, expect: 1, change: 1
```

Practice: tokenization, dictionaries/maps, normalization.

Tests to consider:

- Repeated words.
- Different capitalization.
- Punctuation.
- Empty string.
- Extra spaces.

Stretch: ignore common stop words such as `"the"` and `"and"`.

### Ticket 17: Find Papers by Keyword

Given a list of paper titles, return titles containing a search word.

Example:

```txt
search: "risk"
titles: ["Market Risk Models", "Neural Networks", "Credit Risk"]
output: ["Market Risk Models", "Credit Risk"]
```

Practice: filtering, strings, case normalization.

Tests to consider:

- Multiple matches.
- One match.
- No matches.
- Different capitalization.
- Search term embedded in another word.

Stretch: search both title and abstract.

### Ticket 18: Sort Experiments by Score

Given experiment names and scores, sort from best to worst.

Example:

```txt
model_a: 0.72
model_b: 0.81
model_c: 0.65
output: model_b, model_a, model_c
```

Practice: sorting structured data.

Tests to consider:

- Distinct scores.
- Tied scores.
- Negative scores.
- One experiment.
- Empty experiment list.

Stretch: return only experiments above a threshold.

### Ticket 19: Missing Data Counter

Given rows of data, count how many missing values appear.

Example:

```txt
input:  [10, "", 12, "", 15]
output: missing: 2
```

Practice: data cleaning, conditionals, counting.

Tests to consider:

- Empty strings.
- Null/nil/None values if available.
- Zero values, which should usually not count as missing.
- No missing values.
- All missing values.

Stretch: support rows and columns, then report missing count per column.

### Ticket 20: Top 3 Ranking

Given items with scores, return the top 3.

Example:

```txt
A: 50
B: 80
C: 65
D: 90
output: D, B, C
```

Practice: sorting, ranking, slicing.

Tests to consider:

- More than three items.
- Exactly three items.
- Fewer than three items.
- Tied scores.
- Negative scores.

Stretch: make `N` configurable instead of always returning 3.

## How To Verify Your Work

Use three layers of verification:

1. Example tests: the obvious examples from the ticket.
2. Edge tests: small, empty, tied, zero, negative, repeated, or invalid inputs.
3. Property checks: facts that should always be true.

Examples of useful properties:

- The mean of `[x]` should be `x`.
- The range should never be negative.
- The number of daily price changes should be one less than the number of prices.
- Accuracy should always be between `0` and `1`.
- A top-3 function should never return more than 3 items.
- A missing-data counter should not count numeric zero as missing unless you explicitly choose that rule.

## How To Know Whether Your Tests Are Sufficient

Your tests are probably good enough for these small tickets when:

- They cover the normal case.
- They cover at least one edge case.
- They cover the most likely mistake you personally might make.
- They force you to define ambiguous behavior, such as ties or empty input.
- They would fail if you hard-coded the example output.

For each ticket, write a short "test notes" section:

```txt
Assumptions:
- Empty input returns an error.
- Ties return the first matching item.
- Matching is case-insensitive.

Cases tested:
- Normal case.
- Empty input.
- Tie case.
- Repeated values.
```

## How To Generate Mock Input

Start with hand-written inputs first. Random data is useful only after you understand the expected behavior.

Use this progression:

1. Tiny hand-made data: 1-5 values where you can calculate the answer mentally.
2. Medium hand-made data: 5-20 values with repeated values, negatives, zeros, or ties.
3. Random generated data: useful for stress testing, not for proving correctness by itself.
4. Known properties: check facts that must always be true, even if you do not know the exact answer ahead of time.

Mock data patterns to reuse:

- Empty: `[]`
- Single value: `[5]`
- All same: `[4, 4, 4]`
- Increasing: `[1, 2, 3, 4]`
- Decreasing: `[4, 3, 2, 1]`
- Mixed signs: `[-3, 0, 2, 8]`
- Repeated labels: `["A", "B", "A", "C"]`
- Ties: `["A", "B", "A", "B"]`
- Missing values: `[10, "", 12, null, 0]`

## Review Workflow With Codex

When you finish a ticket, ask for a review like this:

```txt
I solved Ticket 8 in Go. Please review my solution and tests. Focus on correctness, edge cases, and whether the tests are sufficient.
```

Include or point to:

- The ticket number.
- The language used.
- The solution file.
- The test file.
- Any assumptions you made.

The review should check:

- Whether the implementation matches the ticket.
- Whether edge cases are defined and tested.
- Whether expected outputs are mathematically correct.
- Whether tests can catch realistic bugs.
- Whether the code is more complicated than the problem requires.

