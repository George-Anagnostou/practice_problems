def calculate_mean(numbers):
    if len(numbers) == 0:
        raise ValueError("cannot calculate the mean of an empty list")

    total = 0
    for number in numbers:
        total += number

    return total / len(numbers)


def above_average_count(numbers):
    if len(numbers) == 0:
        raise ValueError("cannot calculate the mean of an empty list")

    count = 0
    mean = calculate_mean(numbers)
    for number in numbers:
        if number > mean:
            count += 1

    return count
