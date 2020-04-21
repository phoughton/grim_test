import pytest
import grim_tester
import decimal


@pytest.mark.parametrize("mean, n", [
        ('10.00', '-1'),
        ('11.10', '0'),
        ('-4511.67', '-982743875438547')
])
def test_n_value_exceptions_for_negatives(mean, n):

    with pytest.raises(ValueError, match=r".*greater than zero.*"):
        grim_tester.consistency_check(mean, n)


@pytest.mark.parametrize("mean, n", [
        ('10.00', '1.01'),
        ('11.10', '0.5'),
        ('11.10', '0.000000003345'),
        ('-4511.67', '98274387.5438547')
])
def test_n_value_exceptions_for_integer(mean, n):

    with pytest.raises(ValueError, match=r".*whole number.*"):
        grim_tester.consistency_check(mean, n)


@pytest.mark.parametrize("mean, n, expected_consistency", [
        ('10.00', '2', True),
        ('11.10', '19', False),
        ('11.10', '20', True),
        ('11.10', '21', False),
        ('234567.3333', '3', False),
        ('1133.98', '28', False),
        ('11.09', '21', False),
        ('11.09', '22', False),
        ('11.09', '23', False),
        ('11.67', '3', False)
])
def test_simple_no_rounding(mean, n, expected_consistency):

    calculated_consistency = grim_tester.consistency_check(mean, n)
    assert calculated_consistency == expected_consistency, \
        f"The calculated score was: {calculated_consistency}, the expected score: {expected_consistency}. " + \
        f"The mean was: {mean} and the population size (n) was: {n}"


@pytest.mark.parametrize("mean, n, expected_consistency", [
    ('11.67', '3', True),
    ('11.09', '21', False),
    ('11.09', '22', True),
    ('11.09', '23', True),
    ('0.3333333333333', '9', True),
    ('133.98', '28', False),
    ('-11.67', '3', True),
    ('-11.66', '3', False),
    ('-11.09', '21', False),
    ('-11.09', '22', True),
    ('-11.09', '23', True),
    ('-133.98', '28', False)
])
def test_simple_rounding_half_up(mean, n, expected_consistency):

    calculated_consistency = grim_tester.consistency_check(mean, n, decimal.ROUND_HALF_UP)
    assert calculated_consistency == expected_consistency, \
        f"The calculated score was: {calculated_consistency}, the expected score: {expected_consistency}. " + \
        f"The mean was: {mean} and the population size (n) was: {n}"


@pytest.mark.parametrize("mean, n, expected_consistency", [
    ('11.67', '3', True),
    ('11.09', '21', False),
    ('11.09', '22', True),
    ('133.98', '28', False),
    ('-11.67', '3', True),
    ('-11.66', '3', False),
    ('-11.6667', '3', True),
    ('-11.6666', '3', False),
    ('-11.09', '21', False),
    ('-11.09', '22', True),
    ('-133.98', '28', False)
])
def test_simple_rounding_half_down(mean, n, expected_consistency):

    calculated_consistency = grim_tester.consistency_check(mean, n, decimal.ROUND_HALF_DOWN)
    assert calculated_consistency == expected_consistency, \
        f"The calculated score was: {calculated_consistency}, the expected score: {expected_consistency}. " + \
        f"The mean was: {mean} and the population size (n) was: {n}"


@pytest.mark.parametrize("mean, n, expected_consistency", [
    ('11.67', '3', True),
    ('11.09', '21', False),
    ('11.09', '22', False),
    ('133.98', '28', False),
    ('-11.67', '3', False),
    ('-11.66', '3', True),
    ('-11.6667', '3', False),
    ('-11.6666', '3', True),
    ('-11.09', '21', True),
    ('-11.09', '22', True),
    ('-133.98', '28', False)
])
def test_simple_rounding_ceiling(mean, n, expected_consistency):

    calculated_consistency = grim_tester.consistency_check(mean, n, decimal.ROUND_CEILING)
    assert calculated_consistency == expected_consistency, \
        f"The calculated score was: {calculated_consistency}, the expected score: {expected_consistency}. " + \
        f"The mean was: {mean} and the population size (n) was: {n}"


@pytest.mark.parametrize("mean, n, expected_consistency", [
   ('11.67', '3', False),
   ('11.09', '21', True),
   ('11.09', '22', True),
    ('133.98', '28', False),
    ('-11.67', '3', True),
    ('-11.66', '3', False),
    ('-11.6667', '3', True),
    ('-11.6666', '3', False),
    ('-11.09', '21', False),
    ('-11.09', '22', False),
    ('-133.98', '28', False),
    ('6.10', '121', True)
])
def test_simple_rounding_floor(mean, n, expected_consistency):

    calculated_consistency = grim_tester.consistency_check(mean, n, decimal.ROUND_FLOOR)
    assert calculated_consistency == expected_consistency, \
        f"The calculated score was: {calculated_consistency}, the expected score: {expected_consistency}. " + \
        f"The mean was: {mean} and the population size (n) was: {n}"


@pytest.mark.parametrize("mean, n, expected_consistency", [
    ('11.67', '3', False),
    ('11.09', '21', True),
    ('11.09', '22', True),
    ('133.98', '28', False),
    ('-11.67', '3', False),
    ('-11.66', '3', True),
    ('-11.6667', '3', False),
    ('-11.6666', '3', True),
    ('-11.09', '21', True),
    ('-11.10', '200', True),
    ('-11.09', '111', True),
    ('-133.98', '28', False),
    ('6.05', '121', False),
    ('6.10', '121', False)
])
def test_simple_rounding_05up(mean, n, expected_consistency):

    calculated_consistency = grim_tester.consistency_check(mean, n, decimal.ROUND_05UP)
    assert calculated_consistency == expected_consistency, \
        f"The calculated score was: {calculated_consistency}, the expected score: {expected_consistency}. " + \
        f"The mean was: {mean} and the population size (n) was: {n}"
