import pytest

from practice.finance_basics import (
    pnl,
    portfolio_weights,
    Position,
    portfolio_value,
    price_change,
)


# profit or loss
def test_pnl_positive_return():
    assert pnl(100, 115) == (15, 0.15)


def test_pnl_negative_return():
    assert pnl(100, 95) == (-5, -0.05)


def test_pnl_zero_return():
    assert pnl(100, 100) == (0, 0)


def test_pnl_decimal():
    assert pnl(123.45, 32.34) == (-91.11, pytest.approx(-0.7380315917375455))


def test_pnl_total_loss():
    assert pnl(100, 0) == (-100, -1)


def test_pnl_buy_price_is_zero():
    with pytest.raises(ValueError, match="invalid purchase price"):
        pnl(0, 100)


def test_pnl_negative_buy_price_is_invalid():
    with pytest.raises(ValueError, match="invalid purchase price"):
        pnl(-100, 120)


# test portfolio value
def test_portfolio_value_one_holding():
    assert portfolio_value([Position("AAPL", 2, 200)]) == 400


def test_portfolio_value_multiple_holdings():
    assert portfolio_value([Position("AAPL", 2, 200), Position("MSFT", 1, 300)]) == 700


def test_portfolio_value_zero_shares():
    assert portfolio_value([Position("AAPL", 0, 100)]) == 0


def test_portfolio_value_multi_holding_zero_shares():
    assert (
        portfolio_value(
            [
                Position("AAPL", 0, 100),
                Position("MSFT", 2, 200),
            ]
        )
        == 400
    )


def test_portfolio_value_decimal_price():
    assert portfolio_value([Position("AAPL", 1, 110.25)]) == 110.25


def test_portfolio_value_decimal_quantity():
    assert portfolio_value([Position("AAPL", 1.5, 200)]) == 300.0


def test_portfolio_value_decimal_price_quantity():
    assert portfolio_value([Position("AAPL", 1.5, 123.45)]) == pytest.approx(185.175)


def test_portfolio_value_empty():
    assert portfolio_value([]) == 0


# test portfolio weights
def test_portfolio_weights_multiple_holdings():
    weights = portfolio_weights(
        [
            Position("AAPL", 2, 200),
            Position("MSFT", 1, 300),
        ]
    )

    assert weights["AAPL"] == pytest.approx(400 / 700)
    assert weights["MSFT"] == pytest.approx(300 / 700)


def test_portfolio_weights_sum_to_one():
    weights = portfolio_weights(
        [
            Position("AAPL", 2, 200),
            Position("MSFT", 1, 300),
        ]
    )

    assert sum(weights.values()) == pytest.approx(1)


def test_portfolio_weights_empty_portfolio():
    with pytest.raises(ValueError, match="empty portfolio"):
        portfolio_weights([])


def test_portfolio_weights_non_empty_zero_portfolio():
    with pytest.raises(ValueError, match="zero balance portfolio"):
        portfolio_weights([Position("AAPL", 0, 100)])


def test_portfolio_weights_multiple_holdings_some_zero():
    weights = portfolio_weights(
        [
            Position("AAPL", 0, 100),
            Position("MSFT", 1, 200),
        ]
    )

    assert weights["AAPL"] == 0
    assert weights["MSFT"] == 1


def test_portfolio_weights_duplicate_holdings():
    weights = portfolio_weights(
        [
            Position("AAPL", 1, 100),
            Position("AAPL", 1, 100),
            Position("MSFT", 1, 200),
        ]
    )

    assert weights["AAPL"] == 0.5
    assert weights["MSFT"] == 0.5


# test daily price changes
def test_price_change():
    assert price_change([100, 105, 103, 110]) == [5, -2, 7]


def test_price_change_increasing():
    assert price_change([100, 102, 110, 113]) == [2, 8, 3]


def test_price_change_decreasing():
    assert price_change([100, 99, 88, 8]) == [-1, -11, -80]


def test_price_change_repeating():
    assert price_change([100, 101, 101, 102]) == [1, 0, 1]


def test_price_change_no_prices():
    assert price_change([]) == []


def test_price_change_one_price():
    assert price_change([1]) == []
