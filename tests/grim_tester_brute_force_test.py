import pytest
from grim import mean_tester
from decimal import Decimal
import random
import decimal


rounding_types = [decimal.ROUND_CEILING,
                  decimal.ROUND_DOWN,
                  decimal.ROUND_FLOOR,
                  decimal.ROUND_HALF_DOWN,
                  decimal.ROUND_HALF_EVEN,
                  decimal.ROUND_HALF_UP,
                  decimal.ROUND_UP, decimal.ROUND_05UP]


def check_consistency(mean, n, expected_consistency, rounding_type, samples):
    calculated_consistency = mean_tester.consistency_check(mean, n, rounding_type)
    assert calculated_consistency == expected_consistency, \
        f"The calculated score was: {calculated_consistency}, the expected score: {expected_consistency}. " + \
        f"The mean was: {mean} and the population size (n) was: {n}. (Passed as Decimals). " + \
        f"The rounding type was {rounding_type}.  " + \
        f"The raw data was: {samples}. "


def make_mean(raw_n, rounding_type, exp):

    n = Decimal(raw_n)

    samples = []
    for item in range(raw_n):
        samples.append(random.randint(-1000, 1000))

    total = Decimal(sum(samples))

    raw_mean = total/n
    rounded_mean = raw_mean.quantize(Decimal(exp), rounding=rounding_type)

    return {"rounded_mean": rounded_mean, "raw_mean": raw_mean, "samples": samples, "rounding_type": rounding_type}


@pytest.fixture(params=range(0, 1000))
def mean_data(request):

    num_samples = random.randint(1, 100)
    return make_mean(num_samples, random.choice(rounding_types), '0.001')


def test_simple__consistent(mean_data):

    check_consistency(mean_data['rounded_mean'],
                      len(mean_data['samples']),
                      True,
                      mean_data['rounding_type'],
                      mean_data['samples'])


def test_simple__inconsistent(mean_data):

    check_consistency(mean_data['rounded_mean'] + Decimal('0.001'),
                      len(mean_data['samples']),
                      False,
                      mean_data['rounding_type'],
                      mean_data['samples'])

    check_consistency(mean_data['rounded_mean'] + Decimal('-0.001'),
                      len(mean_data['samples']),
                      False,
                      mean_data['rounding_type'],
                      mean_data['samples'])

    check_consistency(mean_data['rounded_mean'] + Decimal('0.002'),
                      len(mean_data['samples']),
                      False,
                      mean_data['rounding_type'],
                      mean_data['samples'])

    check_consistency(mean_data['rounded_mean'] + Decimal('-0.002'),
                      len(mean_data['samples']),
                      False,
                      mean_data['rounding_type'],
                      mean_data['samples'])

    check_consistency(mean_data['rounded_mean'] + Decimal('0.003'),
                      len(mean_data['samples']),
                      False,
                      mean_data['rounding_type'],
                      mean_data['samples'])

    check_consistency(mean_data['rounded_mean'] + Decimal('-0.003'),
                      len(mean_data['samples']),
                      False,
                      mean_data['rounding_type'],
                      mean_data['samples'])

    check_consistency(mean_data['rounded_mean'] + Decimal('0.004'),
                      len(mean_data['samples']),
                      False,
                      mean_data['rounding_type'],
                      mean_data['samples'])

    check_consistency(mean_data['rounded_mean'] + Decimal('-0.004'),
                      len(mean_data['samples']),
                      False,
                      mean_data['rounding_type'],
                      mean_data['samples'])
