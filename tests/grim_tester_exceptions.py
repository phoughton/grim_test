import pytest
from grim import mean_tester
import decimal


@pytest.mark.parametrize("mean, n", [
        ('10.00', '-1'),
        ('11.10', '0'),
        ('-4511.67', '-982743875438547')
])
def test_n_value_exceptions_for_negatives(mean, n):

    with pytest.raises(ValueError, match=r".*greater than zero.*"):
        mean_tester.consistency_check(mean, n)


@pytest.mark.parametrize("mean, n", [
        ('10.00', '1.01'),
        ('11.10', '0.5'),
        ('11.10', '0.000000003345'),
        ('-4511.67', '98274387.5438547')
])
def test_n_value_exceptions_for_integer(mean, n):

    with pytest.raises(ValueError, match=r".*whole number.*"):
        mean_tester.consistency_check(mean, n)

