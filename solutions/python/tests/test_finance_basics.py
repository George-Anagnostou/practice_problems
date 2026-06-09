import pytest

from practice.finance_basics import pnl


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
