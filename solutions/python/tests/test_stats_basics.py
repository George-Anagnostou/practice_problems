import pytest

from practice.stats_basics import calculate_mean, above_average_count


# test mean calculator
def test_mean_multiple_positive_numbers():
    assert calculate_mean([2, 4, 6, 8]) == 5


def test_mean_single_number_returns_that_number():
    assert calculate_mean([42]) == 42


def test_mean_numbers_including_zero():
    assert calculate_mean([0, 10, 20]) == 10


def test_mean_negative_numbers():
    assert calculate_mean([-10, -5, 0, 5]) == -2.5


def test_mean_decimal_numbers():
    assert calculate_mean([1.5, 2.5, 3.5]) == pytest.approx(2.5)


def test_mean_empty_list_raises_value_error():
    with pytest.raises(ValueError, match="empty list"):
        calculate_mean([])


# test above average calculator
def test_above_average_count_multiple_positive_numbers():
    assert above_average_count([10, 20, 30, 40]) == 2


def test_above_average_count_single_number_returns_0():
    assert above_average_count([10]) == 0


def test_above_average_count_repeated_values_returns_0():
    assert above_average_count([10, 10, 10]) == 0


def test_above_average_count_negative_numbers():
    assert above_average_count([-40, -30, -20, -10]) == 2


def test_above_average_count_decimal_numbers():
    assert above_average_count([1.5, 2.5, 3.5]) == 1


def test_above_average_count_raises_value_error():
    with pytest.raises(ValueError, match="empty list"):
        above_average_count([])
