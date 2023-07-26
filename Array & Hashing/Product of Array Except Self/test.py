from product_of_array_except_self import Solution
import pytest

@pytest.mark.report_tracemalloc
@pytest.mark.report_duration
@pytest.mark.parametrize("expected,test_input", [([24,12,8,6],[1,2,3,4]), ([0,0,9,0,0],[-1,1,0,-3,3])])
def test(expected,test_input):
    answer = Solution()
    assert answer.product_of_array_except_self_SS(test_input) == expected