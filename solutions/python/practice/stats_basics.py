def calculate_mean(numbers):
    if len(numbers) == 0:
        raise ValueError("cannot calculate the mean of an empty list")

    total = 0
    for number in numbers:
        total += number

    return total / len(numbers)


def above_average_count(numbers):
    if len(numbers) == 0:
        raise ValueError("cannot calculate the above average count of an empty list")

    count = 0
    mean = calculate_mean(numbers)
    for number in numbers:
        if number > mean:
            count += 1

    return count


# calculate min, max, range
def mmr(numbers):
    if len(numbers) == 0:
        raise ValueError("cannot calculate the min, max, range of an empty list")

    # solve without using builtin functions min() or max()
    min_num = numbers[0]
    max_num = numbers[0]
    for number in numbers:
        if number < min_num:
            min_num = number
        if number > max_num:
            max_num = number

    range_num = max_num - min_num
    return (min_num, max_num, range_num)


# distance from mean
def deviation(numbers):
    if len(numbers) == 0:
        raise ValueError("cannot calculate deviation of an empty list")

    deviations = []
    mean = calculate_mean(numbers)
    for number in numbers:
        deviation = number - mean
        deviations.append(deviation)
    return deviations
