import pytest
from grim import grim_tester
import decimal


def check_consistency(mean, n, expected_consistency, rounding_type):
    calculated_consistency = grim_tester.consistency_check(mean, n, rounding_type)
    assert calculated_consistency == expected_consistency, \
        f"The calculated score was: {calculated_consistency}, the expected score: {expected_consistency}. " + \
        f"The mean was: {mean} and the population size (n) was: {n}. " + \
        f"The rounding type was ${rounding_type}.  "


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

    check_consistency(mean, n, expected_consistency, decimal.ROUND_HALF_UP)


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

    check_consistency(mean, n, expected_consistency, decimal.ROUND_HALF_DOWN)


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

    check_consistency(mean, n, expected_consistency, decimal.ROUND_CEILING)


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

    check_consistency(mean, n, expected_consistency, decimal.ROUND_FLOOR)


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

    check_consistency(mean, n, expected_consistency, decimal.ROUND_05UP)


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
    ('-11.10', '200', True),
    ('-11.09', '111', True),
    ('-133.98', '28', False),
    ('6.05', '121', True),
    ('6.10', '121', True),
    ('3.5', '9', False),
    ('1.600', '2000', True)
])
def test_simple_rounding_half_even(mean, n, expected_consistency):

    check_consistency(mean, n, expected_consistency, decimal.ROUND_HALF_EVEN)

