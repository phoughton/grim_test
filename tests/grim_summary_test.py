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


def check_consistency_summary(mean, n, rounding_results):

    calc_consistency_summary = mean_tester.summary_consistency_check(mean, n)

    for rounding_type in rounding_types:
        expect_consistency = rounding_results[rounding_type]

        assert calc_consistency_summary[rounding_type] == expect_consistency, \
            f"The calc consistency was: {calc_consistency_summary[rounding_type]}, " + \
            f"The expected consistency: {expect_consistency}. " + \
            f"The mean was: {mean} and the population size (n) was: {n}. (Passed as Decimals). " + \
            f"The rounding type was {rounding_type}.  "

        expect_consistency = mean_tester.consistency_check(
            decimal.Decimal(mean), decimal.Decimal(n), rounding_type)
        assert calc_consistency_summary[rounding_type] == expect_consistency, \
            f"The calc consistency: {calc_consistency_summary[rounding_type]}, " + \
            f"The expected consistency: {expect_consistency}. " + \
            f"The mean was: {mean} and the population size (n) was: {n}.  (Passed as strings). " + \
            f"The rounding type was {rounding_type}.  "


@pytest.fixture()
def data_loader():
    test_data = pd.read_csv(os.path.join(os.path.dirname(__file__), TEST_DATA_FILE), dtype={'mean': str, 'n': str})

    test_sets = []
    test_data_dict = test_data.to_dict(orient='records')

    for row_index in range(0, len(test_data)):

        mean = test_data_dict[row_index]['mean'].strip('"')
        n = test_data_dict[row_index]['n'].strip('"')

        test_sets.append({"mean": mean,
                          "n": n,
                          "rounding_results": test_data_dict[row_index]})

    return test_sets


def test__csv(data_loader):
    for data_set in data_loader:
        check_consistency_summary(data_set["mean"],
                                  data_set["n"],
                                  data_set["rounding_results"]
                                  )
