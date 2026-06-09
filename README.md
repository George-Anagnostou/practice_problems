# Practice Problems

Basic practice problems for getting reps with different languages, techniques,
domains, and stacks.

The goal is simple: solve small challenges consistently, write enough tests to
prove the solution, and keep short notes about what was learned.

## Assistant Role

This is a human-practice repo. The human writes implementation and test code.
Codex or any AI assistant should review, audit, explain, organize, and suggest.

Project assistant rules live in `AGENTS.md`. Most importantly:

- Do not edit implementation code unless explicitly asked.
- Do not edit test code unless explicitly asked.
- When code or tests fail, explain the issue and suggest the smallest fix
  before making changes.

## Repository Structure

```txt
practice-tickets.md
solutions/
  INDEX.md
  _language-template/
  <language>/
    README.md
    language config files, if needed
    src or package directory
      stats_basics.<ext>
      finance_basics.<ext>
      ml_basics.<ext>
      research_data_basics.<ext>
    tests/
      test_stats_basics.<ext>
      test_finance_basics.<ext>
      test_ml_basics.<ext>
      test_research_data_basics.<ext>
    notes/
      ticket-001-mean-calculator.md
skills/
  review-practice-ticket/
    SKILL.md
```

Examples:

```txt
solutions/python/practice/stats_basics.py
solutions/python/tests/test_stats_basics.py
solutions/typescript/src/stats-basics.ts
solutions/go/stats_basics.go
```

Use any language and any number of tickets. Each language folder should be one
small project. Tickets are usually functions inside topic files, not separate
folders.

## Language Project Convention

Each language folder should contain:

- `README.md`: how to run tests and how that language project is organized.
- source files grouped by topic, such as `stats_basics` or `finance_basics`.
- `tests/`: grouped tests matching the topic files.
- `notes/`: short per-ticket notes about assumptions, mistakes, and follow-ups.

Use `src/` only when it fits the language or tooling. For Python, this repo uses
a simple root package with one `uv` project in `solutions/python`.

For quick setup, copy the structure from `solutions/_language-template/`.

For Python, run all ticket tests from `solutions/python`:

```sh
uv run pytest
```

Do not create a separate `uv` project per ticket. Add new Python tickets to the
existing Python project, add tests under `solutions/python/tests`, and let the
single `pyproject.toml` handle shared tooling like `pytest`.

## Combining Tickets

Related tickets should often live in the same program:

```txt
stats_basics: tickets 1-5
finance_basics: tickets 6-10
ml_basics: tickets 11-15
research_data_basics: tickets 16-20
```

This makes it easy to share helper functions within a language while keeping
the repo flatter than one-folder-per-ticket.

## Practice Loop

1. Pick one ticket from `practice-tickets.md`.
2. Pick one language.
3. Add or update the relevant topic file under `solutions/<language>/`.
4. Add or update the matching test file.
5. Decide edge behavior before coding.
6. Write 3-5 tests.
7. Implement the smallest correct solution.
8. Run the tests.
9. Ask Codex to review the completed ticket.
10. Update `notes/ticket-###-slug.md` with mistakes, edge cases, and follow-ups.

Keep each challenge scoped to 30-60 minutes. Prefer finishing a small ticket
cleanly over expanding the problem.

## Language Selection

Use Python as the default for statistics, math, finance, and AI/ML practice.
It is fast to test and maps naturally to later data work.

Use another language when you have a specific reason:

- `typescript`: frontend/backend practice, typed application code.
- `go`: simple CLIs, services, explicit error handling.
- `sql`: table-shaped data questions.
- `rust` or `cpp`: performance, memory, and lower-level fundamentals.

A good starting rhythm:

```txt
Tickets 1-10: Python
Tickets 1-5 again: TypeScript or Go
Tickets 11-20: Python
Then revisit selected tickets in a second language
```

## Review Workflow

When a ticket feels complete, ask:

```txt
Use skills/review-practice-ticket to review Ticket 001 in solutions/python.
Check correctness, tests, edge cases, and approach.
```

The review should be critical. The point is not to rubber-stamp the solution;
the point is to prove the answer is correct, find missing cases, and improve
your problem-solving habits.
