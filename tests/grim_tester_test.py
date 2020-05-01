import pytest
from grim import mean_tester
import decimal
import pandas as pd
import os


rounding_types = ["ROUND_CEILING",
                  "ROUND_DOWN",
                  "ROUND_FLOOR",
                  "ROUND_HALF_DOWN",
                  "ROUND_HALF_EVEN",
                  "ROUND_HALF_UP",
                  "ROUND_UP",
                  "ROUND_05UP"]

TEST_DATA_FILE = "grim_test_data.csv"


def check_consistency(mean, n, expected_consistency, rounding_type):
    calculated_consistency = mean_tester.consistency_check(mean, n, rounding_type)
    assert calculated_consistency == expected_consistency, \
        f"The calc consistency was: {calculated_consistency}, the expected consistency: {expected_consistency}. " + \
        f"The mean was: {mean} and the population size (n) was: {n}. (Passed as Decimals). " + \
        f"The rounding type was {rounding_type}.  "

    expected_consistency = mean_tester.consistency_check(decimal.Decimal(mean), decimal.Decimal(n), rounding_type)
    assert calculated_consistency == expected_consistency, \
        f"The calc consistency: {calculated_consistency}, the expected consistency: {expected_consistency}. " + \
        f"The mean was: {mean} and the population size (n) was: {n}.  (Passed as strings). " + \
        f"The rounding type was {rounding_type}.  "


@pytest.fixture()
def data_loader():
    test_data = pd.read_csv(os.path.join(os.path.dirname(__file__), TEST_DATA_FILE), dtype={'mean': str, 'n': str})

    test_sets = []

    for rounding_type in rounding_types:
        for row_index in range(0, len(test_data)):

            mean = test_data.iloc[row_index]['mean'].strip('"')
            n = test_data.iloc[row_index]['n'].strip('"')
            expected_consistency = test_data.iloc[row_index][rounding_type]

            test_sets.append({"mean": mean,
                              "n": n,
                              "expected_consistency": expected_consistency,
                              "rounding_type": rounding_type})

    return test_sets


def test__csv(data_loader):
    print(data_loader)
    for data_set in data_loader:
        print(data_set)
        check_consistency(data_set["mean"],
                          data_set["n"],
                          data_set["expected_consistency"],
                          getattr(decimal, data_set["rounding_type"]))
