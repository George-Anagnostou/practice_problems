# finance basics

from typing import Tuple


def pnl(buy: int | float, sell: int | float) -> Tuple[int | float, float]:
    if buy <= 0:
        raise ValueError("invalid purchase price")
    profit = sell - buy
    ret = profit / buy
    return (profit, ret)
