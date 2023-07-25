from two_sum import Solution
import pytest

@pytest.mark.report_tracemalloc
@pytest.mark.report_duration
@pytest.mark.parametrize("expected,test_input", [([0,1],([2,7,11,15],9)), ([1,2],([3,2,4],6)),([0,1],([3,3],6))])
def test(expected,test_input):
    answer = Solution()
    assert answer.two_sum_SS(test_input[0],test_input[1]) == expected