from Sliding_Window_Maximum import Solution
import pytest

@pytest.mark.report_tracemalloc
@pytest.mark.report_duration
@pytest.mark.parametrize("expected,test_input", [([3,3,5,5,6,7],([1,3,-1,-3,5,3,6,7],3)), ([1],([1],1))])
def test_1(expected,test_input):
    answer = Solution()
    assert answer.Sliding_Window_Maximum_SS(test_input[0],test_input[1]) == expected