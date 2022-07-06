import numpy as np
import matplotlib.pyplot
import math

"""
Create functions to calculate count, mean, median, mode, range, sum,
standard deviation (for population and sample), variance (for population and sample), and Z-score
"""
def count(numbers):
    return len(numbers)

def mean(numbers):
    return sum(numbers) / len(numbers)

def median(numbers):
    numbers.sort()
    if len(numbers) % 2 == 0:
        return (numbers[len(numbers) // 2] + numbers[len(numbers) // 2 - 1]) / 2
    else:
        return numbers[len(numbers) // 2]

def mode(numbers):
    count = {}
    for num in numbers:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    max_count = max(count.values())
    return [num for num in count if count[num] == max_count]

def range(numbers):
    return max(numbers) - min(numbers)

def standard_deviation_population(numbers):
    return math.sqrt(sum([(num - mean(numbers)) ** 2 for num in numbers]) / len(numbers))

def standard_deviation_sample(numbers):
    return math.sqrt(sum([(num - mean(numbers)) ** 2 for num in numbers]) / (len(numbers) - 1))

def variance_population(numbers):
    return sum([(num - mean(numbers)) ** 2 for num in numbers]) / (len(numbers))

def variance_sample(numbers):
    return sum([(num - mean(numbers)) ** 2 for num in numbers]) / (len(numbers) - 1)

def z_score(numbers, mean_num, standard_deviation):
    return [(num - mean_num) / standard_deviation for num in numbers]

def quartiles(numbers):
    numbers.sort()
    Q1, Q2, Q3 = np.quantile(numbers, [0.25, 0.5, 0.75], axis=0)
    return {
        'Q1': Q1,
        'Q2': Q2,
        'Q3': Q3
    }

def iqr(numbers):
    numbers.sort()
    quartileList = quartiles(numbers)
    return quartileList['Q3'] - quartileList['Q1']

def outliers(numbers):
    numbers.sort()
    quartileList = quartiles(numbers)
    lower_outliers = [num for num in numbers if num < quartileList['Q1'] - 1.5 * iqr(numbers)]
    upper_outliers = [num for num in numbers if num > quartileList['Q3'] + 1.5 * iqr(numbers)]
    return {
        'lower_outliers': lower_outliers,
        'upper_outliers': upper_outliers
    }

def standard_error(numbers):
    return standard_deviation_population(numbers) / math.sqrt(len(numbers))

def frequency_table(numbers):
    count = {}
    for num in numbers:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    return count


def testFunctions():
    numbers = np.random.randint(0, 100, 11)
    numbers.sort()
    print(numbers)
    return {
        'count': count(numbers),
        'mean': mean(numbers),
        'median': median(numbers),
        'mode': mode(numbers),
        'range': range(numbers),
        'sum': sum(numbers),
        'standard_deviation_population': standard_deviation_population(numbers),
        'standard_deviation_sample': standard_deviation_sample(numbers),
        'variance_population': variance_population(numbers),
        'variance_sample': variance_sample(numbers),
        'z_score': z_score(numbers, mean(numbers), standard_deviation_population(numbers)),
        'quartiles': quartiles(numbers),
        'iqr': iqr(numbers),
        'outliers': outliers(numbers),
        'standard_error': standard_error(numbers),
        'frequency_table': frequency_table(numbers)
    }

finalStats = testFunctions()
for key, value in finalStats.items():
    print(key, ":", value)