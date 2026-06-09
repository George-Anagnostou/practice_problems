import pytest

from practice.stats_basics import (
    calculate_mean,
    above_average_count,
    mmr,
    deviation,
    mode,
)


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


# test min_max_range
def test_mmr_multiple_positive_numbers():
    assert mmr([1, 2, 3, 4, 5]) == (1, 5, 4)


def test_mmr_single_number():
    assert mmr([4]) == (4, 4, 0)


def test_mmr_repeated():
    assert mmr([3, 3, 3]) == (3, 3, 0)


def test_mmr_decimal_numbers():
    assert mmr([1.2, 32.4, 50.1]) == (1.2, 50.1, 48.9)


def test_mmr_negative_numbers():
    assert mmr([10, -12, -2, 4, -1.23]) == (-12, 10, 22)


def test_mmr_raises_value_error():
    with pytest.raises(ValueError, match="empty list"):
        mmr([])


# test deviation (distance from mean)
def test_deviation_positive_numbers():
    assert deviation([8, 10, 12]) == [-2, 0, 2]


def test_deviation_negative_numbers():
    assert deviation([-1, 0, 1]) == [-1, 0, 1]


def test_deviation_raises_value_error():
    with pytest.raises(ValueError, match="empty list"):
        deviation([])


def test_deviation_decimal_mean():
    assert deviation([1, 2]) == pytest.approx([-0.5, 0.5])


def test_deviation_all_values_equal():
    assert deviation([7, 7, 7]) == [0, 0, 0]


def test_deviation_single_number():
    assert deviation([42]) == [0]


def test_deviation_sum_is_zero():
    assert sum(deviation([2, 4, 9])) == pytest.approx(0)


# test mode (most common value)
def test_mode_all_uppercase():
    assert mode(["A", "B", "A", "C", "A"]) == "A"


def test_mode_is_case_sensitive():
    assert mode(["A", "a", "a"]) == "a"


def test_mode_numbers():
    assert mode([1, 2, 3, 4, 5, 6, 7, 1]) == 1


def test_mode_tie():
    assert set(mode(["A", "A", "B", "B"])) == {"A", "B"}


def test_mode_one_item():
    assert mode(["A"]) == "A"


def test_mode_raises_value_error():
    with pytest.raises(ValueError, match="empty list"):
        mode([])
