# finance basics

from dataclasses import dataclass


def pnl(buy: int | float, sell: int | float) -> tuple[int | float, float]:
    if buy <= 0:
        raise ValueError("invalid purchase price")
    profit = sell - buy
    ret = profit / buy
    return (profit, ret)


@dataclass
class Position:
    ticker: str
    quantity: float
    price: float


def portfolio_value(portfolio: list[Position]) -> float:
    total = 0
    for position in portfolio:
        total += position.price * position.quantity
    return total


def portfolio_weights(portfolio: list[Position]) -> dict[str, float]:
    if len(portfolio) == 0:
        raise ValueError("empty portfolio")

    weights = {}
    total_value = portfolio_value(portfolio)

    if total_value == 0:
        raise ValueError("zero balance portfolio")

    for position in portfolio:
        weight = (position.price * position.quantity) / total_value
        weights[position.ticker] = weights.get(position.ticker, 0) + weight

    return weights


def price_change(prices: list[int | float]) -> list[int | float]:
    if len(prices) <= 1:
        return []

    last_price = prices[0]
    changes = []
    for price in prices[1:]:
        change = price - last_price
        changes.append(change)
        last_price = price

    return changes
