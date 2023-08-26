from best_time_to_buy_and_sell_stock import Solution
import pytest

@pytest.mark.report_tracemalloc
@pytest.mark.report_duration
@pytest.mark.parametrize("expected,test_input", [(5,[7,1,5,3,6,4]), (0,[7,6,4,3,1])])
def test_1(expected,test_input):
    answer = Solution()
    assert answer.best_time_to_buy_and_sell_stock_SS(test_input) == expected