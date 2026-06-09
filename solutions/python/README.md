# Python Solutions

This is one small Python project for many tickets.

Run tests from this directory:

```sh
uv run pytest
```

`pytest` is configured in `pyproject.toml`. Use this single Python project for
all Python tickets instead of creating a separate environment per ticket.

## Layout

```txt
practice/
  stats_basics.py
  finance_basics.py
  ml_basics.py
  research_data_basics.py
tests/
  test_stats_basics.py
  test_finance_basics.py
  test_ml_basics.py
  test_research_data_basics.py
```

Group related tickets in the same module. For example, Tickets 1-5 can live in
`practice/stats_basics.py` with corresponding tests in
`tests/test_stats_basics.py`.
