import pytest
import grim_tester
import decimal


@pytest.mark.parametrize("mean, n, expected_consistency", [
        ('10.00', '2', True),
        ('11.10', '19', False),
        ('11.10', '20', True),
        ('11.10', '21', False),
        ('1133.98', '28', False),
        ('11.09', '21', False),
        ('11.09', '22', False),
        ('11.09', '23', False),
        ('11.67', '3', False)
])
def test_simple_no_rounding(mean, n, expected_consistency):

    calculated_consistency = grim_tester.consistency_check(mean, n, None)
    assert calculated_consistency == expected_consistency, \
        f"The calculated score was: {calculated_consistency}, the expected score: {expected_consistency}. " + \
        f"The mean was: {mean} and the population size (n) was: {n}"


@pytest.mark.parametrize("mean, n, expected_consistency", [
        ('11.67', '3', True),
        ('11.09', '21', False),
        ('11.09', '22', True),
        ('11.09', '23', True),
        ('1133.98', '28', False)
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
        ('1133.98', '28', False)
])
def test_simple_rounding_half_down(mean, n, expected_consistency):

    calculated_consistency = grim_tester.consistency_check(mean, n, decimal.ROUND_HALF_DOWN)
    assert calculated_consistency == expected_consistency, \
        f"The calculated score was: {calculated_consistency}, the expected score: {expected_consistency}. " + \
        f"The mean was: {mean} and the population size (n) was: {n}"
