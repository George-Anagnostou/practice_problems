# Language Solutions

This folder is one small project for many tickets in one language.

## Run Tests

```sh
replace with this language's test command
```

Prefer one dependency/test setup per language folder. Do not create a separate
project for every ticket unless the ticket genuinely needs isolated tooling.

## Layout

```txt
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
```

Group related tickets together. Add new files only when a domain or topic gets
large enough to deserve one.
